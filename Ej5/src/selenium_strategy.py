import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from src.scrape_strategy import ScrapeStrategy  # Import for exception handling


class SeleniumStrategy(ScrapeStrategy):
    def __init__(self):
        self.open_value_selector = "td[data-test='OPEN-value']"
        self.prev_close_selector = "td[data-test='PREV_CLOSE-value']"
        self.volume_selector = "td[data-test='TD_VOLUME-value']"
        self.market_cap_selector = "td[data-test='MARKET_CAP-value']"

    def scrape(self, url):
        driver = webdriver.Firefox()
        driver.get(url)
        data = {}

        # Aceptamos las cookies si es que hay, si no hay, se ignora
        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, ".btn.secondary.accept-all")
                )
            ).click()
        except TimeoutException:
            print("No se ha encontrado el botón de aceptar cookies")
            driver.quit()
            return "Error al intentar aceptar las cookies"

        # Esperamos a que el elemento que queremos esté presente y entonces lo cogemos. Si no está, se maneja la excepción
        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, self.open_value_selector)
                )
            )
            open_value = driver.find_element(By.CSS_SELECTOR, self.open_value_selector)
            data["open-value"] = open_value.text
            print(open_value.text)

            close_value = driver.find_element(By.CSS_SELECTOR, self.prev_close_selector)
            data["close-value"] = close_value.text
            print(close_value.text)

            volume = driver.find_element(By.CSS_SELECTOR, self.volume_selector)
            data["volume"] = volume.text
            print(volume.text)

            market_cap = driver.find_element(By.CSS_SELECTOR, self.market_cap_selector)
            data["market-cap"] = market_cap.text
            print(market_cap.text)
        except TimeoutException:
            print("No se ha encontrado un elemento en la página")
        finally:
            json.dump(data, open("data-selenium.json", "w"))
            driver.quit()
            return "Consulta hecha"
