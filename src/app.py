import streamlit as st
import pandas as pd
from travel_calculator import (
    get_cities_by_state, calculate_travel_costs, create_budget_justification,
    load_travel_data, get_city_group_rates)

st.set_page_config(page_title="Travel Cost Calculator App")


def main():
    st.title('Travel Cost Calculator')
    st.markdown("""
        This tool is designed to assist in planning and budgeting for official travel.
        It calculates estimated travel costs based on user-entered airfare data and categorized city rates for lodging, ground transport, and per diem allowances.
        For further information regarding travel policies, please consult [City of Chicago Travel Guidelines](https://www.chicago.gov/content/dam/city/depts/fin/supp_info/RiskManagement/Exhibit3_City_Travel_Guidelines.pdf) and the [Uniform Guidance for Travel Costs](https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-E/subject-group-ECFRed1f39f9b3d4e72/section-200.475).
        
        Created by **Nelson Lu**, Grants Research Specialist, City of Chicago's Department of Public Health.
        For more information, questions, or comments, please feel free to contact me [here](mailto:Nelson.Lu@cityofchicago.org).

        [LinkedIn](https://www.linkedin.com/in/nelson-lu-075a6b53/) | [GitHub](https://github.com/nelkalm)
                
        ### Instructions
        - **Select your origin and destination:** Start by choosing your arrival city.
        - **Enter ONE-WAY airfare rate:** Research and enter **ONE-WAY** airfare rate in accordance to city's OBM policies and Uniform Guidance for Travel Costs.
        - **Enter travel dates and number of staff:** Specify the travel period and the number of people traveling. The [GSA Airfare Database](https://www.gsa.gov/travel/plan-a-trip/transportation-airfare-rates-pov-rates-etc/airfare-rates-city-pair-program) provides contract award airfare rates, which is available for government travelers and is used to estimate air travel costs between major destinations.
        - **Calculate costs and generate budget justification:** After entering details, review the estimated expenses and a detailed budget justification.
        """)

    col1, col2 = st.columns(2)

    travel_df, states = load_travel_data()

    # Fetch and display data for the selected city
    selected_state = col1.selectbox('Select Travel State', states)
    cities = get_cities_by_state(travel_df, selected_state)
    selected_city = col1.selectbox('Select Travel City', cities)
    airfare_rate = col1.number_input(
        "Enter Airfare Rate (one way):", min_value=0.0, format="%.2f")

    # Dates UI Components
    start_date = col2.date_input("Start Date", value=pd.to_datetime('today'))
    end_date = col2.date_input("End Date", value=pd.to_datetime(
        'today') + pd.DateOffset(days=1))

    num_staff = col2.number_input('Number of Staff', min_value=1, step=1)

    if st.button('Calculate Travel Costs'):
        lodging_rate, ground_transport, per_diem = get_city_group_rates(
            travel_df, selected_city, selected_state)
        costs = calculate_travel_costs(start_date, end_date, num_staff,
                                       airfare_rate, lodging_rate, per_diem,
                                       ground_transport)

        budget_justification = create_budget_justification(selected_state,
                                                           selected_city,
                                                           start_date,
                                                           end_date,
                                                           num_staff, costs)

        st.subheader(
            f"Total Travel Cost: ${costs['Total budgeted travel cost']}")

        st.subheader("Budget Justification Language for Grant")

        st.text_area("Copy and paste this into your grant budget documentation:",
                     budget_justification, height=175)


if __name__ == "__main__":
    main()
