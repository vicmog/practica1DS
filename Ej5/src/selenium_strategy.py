from src.scrape_strategy import ScrapeStrategy  # Asegúrate de que esta importación sea correcta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

class SeleniumStrategy(ScrapeStrategy):
    def scrape(self, url):
        driver = webdriver.Firefox()
        driver.get(url)  # Usa la URL proporcionada en lugar de una fija
        elem = driver.find_element(By.XPATH, "//input[@class='Ta(end) Fw(600) Lh(14px)']")  # Reemplaza 'input-class' con la clase real del elemento
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()
        print(elem)
        return "Consulta hecha"
