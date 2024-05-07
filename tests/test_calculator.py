
import pytest
from datetime import datetime

import sys
import os

try:
    from travel_calculator import (
        load_travel_data, get_city_group_rates, calculate_travel_costs,
        clean_currency, create_budget_justification)
except ImportError:
    # Assuming 'src' directory is one level up from the 'test' directory
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(script_dir)  # Get the parent directory
    # Build the path to the 'src' directory
    src_path = os.path.join(parent_dir, 'src')
    sys.path.append(src_path)  # Add 'src' directory to sys.path
    from travel_calculator import (
        load_travel_data, get_city_group_rates, calculate_travel_costs,
        clean_currency, create_budget_justification)


def test_load_travel_data():
    """Test data loading function for correctness and structure."""
    travel_data_df, states = load_travel_data()
    assert not travel_data_df.empty, "The DataFrame should not be empty."
    assert isinstance(states, list), "States should be returned as a list."
    assert 'Illinois' in states, "Illinois should be in the list of states."


def test_get_city_group_rates():
    """Test the function that retrieves rates based on city and state."""
    travel_data_df, _ = load_travel_data()
    lodging, transport, per_diem = get_city_group_rates(
        travel_data_df, 'Chicago', 'Illinois')
    assert lodging is not None, "Lodging rate should not be None."
    assert transport is not None, "Ground transport rate should not be None."
    assert per_diem is not None, "Per diem rate should not be None."


def test_clean_currency():
    """Ensure currency cleaning works correctly."""
    assert clean_currency(
        '$1,234.56') == 1234.56, "Currency should be converted to float without symbols."


def test_calculate_travel_costs():
    """Test travel cost calculations."""
    costs = calculate_travel_costs(
        datetime.strptime('2024-07-11', '%Y-%m-%d'),
        datetime.strptime('2024-07-14', '%Y-%m-%d'),
        3, 600, 250, 65, 55)
    assert costs['Total Budgeted Travel Cost'] > 0, "Total budgeted travel cost should be greater than zero."
    assert 'Airfare RT' in costs, "Airfare round trip cost should be calculated."


def test_create_budget_justification():
    """Verify that budget justification text is generated correctly."""
    costs = {
        'Airfare RT': 1200,
        'Hotel': 1500,
        'Per Diem': 195,
        'Ground Transport Total': 165,
        'Total Budgeted Travel Cost': 3060
    }
    justification = create_budget_justification(
        'Illinois', 'Chicago', datetime(2024, 7, 11), datetime(2024, 7, 14), 3, costs)
    assert "Travel to Chicago, Illinois" in justification, "Justification should include travel destination."
    assert "$3,060" in justification, "Justification should include formatted total cost."


if __name__ == "__main__":
    pytest.main()
