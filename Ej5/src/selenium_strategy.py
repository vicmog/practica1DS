from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException  # Import for exception handling

OPEN_VALUE_SELECTOR = "td[data-test='OPEN-value']"
CLOSE_VALUE_SELECTOR = "td[data-test='PREV_CLOSE-value']"
VOLUME_SELECTOR = "td[data-test='TD_VOLUME-value']"
MARKET_CAP_SELECTOR = "td[data-test='MARKET_CAP-value']"


class SeleniumStrategy:
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
            print("Error: Could not find cookie acceptance button.")
            driver.quit()
            return "Error: Accepting cookies failed."

        # Esperamos a que el elemento que queremos esté presente y entonces lo cogemos. Si no está, se maneja la excepción
        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, "td[data-test='OPEN-value']")
                )
            )
            open_value = driver.find_element(By.CSS_SELECTOR, OPEN_VALUE_SELECTOR)
            data["open-value"] = open_value.text
            print(open_value.text)

            close_value = driver.find_element(By.CSS_SELECTOR, CLOSE_VALUE_SELECTOR)
            data["close-value"] = close_value.text
            print(close_value.text)

            volume = driver.find_element(By.CSS_SELECTOR, VOLUME_SELECTOR)
            data["volume"] = volume.text
            print(volume.text)

            market_cap = driver.find_element(By.CSS_SELECTOR, MARKET_CAP_SELECTOR)
            data["market-cap"] = market_cap.text
            print(market_cap.text)
        except TimeoutException:
            print("Error: Could not find target element.")
        finally:
            driver.quit()
            return "Consulta hecha"  # Adjust return message if needed
