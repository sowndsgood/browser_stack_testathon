import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_offers_displayed(driver):
    """
    Test that offers are displayed on the homepage.
    Steps:
    - Navigate to the homepage.
    - Assert that the offers section is present.
    - Assert that at least one offer is visible.
    """
    driver.get("https://testathon.live/")
    wait = WebDriverWait(driver, 10)
    offers_section = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "offers")))
    offers = offers_section.find_elements(By.CLASS_NAME, "offer-item")
    assert offers, "No offers found on the homepage"