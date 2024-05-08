import streamlit as st
import pandas as pd
from datetime import datetime
from travel_calculator import (get_cities_by_state, get_unique_states,
                               load_perdiem_data, retrieve_rates,
                               load_ground_transport_data, get_travel_details,
                               calculate_travel_costs,
                               create_budget_justification,
                               verify_data_presence)

st.set_page_config(page_title="Travel Cost Calculator")


def main():
    st.title('Travel Cost Calculator')
    st.markdown("""
        This tool is designed to assist in planning and budgeting for official travel.
        It calculates estimated travel costs based on GSA per diem rates and airfare data for FY24.
        For further information regarding travel policies, please consult [City of Chicago Travel Guidelines](https://www.chicago.gov/content/dam/city/depts/dps/ContractAdministration/Forms/CityofChicago_TravelGuidelines.pdf) and the [Uniform Guidance for Travel Costs](https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-E/subject-group-ECFRed1f39f9b3d4e72/section-200.475).

        ### Data Sources
        - [GSA Per Diem Rates](https://www.gsa.gov/travel/plan-book/per-diem-rates): Utilized for determining daily allowances for lodging, meals, and incidental expenses for travel within the United States. The rates are specified for different locations and times of the year.
        - [GSA Airfare Database](https://www.gsa.gov/travel/plan-a-trip/transportation-airfare-rates-pov-rates-etc/airfare-rates-city-pair-program): Provides contract award airfare rates, which are typically available for government travelers and are used to estimate air travel costs between major destinations.


        ### Instructions
        - **Select your origin and destination:** Start by choosing your arrival city.
        - **Enter ONE-WAY airfare rate:** Research and enter **ONE-WAY** airfare rate in accordance with city's OBM policies and Uniform Guidance for Travel Costs.
        - **Enter travel dates and number of staff:** Specify the travel period and the number of people traveling.
        - **Calculate costs and generate budget justification:** After entering details, review the estimated expenses and a detailed budget justification.
        """)

    col1, col2 = st.columns(2)

    perdiem_df = load_perdiem_data()
    ground_transport_df = load_ground_transport_data()
    states = get_unique_states(perdiem_df)

    # Fetch and display available airports for the selected city

    selected_state = col1.selectbox('Select Travel State', states)
    cities = get_cities_by_state(perdiem_df, selected_state)
    selected_city = col1.selectbox('Select Travel City', cities)

    # Dates UI Components
    start_date = col2.date_input("Start Date", value=pd.to_datetime('today'))
    end_date = col2.date_input("End Date", value=pd.to_datetime(
        'today') + pd.DateOffset(days=1))

    num_staff = col2.number_input('Number of Staff', min_value=1, step=1)

    airfare_rate = col1.number_input(
        "Enter Airfare Manually (one way)", min_value=0.0, format="%.2f")

    if st.button('Calculate Travel Costs'):
        lodging_rate, mie_rate = retrieve_rates(
            selected_city, selected_state, start_date, end_date, perdiem_df)
        lodging_rate, lodging_error = verify_data_presence(
            lodging_rate, "lodging rate")
        mie_rate, mie_error = verify_data_presence(mie_rate, "M&IE rate")
        if lodging_error or mie_error:
            return

        lodging_rate, mie_rate, ground_transport_rate = get_travel_details(
            selected_city, selected_state, start_date, end_date, perdiem_df,
            ground_transport_df)

        costs = calculate_travel_costs(start_date, end_date, num_staff,
                                       airfare_rate, lodging_rate, mie_rate,
                                       ground_transport_rate)

        st.subheader(
            f"Total Travel Cost: ${costs['Total budgeted travel cost']}")

        st.subheader("Budget Justification Language for Grant")

        justification_text = create_budget_justification(selected_state,
                                                         selected_city,
                                                         start_date,
                                                         end_date, num_staff,
                                                         costs)

        st.text_area("Copy and paste this into your grant budget documentation:",
                     justification_text, height=175)
        st.write(
            "These are estimated travel costs based on the most current GSA data.")


if __name__ == "__main__":
    main()
