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

def test_add_to_favorites(driver):
    """
    Test adding an item to favorites.
    Steps:
    - Navigate to the homepage.
    - Click the favorite button on an item.
    - Open the favorites page and assert the item is present.
    """
    driver.get("https://testathon.live/")
    wait = WebDriverWait(driver, 10)
    fav_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shelf-item__fav-btn")))
    fav_button.click()
    driver.get("https://testathon.live/favorites")
    favorites = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "favorite-item")))
    assert favorites, "No items found in favorites"