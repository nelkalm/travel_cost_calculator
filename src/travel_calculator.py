import pandas as pd
import os


def load_travel_data():
    """
    Load travel reimbursement rates from a CSV file and return the data frame
    and a list of unique states.

    Returns:
        tuple: A tuple containing the DataFrame of travel data and a sorted
        list of unique states.
    """
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, '..', 'data')
    csv_path = os.path.join(data_path, 'travel_reimbursement_rates.csv')
    travel_data_df = pd.read_csv(csv_path)
    unique_states = sorted(travel_data_df['State'].unique())
    return travel_data_df, unique_states


def get_city_group_rates(travel_data_df, city, state):
    """
    Fetch group rates for lodging, ground transport, and per diem for a
    specific city and state.

    Args:
        travel_data_df (DataFrame): DataFrame containing travel data.
        city (str): The city for which rates are being queried.
        state (str): The state in which the city is located.

    Returns:
        tuple: A tuple containing the lodging rate, ground transport rate, and
        per diem rate; or None values if no data found.
    """
    matched_row = travel_data_df[(travel_data_df['City'].str.lower() == city
                                  .lower()) &
                                 (travel_data_df['State'].str.lower() == state
                                  .lower())]
    if not matched_row.empty:
        return (matched_row.iloc[0]['Lodging'],
                matched_row.iloc[0]['Ground_Transport'],
                matched_row.iloc[0]['Per_Diem'])
    else:
        return None, None, None  # Default or error handling


def get_cities_by_state(travel_data_df, state):
    """
    Returns a list of cities for the given state from the travel data
    DataFrame.

    Args:
        travel_data_df (DataFrame): DataFrame containing travel data.
        state (str): The state for which cities are being listed.

    Returns:
        list: A list of cities available in the specified state.
    """
    filtered_df = travel_data_df[travel_data_df['State'].str.lower(
    ) == state.lower()]
    cities_list = filtered_df['City'].tolist()
    return cities_list


def clean_currency(value):
    """
    Remove currency symbols and commas from a string and convert it to a float.

    Args:
        value (str): String value to clean.

    Returns:
        float: The numeric value of the input string.
    """
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
    total_budgeted_cost = total_cost_per_pax * num_staff  # Total cost for all staff

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
