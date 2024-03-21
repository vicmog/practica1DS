
from src.scrape_strategy import ScrapeStrategy
import requests

from bs4 import BeautifulSoup

import json
import os

class BeautifulSoupStrategy(ScrapeStrategy):
    def scrape(self, url):
        data = {}
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            open_value_td = soup.find('td', {'data-test': 'OPEN-value'})
            if open_value_td:
                data["open-value"] = open_value_td.text.strip()
            else:
                return 'Open Value not found'
            
            prev_clouse = soup.find('td',{'data-test':'PREV_CLOSE-value'})
            if prev_clouse:
                data["prev-clouse"] = prev_clouse.text.strip()
            else:
                return 'Prev Clouse not found'
            
            volume = soup.find('td',{'data-test':'TD_VOLUME-value'})
            if volume:
                data["volume"] = volume.text.strip()
            else:
                return 'Volume not found'
            
            market_cap = soup.find('td',{'data-test':'MARKET_CAP-value'})
            if market_cap:
                data["market-cap"]=market_cap.text.strip()
            else:
                return 'Market Cap not found'
            
            with open('data-beautiful.json', 'w') as file:
                json.dump(data,file)
                return "Json Creado"
        else:
            return f'Failed to retrieve the webpage, status code: {response.status_code}'