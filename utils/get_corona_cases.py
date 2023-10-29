import requests
from bs4 import BeautifulSoup


"""
    Function that scrapes the latest global Coronavirus statistics from www.worldometers.info

    Returns:
        str: The total number of confirmed Coronavirus cases worldwide, 
        or "Failed to retrieve data" if the data couldn't be retrieved.
"""

def get_corona_cases():
    
    # URL of the website to scrape
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)
    
    if response.status_code == 200:
        
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        data_div = soup.find("div", {"class": "maincounter-number"})
        
        # Extract the latest global Coronavirus statistics
        total_cases = data_div.find("span").text.strip()
        return total_cases
    
    else:
        return "Failed to retrieve data"


