import streamlit as st
import pandas as pd
from datetime import datetime
from travel_calculator import (get_per_diem_rates, load_airfare_data,
                               get_unique_states, get_cities_for_state,
                               get_yca_fare, load_perdiem_data,
                               get_airports_for_city, calculate_travel_costs,
                               create_budget_justification,
                               verify_data_presence)


def main():
    st.title('Travel Cost Calculator')
    st.markdown("""
        This tool is designed to assist in planning and budgeting for official travel.
        It calculates estimated travel costs based on GSA per diem rates and airfare data for FY24.
        For further information regarding travel policies, please consult [City of Chicago Travel Guidelines](https://www.chicago.gov/dam/city/depts/dps/ContractAdministration/Forms/CityofChicago_TravelGuidelines.pdf) and the [Uniform Guidance for Travel Costs](https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-E/subject-group-ECFRed1f39f9b3d4e72/section-200.475).
                
        ### Data Sources
        - [GSA Per Diem Rates](https://www.gsa.gov/travel/plan-book/per-diem-rates): Utilized for determining daily allowances for lodging, meals, and incidental expenses for travel within the United States. The rates are specified for different locations and times of the year.
        - [GSA Airfare Database](https://www.gsa.gov/travel/plan-a-trip/transportation-airfare-rates-pov-rates-etc/airfare-rates-city-pair-program): Provides contract award airfare rates, which are typically available for government travelers and are used to estimate air travel costs between major destinations.

        
        ### Instructions
        - **Select your origin and destination:** Start by choosing your departure and arrival cities.
        - **Enter travel dates and number of staff:** Specify the travel period and the number of people traveling.
        - **Calculate costs and generate budget justification:** After entering details, review the estimated expenses and a detailed budget justification.
        """)

    col1, col2, col3 = st.columns(3)

    airfare_df = load_airfare_data()
    perdiem_df, standard_rate = load_perdiem_data()
    states = get_unique_states(airfare_df)

    default_origin_state = 'IL'
    default_origin_city = 'Chicago'
    default_origin_airport = 'ORD'

    origin_state = col1.selectbox('Select Origin State', states, index=states.index(
        default_origin_state) if default_origin_state in states else 0)
    origin_cities = get_cities_for_state(airfare_df, origin_state)
    origin_city = col1.selectbox('Select Origin City', origin_cities, index=origin_cities.index(
        default_origin_city) if default_origin_city in origin_cities else 0)

    # Fetch and display available airports for the selected city
    origin_airports = get_airports_for_city(
        airfare_df, origin_city, origin_state)
    selected_airport = col1.selectbox('Select Origin Airport', origin_airports, index=origin_airports.index(
        default_origin_airport) if default_origin_airport in origin_airports else 0)

    selected_state = col2.selectbox('Select Travel State', states)
    cities = get_cities_for_state(airfare_df, selected_state)
    selected_city = col2.selectbox('Select Travel City', cities)

    # Dates UI Components
    start_date = col3.date_input("Start Date", value=pd.to_datetime('today'))
    end_date = col3.date_input("End Date", value=pd.to_datetime(
        'today') + pd.DateOffset(days=1))

    num_staff = col2.number_input('Number of Staff', min_value=1, step=1)

    airfare_rate = get_yca_fare(airfare_df, selected_airport,
                                origin_city, origin_state, selected_city, selected_state)

    if airfare_rate == 0 or airfare_rate is None or airfare_rate == "No fare data available":
        st.error("With current inputs, there is no direct route available for the selected cities. Please enter the airfare manually or select the nearest major city. The one-way YCA fare can be found here: https://www.gsa.gov/travel/plan-a-trip/transportation-airfare-rates-pov-rates-etc/airfare-rates-city-pair-program?gsaredirect=portalcategory")
        airfare_rate = st.number_input(
            "Enter Airfare Manually (one way):", min_value=0.0, format="%.2f")

    if st.button('Calculate Travel Costs'):
        lodging_rate, mie_rate = get_per_diem_rates(
            perdiem_df, standard_rate, selected_city, start_date, end_date)
        lodging_rate, lodging_error = verify_data_presence(
            lodging_rate, "lodging rate")
        mie_rate, mie_error = verify_data_presence(mie_rate, "M&IE rate")
        if lodging_error or mie_error:
            return

        costs = calculate_travel_costs(start_date, end_date, num_staff,
                                       airfare_rate, lodging_rate, mie_rate,
                                       baggage_fee=50,
                                       ground_transport_source=50,
                                       ground_transport_destination=30)

        st.subheader(
            f"Total Travel Cost: ${costs['Total budgeted travel cost']}")

        st.subheader("Budget Justification Language for Grant")

        justification_text = create_budget_justification(origin_city,
                                                         selected_state,
                                                         selected_city,
                                                         start_date, end_date,
                                                         num_staff, costs)
        st.text_area("Copy and paste this into your grant budget documentation:",
                     justification_text, height=175)
        st.write("These are estimated travel costs based on the most current GSA data. If you need more current values, please change your costs manually.")

        # st.subheader("Costs Summary")
        # st.write(costs)


if __name__ == "__main__":
    main()
