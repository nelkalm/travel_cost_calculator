# Travel Cost Calculator

## Overview

The Travel Cost Calculator is designed to assist users in planning and budgeting for official travel. It estimates the travel costs based on General Services Administration (GSA) per diem rates and airfare data for FY24. This tool aims to provide a seamless interface to calculate estimated travel costs, generate detailed budget justifications, and handle different scenarios based on available GSA data.

## Features

- **Travel State and City Selection**: Users can select their origin and destination states and cities.
- **Date Selection**: Users specify the start and end dates of their travel.
- **Number of Travelers**: Users input the number of staff traveling.
- **Cost Calculation**: Based on input details, the tool calculates airfare, lodging, per diem, and transportation costs.
- **Budget Justification**: Generates a detailed budget justification suitable for grant applications and budget planning.

## Data Sources

- **GSA Per Diem Rates**: Provides daily allowances for lodging, meals, and incidental expenses for travel within the United States.
- **GSA Airfare Database**: Includes contract award airfare rates, which are used to estimate air travel costs between major destinations.

## Usage Instructions

1. **Select your origin and destination**: Start by choosing your departure and arrival cities.
2. **Enter travel dates and number of staff**: Specify the travel period and the number of people traveling.
3. **Calculate costs and generate budget justification**: After entering details, review the estimated expenses and a detailed budget justification.

## Error Handling

- **No Route Available**: If no direct airfare route is available, the user is prompted to manually enter airfare or select the nearest major city.
- **Data Integrity**: The application checks for missing or incomplete data entries and provides feedback to ensure accurate calculations.

## Installation

To set up the Travel Cost Calculator, clone the repository and install the required dependencies:

```bash
git clone https://github.com/nelkalm/travel_cost_calculator.git
cd travel_cost_calculator
pip install -r requirements.txt
```

This markdown file gives an outline of what the project is about, how to use it, and additional details like data sources and error handling. You can adjust the content to better fit your specific project or add more sections as necessary.
