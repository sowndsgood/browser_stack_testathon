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

def test_orders_page_access(driver):
    """
    Test that the orders page can be accessed and displays orders.
    Steps:
    - Navigate to the orders page.
    - Assert that the orders list is present.
    """
    driver.get("https://testathon.live/orders")
    wait = WebDriverWait(driver, 10)
    orders_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "orders-list")))
    orders = orders_list.find_elements(By.CLASS_NAME, "order-item")
    assert orders is not None, "Orders list not found"