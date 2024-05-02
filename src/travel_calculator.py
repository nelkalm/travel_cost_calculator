import pandas as pd
import streamlit as st
import os
from datetime import datetime, date
from data import city_mapping


def verify_data_presence(value, data_type):
    """Check if the necessary data is present and return appropriate messages or values."""
    if value is None:
        st.error(
            f"No available {data_type}. Please select another nearest city or check your inputs.")
        return None, True
    return value, False


def normalize_city_name(city_name, state_code):
    """Normalize city names based on predefined mapping and state."""
    try:
        city_name = str(city_name).strip().title(
        ) if not pd.isna(city_name) else ''
        state_code = str(state_code).strip().upper(
        ) if not pd.isna(state_code) else ''

        normalized_name = city_mapping.get((city_name, state_code), city_name)
        return normalized_name
    except Exception as e:
        print(f"Error normalizing city name: {e}")
        return city_name  # Fallback to original city name if error occurs


@st.cache_data
def load_airfare_data():
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, '..', 'data')
    airfare_path = os.path.join(data_path, 'airfare.csv')
    airfare_df = pd.read_csv(airfare_path)

    # Apply normalization for both origin and destination city names
    airfare_df['Normalized Origin City Name'] = airfare_df.apply(
        lambda row: normalize_city_name(row['ORIGIN_CITY_NAME'], row['ORIGIN_STATE']), axis=1)
    airfare_df['Normalized Destination City Name'] = airfare_df.apply(
        lambda row: normalize_city_name(row['DESTINATION_CITY_NAME'], row['DESTINATION_STATE']), axis=1)

    return airfare_df


@st.cache_data
def get_unique_states(airfare_df):
    states = airfare_df['DESTINATION_STATE'].fillna(
        'Unknown').astype(str).unique().tolist()
    states = sorted(states)
    return ['Other'] + states


@st.cache_data
def get_cities_for_state(airfare_df, state):
    if state == 'Other':
        # Assuming 'Other' should check the destination country is not the USA
        return sorted(airfare_df[airfare_df['DESTINATION_COUNTRY'] != 'USA']['Normalized Destination City Name'].unique().tolist())
    else:
        cities = sorted(airfare_df[(airfare_df['DESTINATION_STATE'] == state) &
                                   (airfare_df['DESTINATION_COUNTRY'] == 'USA')]['Normalized Destination City Name'].unique().tolist())
        print(f"Cities in state {state}: {cities}")  # Debugging statement
        return cities


def get_airports_for_city(airfare_df, city, state):
    """Fetch airports for the given city and state."""
    filtered_data = airfare_df[(airfare_df['Normalized Origin City Name'] == city) &
                               (airfare_df['ORIGIN_STATE'] == state)]
    airports = filtered_data['ORIGIN_AIRPORT_ABBREV'].unique()
    return airports.tolist()


@st.cache_data
def get_yca_fare(airfare_df, airport_abbr, origin_city, origin_state, selected_city, selected_state):
    """Fetch the YCA fare based on specific city and airport."""
    city_data = airfare_df[
        (airfare_df['ORIGIN_AIRPORT_ABBREV'] == airport_abbr) &
        (airfare_df['Normalized Origin City Name'] == origin_city) &
        (airfare_df['ORIGIN_STATE'] == origin_state) &
        (airfare_df['Normalized Destination City Name'] == selected_city) &
        (airfare_df['DESTINATION_STATE'] == selected_state)
    ]
    if not city_data.empty:
        return city_data.iloc[0]['YCA_FARE']
    else:
        return "No fare data available"


def parse_season_date(date_str, default_year):
    """Parse dates that only include the month and day by appending a default year."""
    # First, check if date_str is already a Timestamp
    if isinstance(date_str, pd.Timestamp):
        return date_str  # If it's a Timestamp, return it directly

    # Handle non-string or NA values safely
    if not isinstance(date_str, str) or pd.isna(date_str):
        return pd.NaT

    try:
        # Strip any leading/trailing whitespace and parse the date
        return pd.to_datetime(f'{date_str.strip()} {default_year}', format='%B %d %Y')
    except ValueError:
        return pd.NaT  # Return NaT if parsing fails


def adjust_season_dates(row, event_start_date):
    # Parse season dates from the dataframe
    season_start = pd.to_datetime(row['Season Begin'])
    season_end = pd.to_datetime(row['Season End'])

    # Adjust the year of the season dates based on the event start date
    if season_start.month > season_end.month:
        # This handles a season that wraps to the next year (e.g., Oct to Jan)
        if event_start_date.month < season_start.month:
            season_start = season_start.replace(year=event_start_date.year - 1)
            season_end = season_end.replace(year=event_start_date.year)
        else:
            season_start = season_start.replace(year=event_start_date.year)
            season_end = season_end.replace(year=event_start_date.year + 1)
    else:
        # Season does not wrap
        season_start = season_start.replace(year=event_start_date.year)
        season_end = season_end.replace(year=event_start_date.year)

    return season_start, season_end


@st.cache_data
def load_perdiem_data():
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, '..', 'data')
    perdiem_path = os.path.join(data_path, 'perdiem24.csv')
    perdiem_df = pd.read_csv(perdiem_path)

    standard_rate = perdiem_df[perdiem_df['Destination'] == 'All'].iloc[0]
    perdiem_df = perdiem_df[perdiem_df['Destination'] != 'All']

    # Get the current year or a specific year if needed
    current_year = datetime.now().year

    # Apply date parsing
    perdiem_df['Season Begin'] = perdiem_df['Season Begin'].apply(
        parse_season_date, default_year=current_year)
    perdiem_df['Season End'] = perdiem_df['Season End'].apply(
        parse_season_date, default_year=current_year)

    # Normalize city names
    perdiem_df['Normalized Destination'] = perdiem_df.apply(
        lambda row: normalize_city_name(row['Destination'], row['State']), axis=1)
    return perdiem_df, standard_rate


@st.cache_data
def get_per_diem_rates(perdiem_df, standard_rate, city, start_date, end_date):
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)

    filtered_df = perdiem_df[perdiem_df['Normalized Destination'].str.lower(
    ) == city.lower()]

    for index, row in filtered_df.iterrows():
        season_start, season_end = adjust_season_dates(row, start_date)

        # Extend season_end to include the entire last day
        season_end += pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

        if season_start <= end_date and season_end >= start_date:
            return row['FY24 Lodging Rate'], row['FY24 M&IE']

    return standard_rate['FY24 Lodging Rate'], standard_rate['FY24 M&IE']


def clean_currency(value):
    """Remove currency symbols and commas from strings and convert to float."""
    if isinstance(value, str):
        value = value.replace('$', '').replace(',', '')
    try:
        return float(value)
    except ValueError:
        return 0.0


def calculate_travel_costs(start_date, end_date, num_staff, airfare_rate,
                           lodging_rate, mie_rate, baggage_fee,
                           ground_transport_source,
                           ground_transport_destination):
    airfare_rate = clean_currency(airfare_rate)
    lodging_rate = clean_currency(lodging_rate)
    mie_rate = clean_currency(mie_rate)
    baggage_fee = clean_currency(baggage_fee)
    ground_transport_destination = clean_currency(ground_transport_destination)

    total_days = (end_date - start_date).days + 2

    # Costs calculation
    airfare_total = airfare_rate * 2
    # Assuming the stay is one night less than total days
    hotel_total = total_days * lodging_rate
    first_and_last_per_diem_rate = mie_rate * 0.75 * 2
    per_diem_rate_in_between = mie_rate * (total_days - 2)
    per_diem_total = first_and_last_per_diem_rate + per_diem_rate_in_between
    baggage_total = baggage_fee

    total_cost_per_pax = airfare_total + hotel_total + \
        per_diem_total + baggage_total + ground_transport_destination
    total_budgeted_cost = total_cost_per_pax

    return {
        "Airfare RT": int(airfare_total),
        "Lodging rate": int(lodging_rate),
        "Hotel": int(hotel_total),
        "Total days": total_days,
        "Hotel nights": total_days - 1,
        "MIE rate": mie_rate,
        "First/Last Day MIE": format(first_and_last_per_diem_rate, ".2f"),
        "Middle Days MIE": format(per_diem_rate_in_between, ".2f"),
        "Meals and incidentals": format(per_diem_total, ".2f"),
        "Baggage fees two way": int(baggage_total),
        "Ground Transport Total": int(ground_transport_destination),
        "Total per pax": format(total_cost_per_pax, ".2f"),
        "Number of pax": num_staff,
        "Total budgeted travel cost": format(total_budgeted_cost * num_staff, ".2f")
    }


def create_budget_justification(origin_city, travel_state, travel_city,
                                start_date, end_date, num_staff, costs):
    start_date_str = start_date.strftime("%m/%d/%Y")
    end_date_str = end_date.strftime("%m/%d/%Y")

    justification = (
        f"Travel to {travel_city}, {travel_state} from {start_date_str} to {end_date_str} - "
        f"Airfare round trip (${costs['Airfare RT']}); "
        f"Lodging for {costs['Hotel nights']} nights x ${costs['Lodging rate']}/night (${costs['Hotel']}); "
        f"Per Diem/meals for {costs['Total days']} days; ${costs['First/Last Day MIE']} "
        f"for first day and last day (75% x MI&E cost for 2 days), ${costs['Middle Days MIE']} for days in between "
        f"(${costs['First/Last Day MIE']} + ${costs['Middle Days MIE']} = ${costs['Meals and incidentals']}); "
        f"Baggage fees $50/ way (${costs['Baggage fees two way']}); "
        f"Ground Transport to and from airport for ${costs['Ground Transport Total']} trip/person in {travel_city} "
        f" = ${costs['Total per pax']} x {num_staff} staff = ${costs['Total budgeted travel cost']}"
    )

    return justification
