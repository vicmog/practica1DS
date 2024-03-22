from src.scrape_strategy import ScrapeStrategy
import requests

from bs4 import BeautifulSoup

import json
import os

OPEN_VALUE_SELECTOR = {"data-test": "OPEN-value"}
PREV_CLOSE_SELECTOR = {"data-test": "PREV_CLOSE-value"}
VOLUME_SELECTOR = {"data-test": "TD_VOLUME-value"}
MARKET_CAP_SELECTOR = {"data-test": "MARKET_CAP-value"}


class BeautifulSoupStrategy(ScrapeStrategy):
    def scrape(self, url):
        data = {}
        response = requests.get(url, headers={"Cache-Control": "no-cache"})
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            open_value_td = soup.find("td", OPEN_VALUE_SELECTOR)
            if open_value_td:
                data["open-value"] = open_value_td.text.strip()
                print(data["open-value"])
            else:
                return "Open Value not found"

            prev_clouse = soup.find("td", PREV_CLOSE_SELECTOR)
            if prev_clouse:
                data["prev-clouse"] = prev_clouse.text.strip()
                print(data["prev-clouse"])
            else:
                return "Prev Clouse not found"

            volume = soup.find("td", VOLUME_SELECTOR)
            if volume:
                data["volume"] = volume.text.strip()
                print(data["volume"])
            else:
                return "Volume not found"

            market_cap = soup.find("td", MARKET_CAP_SELECTOR)
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

