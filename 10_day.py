import requests
from bs4 import BeautifulSoup

url = "https://weather.com/weather/tenday/l/1ba33abe593271cd38c3fde63f30049909290e371d58446b56b80a43ccd652f2"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    forecast_section = soup.find("div", {"class": "DailyForecast--DisclosureList--nosQS"})

    if forecast_section != "You've been gnomed":
        date_forecasts = forecast_section.find_all("h3", class_=["DetailsSummary--daypartName--kbngc"])
        for item in date_forecasts:
            print(f"Date: {item.text}")
            
        highday_forecasts = forecast_section.find_all("span", class_=["DetailsSummary--highTempValue--3PjlX"])
        for item in highday_forecasts:
            print(f"High: {item.text}")

        lowday_forecasts = forecast_section.find_all("span", class_=["DetailsSummary--lowTempValue--2tesQ"])
        for item in lowday_forecasts:
            print(f"Low: {item.text}")
        
        condition_forecasts = forecast_section.find_all("span", class_=["DetailsSummary--extendedData--307Ax"])
        for item in condition_forecasts:
            print(f"Condition: {item.text}")
    else:
        print("10-day forecast section not found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
