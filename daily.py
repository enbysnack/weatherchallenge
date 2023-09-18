import requests
from bs4 import BeautifulSoup

# Replace with the URL of the weather website you want to scrape
url = "https://weather.com/weather/today/l/1ba33abe593271cd38c3fde63f30049909290e371d58446b56b80a43ccd652f2"

# Send an HTTP GET request to fetch the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Locate and extract the weather data by inspecting the HTML structure
temperature = soup.find("span", class_="CurrentConditions--tempValue--MHmYY").text
conditions = soup.find("div", class_="CurrentConditions--phraseValue--mZC_p").text

print(f"Temperature: {temperature}")
print(f"Conditions: {conditions}")
