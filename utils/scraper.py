from scrapingbee import ScrapingBeeClient
from bs4 import BeautifulSoup

# Initialize the ScrapingBee client with your API key
client = ScrapingBeeClient(api_key='H0IGNQC267HB15FZ5XW7LT5P5O9UH7SAJUA08TVA8APCPU3KJR7LLXWFPCKJAEFI12D8REFWN9LM6VBF')

# The URL of the webpage from which you want to discover other URLs
start_url = 'https://vectorbt.pro/pvt_6739a1da/'

# Send a GET request to the ScrapingBee API
response = client.get(start_url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Extract the href attribute from each link and store
urls = [link.get('href') for link in links]

# Iterate over each URL
for url in urls:
    # Send a GET request to the ScrapingBee API
    response = client.get(url)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    # Find all the text within paragraph tags and write to a file
    with open("documentation.txt", "a") as f:
        for paragraph in soup.find_all('p'):
            f.write(paragraph.text)
            f.write('\n')

    # Find all the code snippets and write to a file
    with open("code_snippets.txt", "a") as f:
        for code in soup.find_all('code'):
            f.write(code.text)
            f.write('\n')
