import streamlit as st
import pandas as pd
from datetime import datetime
from travel_calculator import (get_per_diem_rates, load_airfare_data,
                               get_unique_states, get_cities_for_state,
                               get_yca_fare, load_perdiem_data,
                               get_airports_for_city, calculate_travel_costs,
                               create_budget_justification)


def main():
    st.title('Travel Cost Calculator')

    airfare_df = load_airfare_data()
    perdiem_df = load_perdiem_data()
    states = get_unique_states(airfare_df)

    default_origin_state = 'IL'
    default_origin_city = 'Chicago'
    default_origin_airport = 'ORD'

    origin_state = st.selectbox('Select Origin State', states, index=states.index(
        default_origin_state) if default_origin_state in states else 0)
    origin_cities = get_cities_for_state(airfare_df, origin_state)
    origin_city = st.selectbox('Select Origin City', origin_cities, index=origin_cities.index(
        default_origin_city) if default_origin_city in origin_cities else 0)

    # Fetch and display available airports for the selected city
    origin_airports = get_airports_for_city(
        airfare_df, origin_city, origin_state)
    selected_airport = st.selectbox('Select Origin Airport', origin_airports, index=origin_airports.index(
        default_origin_airport) if default_origin_airport in origin_airports else 0)

    selected_state = st.selectbox('Select Travel State', states)
    cities = get_cities_for_state(airfare_df, selected_state)
    selected_city = st.selectbox('Select Travel City', cities)

    # Dates UI Components
    start_date = st.date_input("Start Date", value=pd.to_datetime('today'))
    end_date = st.date_input("End Date", value=pd.to_datetime(
        'today') + pd.DateOffset(days=1))

    num_staff = st.number_input('Number of Staff', min_value=1, step=1)

    if st.button('Calculate Travel Costs'):
        airfare_rate = get_yca_fare(airfare_df, selected_airport,
                                    origin_city, origin_state, selected_city, selected_state)
        lodging_rate, mie_rate = get_per_diem_rates(
            perdiem_df, selected_city, start_date, end_date)
        st.write("Airfare: ", airfare_rate)
        st.write("Lodging: ", lodging_rate)
        st.write("MIE: ", mie_rate)

        costs = calculate_travel_costs(start_date, end_date, num_staff,
                                       airfare_rate, lodging_rate, mie_rate,
                                       baggage_fee=50,
                                       ground_transport_source=50,
                                       ground_transport_destination=30)
        st.write(costs)

        st.divider()

        st.write("Budget Justification Language for Grant")
        justification_text = create_budget_justification(origin_city,
                                                         selected_state,
                                                         selected_city,
                                                         start_date, end_date,
                                                         num_staff, costs)
        justification_tooltip = "Copy and paste this into your grant budget."
        st.text(justification_text, help=justification_tooltip)


if __name__ == "__main__":
    main()
