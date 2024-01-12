from tiingo import TiingoClient
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load the .env file
load_dotenv()

# Get the Tiingo API key from environment variables
tiingo_api_key = os.getenv('TIINGO_API_KEY')

# Set up the Tiingo client
config = {'session': True, 'api_key': tiingo_api_key}
client = TiingoClient(config)

# Calculate the date 30 days ago
start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

# Fetch the data
df = client.get_dataframe('AUDCHF', frequency='1Min', startDate=start_date)

# Print the data
# print(df)