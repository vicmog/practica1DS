
import src as ScrapeStrategy
import requests

from bs4 import BeautifulSoup

class BeautifulSoupStrategy(ScrapeStrategy):
    def scrape(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            open_value_td = soup.find('td', {'data-test': 'OPEN-value'})
            if open_value_td:
                return open_value_td.text.strip()
            else:
                return 'Open Value not found'
        else:
            return f'Failed to retrieve the webpage, status code: {response.status_code}'