# Travel Cost Calculator

## Introduction

The Travel Cost Calculator is a web-based application designed to help users estimate the costs associated with official travel. Utilizing the General Services Administration (GSA) per diem rates and airfare data for FY24, this tool simplifies the process of planning and budgeting for travel expenses, ensuring compliance with government travel policies.

## Key Features

- **State and City Selection**: Choose both origin and destination from a comprehensive list of states and cities.
- **Travel Dates and Number of Travelers**: Input the duration of the trip and how many people are traveling.
- **Cost Calculation**: Automatically calculates expenses for airfare, lodging, per diem, and transportation.
- **Budget Justification**: Generates detailed budget justifications suitable for expense reporting and grant applications.

## Built With

- Python - Primary programming language
- Streamlit - Framework used to create the web application
- Pandas - Used for data manipulation and analysis

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/nelkalm/travel_cost_calculator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd travel_cost_calculator
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

Execute the following command in the project directory:
```sh
streamlit run app.py
```
This will start the Streamlit web server and the application will be accessible via your web browser at `localhost:8501`.

## Usage

After launching the application, use the interface to:
- Select the origin and destination locations.
- Choose the travel dates.
- Enter the number of staff traveling.
- Click on 'Calculate Travel Costs' to view the estimated expenses.

## Contributing

Contributions to enhance the functionality or efficiency of the Travel Cost Calculator are welcome. Please fork the repository and create a pull request with your features or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- GSA Per Diem Rates
- GSA Airfare Database
- Streamlit Documentation

Feel free to explore the app and use it to plan your travel more effectively!
