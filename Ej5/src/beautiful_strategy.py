from src.scrape_strategy import ScrapeStrategy
import requests

from bs4 import BeautifulSoup

import json


class BeautifulSoupStrategy(ScrapeStrategy):
    def __init__(self):
        self.open_value_selector = {"data-test": "OPEN-value"}
        self.prev_close_selector = {"data-test": "PREV_CLOSE-value"}
        self.volume_selector = {"data-test": "TD_VOLUME-value"}
        self.market_cap_selector = {"data-test": "MARKET_CAP-value"}

    def scrape(self, url):
        data = {}
        response = requests.get(url, headers={"Cache-Control": "no-cache"})
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            open_value_td = soup.find("td", self.open_value_selector)
            if open_value_td:
                data["open-value"] = open_value_td.text.strip()
                print(data["open-value"])
            else:
                return "Open Value not found"

            prev_clouse = soup.find("td", self.prev_close_selector)
            if prev_clouse:
                data["prev-clouse"] = prev_clouse.text.strip()
                print(data["prev-clouse"])
            else:
                return "Prev Clouse not found"

            volume = soup.find("td", self.volume_selector)
            if volume:
                data["volume"] = volume.text.strip()
                print(data["volume"])
            else:
                return "Volume not found"

            market_cap = soup.find("td", self.market_cap_selector)
            if market_cap:
                data["market-cap"] = market_cap.text.strip()
                print(data["market-cap"])
            else:
                return "Market Cap not found"

            with open("data-beautiful.json", "w") as file:
                json.dump(data, file)
                return "Json Creado"
        else:
            return (
                f"Failed to retrieve the webpage, status code: {response.status_code}"
            )

