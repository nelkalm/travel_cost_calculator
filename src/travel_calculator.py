import pandas as pd
import streamlit as st
import os
from datetime import datetime


def get_cities_by_state(df, state):
    """
    Returns a list of cities for the given state from the travel data
    DataFrame.

    Args:
        travel_data_df (DataFrame): DataFrame containing travel data.
        state (str): The state for which cities are being listed.

    Returns:
        list: A list of cities available in the specified state.
    """
    filtered_df = df[df['State'].str.lower(
    ) == state.lower()]
    cities_list = filtered_df['Destination'].unique().tolist()
    return cities_list


def get_unique_states(df):
    states = df['State'].fillna(
        'Unknown').astype(str).unique().tolist()
    states = sorted(states)
    return ['Other'] + states


def verify_data_presence(value, data_type):
    """Check if the necessary data is present and return appropriate messages or values."""
    if value is None:
        st.error(
            f"No available {data_type}. Please select another nearest city or check your inputs.")
        return None, True
    return value, False


def normalize_city_name(city_name, state_code):
    return f"{city_name.lower().strip()}_{state_code.lower().strip()}"


def load_perdiem_data():
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, '..', 'data')
    perdiem_path = os.path.join(data_path, 'perdiem24.csv')
    perdiem_df = pd.read_csv(perdiem_path)

    perdiem_df = perdiem_df[perdiem_df['Destination'] != 'All']

    current_year = datetime.now().year
    perdiem_df['Season Begin'] = perdiem_df['Season Begin'].apply(
        parse_season_date, default_year=current_year)
    perdiem_df['Season End'] = perdiem_df['Season End'].apply(
        parse_season_date, default_year=current_year)
    perdiem_df['Normalized Destination'] = perdiem_df.apply(
        lambda row: normalize_city_name(row['Destination'], row['State']), axis=1)

    return perdiem_df


def parse_season_date(date_str, default_year):
    """Parse dates that only include the month and day by appending a default year."""
    if isinstance(date_str, pd.Timestamp):
        return date_str
    if not isinstance(date_str, str) or pd.isna(date_str):
        return pd.NaT
    try:
        return pd.to_datetime(f'{date_str.strip()} {default_year}', format='%B %d %Y')
    except ValueError:
        return pd.NaT


def adjust_season_dates(row, event_start_date):
    season_start = pd.to_datetime(row['Season Begin']).date(
    ) if pd.notna(row['Season Begin']) else None
    season_end = pd.to_datetime(row['Season End']).date(
    ) if pd.notna(row['Season End']) else None

    # If both season start and end are None, consider it year-round
    if season_start is None and season_end is None:
        return None, None

    if season_start and season_end:
        if season_start.month > season_end.month:
            if event_start_date.month < season_start.month:
                season_start = season_start.replace(
                    year=event_start_date.year - 1)
                season_end = season_end.replace(year=event_start_date.year)
            else:
                season_start = season_start.replace(year=event_start_date.year)
                season_end = season_end.replace(year=event_start_date.year + 1)
        else:
            season_start = season_start.replace(year=event_start_date.year)
            season_end = season_end.replace(year=event_start_date.year)

    return season_start, season_end


def get_full_state_name(abbreviation):
    state_abbreviations_to_full = {
        "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
        "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia",
        "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois",
        "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
        "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota",
        "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
        "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
        "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
        "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
        "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia",
        "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"
    }
    return state_abbreviations_to_full.get(abbreviation.upper(), abbreviation)


def retrieve_rates(city, state, start_date, end_date, df):
    start_date_timestamp = pd.to_datetime(start_date)
    end_date_timestamp = pd.to_datetime(end_date)
    df['Normalized Destination'] = df.apply(
        lambda row: normalize_city_name(row['Destination'], row['State']), axis=1)

    filtered_df = df[(df['Normalized Destination'] ==
                      normalize_city_name(city, state))]

    for _, row in filtered_df.iterrows():
        season_start, season_end = adjust_season_dates(
            row, start_date_timestamp)

        # If season start and end are None, consider it year-round
        if season_start is None and season_end is None:
            return row['FY24 Lodging Rate'], row['FY24 M&IE']

        if season_start <= start_date_timestamp.date() <= season_end and season_start <= end_date_timestamp.date() <= season_end:
            return row['FY24 Lodging Rate'], row['FY24 M&IE']

    return None, None


def load_ground_transport_data():
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, '..', 'data')
    csv_path = os.path.join(data_path, 'ground_transport_rates.csv')
    ground_transport_df = pd.read_csv(csv_path)
    return ground_transport_df


def get_ground_transport_rate(ground_transport_df, city, state):
    filtered_df = ground_transport_df[(ground_transport_df['City'].str.lower() == city.lower()) &
                                      (ground_transport_df['State'].str.lower() == state.lower())]
    if not filtered_df.empty:
        return filtered_df.iloc[0]['Ground_Transport']
    else:
        default_df = ground_transport_df[(ground_transport_df['City'].str.lower() == 'other') &
                                         (ground_transport_df['State'].str.lower() == state.lower())]
        if not default_df.empty:
            return default_df.iloc[0]['Ground_Transport']
    return None


def get_travel_details(city, state, start_date, end_date, perdiem_df, ground_transport_df):
    full_state_name = get_full_state_name(state)
    ground_transport_rate = get_ground_transport_rate(
        ground_transport_df, city, full_state_name)
    lodging_rate, mie_rate = retrieve_rates(
        city, state, start_date, end_date, perdiem_df)

    return lodging_rate, mie_rate, ground_transport_rate


def clean_currency(value):
    """
    Remove currency symbols and commas from a string and convert it to a float.

    Args:
        value (str): String value to clean.

    Returns:
        float: The numeric value of the input string.
    """
    if value is None:
        return 0.0
    if isinstance(value, str):
        value = value.replace('$', '').replace(',', '')
    try:
        return float(value)
    except ValueError:
        return 0.0


def calculate_travel_costs(start_date, end_date, num_staff, airfare_rate,
                           lodging_rate, mie_rate,
                           ground_transport_destination):
    """
    Calculate total travel costs based on input parameters.

    Args:
        start_date (datetime): The start date of travel.
        end_date (datetime): The end date of travel.
        num_staff (int): Number of staff members travelling.
        airfare_rate (float): Cost of one-way airfare per staff member.
        lodging_rate (float): Daily lodging rate.
        mie_rate (float): Daily per diem rate.
        ground_transport_destination (float): Total cost of ground transport
        at the destination.

    Returns:
        dict: A dictionary containing detailed cost breakdown.
    """
    airfare_rate = clean_currency(airfare_rate)
    lodging_rate = clean_currency(lodging_rate)
    mie_rate = clean_currency(mie_rate)
    ground_transport_destination = clean_currency(ground_transport_destination)

    total_days = (end_date - start_date).days + 1
    # Costs calculation
    airfare_total = airfare_rate * 2  # Assuming round trip
    hotel_total = total_days * lodging_rate  # Total lodging cost
    first_and_last_per_diem_rate = mie_rate * \
        0.75 * 2  # 75% for first and last days
    per_diem_rate_in_between = mie_rate * \
        (total_days - 1)  # Full rate for middle days
    per_diem_total = first_and_last_per_diem_rate + per_diem_rate_in_between

    total_cost_per_pax = airfare_total + hotel_total + \
        per_diem_total + ground_transport_destination
    total_budgeted_cost = total_cost_per_pax * num_staff

    return {
        "Airfare RT": int(airfare_total),
        "Lodging rate": format(int(lodging_rate), ","),
        "Hotel": format(int(hotel_total), ","),
        "Total days": total_days + 1,
        "Hotel nights": total_days,
        "MIE rate": mie_rate,
        "First/Last Day MIE": format(first_and_last_per_diem_rate, ".2f"),
        "Middle Days MIE": format(per_diem_rate_in_between, ".2f"),
        "Meals and incidentals": format(per_diem_total, ".2f"),
        "Ground Transport Total": int(ground_transport_destination),
        "Total per pax": f"{total_cost_per_pax:,.2f}",
        "Number of pax": num_staff,
        "Total budgeted travel cost": f"{total_budgeted_cost:,.2f}",
    }


def create_budget_justification(travel_state, travel_city, start_date,
                                end_date, num_staff, costs):
    """
    Create a budget justification text based on travel details and calculated 
    costs.

    Args:
        travel_state (str): The state of the destination.
        travel_city (str): The city of the destination.
        start_date (datetime): The start date of the travel.
        end_date (datetime): The end date of the travel.
        num_staff (int): The number of staff members traveling.
        costs (dict): A dictionary containing all the calculated cost details.

    Returns:
        str: A formatted string of budget justification.
    """
    start_date_str = start_date.strftime("%m/%d/%Y")
    end_date_str = end_date.strftime("%m/%d/%Y")

    justification = (
        f"Travel to {travel_city}, {travel_state} from {start_date_str} to {end_date_str} - "
        f"Airfare round trip (${costs['Airfare RT']}); "
        f"Lodging for {costs['Hotel nights']} nights x ${costs['Lodging rate']}/night (${costs['Hotel']}); "
        f"Per Diem/meals for {costs['Total days']} days x ${costs['First/Last Day MIE']} "
        f"for first day and last day, ${costs['Middle Days MIE']} for days in between "
        f"(${costs['First/Last Day MIE']} + ${costs['Middle Days MIE']} = ${costs['Meals and incidentals']}); "
        f"Ground Transport to and from airport for ${costs['Ground Transport Total']} trip/person in {travel_city} "
        f"= ${costs['Total per pax']} x {num_staff} staff = ${costs['Total budgeted travel cost']}"
    )

    return justification


if __name__ == "__main__":
    perdiem_df, standard_rate = load_perdiem_data()
    ground_transport_df = load_ground_transport_data()
    city = "Denver"
    state = "CO"
    start_date = '10/01/2024'
    end_date = '10/05/2024'
    airfare_rate = 300
    num_staff = 2

    lodging_rate, mie_rate, ground_transport_rate = get_travel_details(
        city, state, start_date, end_date, perdiem_df, ground_transport_df)

    print(
        f"Lodging Rate: {lodging_rate}, M&IE: {mie_rate}, Ground Transport Rate: {ground_transport_rate}")

    costs = calculate_travel_costs(start_date, end_date, num_staff, airfare_rate,
                                   lodging_rate, mie_rate,
                                   ground_transport_rate)

    print(create_budget_justification(state, city, start_date,
                                      end_date, num_staff, costs))
