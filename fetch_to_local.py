import os
import requests
import logging
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Retrieve Tiingo API key from .env file
tiingo_api_key = os.getenv('TIINGO_API_KEY')

def fetch_and_store_data(ticker, start_date, end_date, resample_freq='1min'):
    # Define the Tiingo API endpoint for historical forex data
    api_url = f'https://api.tiingo.com/tiingo/fx/{ticker}/prices'

    # Set up the headers and parameters for the API request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {tiingo_api_key}'
    }
    params = {
        'startDate': start_date,
        'endDate': end_date,
        'resampleFreq': resample_freq
    }

    # Make the API request
    response = requests.get(api_url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Process the response data
        data = response.json()

        # Ensure the 'data' directory exists
        if not os.path.exists('data'):
            os.makedirs('data')

        # Save data locally as a JSON file in the 'data' directory
        with open(f'data/{ticker}_{start_date}_{end_date}.json', 'w') as f:
            json.dump(data, f)

        logging.info(f"Successfully fetched and stored data locally for {ticker} from {start_date} to {end_date}")
    else:
        logging.error(f"Failed to fetch data for {ticker} from {start_date} to {end_date}: {response.status_code}")

# Call the function with your desired parameters
if __name__ == '__main__':
    # Calculate the date 30 days ago
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    fetch_and_store_data('AUDCHF', start_date, end_date)