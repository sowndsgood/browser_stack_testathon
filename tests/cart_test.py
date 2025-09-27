import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BROWSERSTACK_USERNAME = "sowndaryas_WzuHaA"
BROWSERSTACK_ACCESS_KEY = "8QYpvFDqgwNPowj8dQru"

@pytest.fixture(scope="module")
def driver():
    bstack_options = {
        "os": "Windows",
        "osVersion": "11",
        "buildName": "Hackathon Build 1",
        "sessionName": "Testathon Cart Test",
        "debug": True
    }

    options = webdriver.ChromeOptions()
    options.set_capability("bstack:options", bstack_options)
    options.set_capability("browserName", "Chrome")
    options.set_capability("browserVersion", "117.0")

    driver = webdriver.Remote(
        command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub.browserstack.com/wd/hub",
        options=options
    )
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    driver.get("https://testathon.live/")
    wait = WebDriverWait(driver, 20)

    # Close any initial pop-ups
    try:
        popups = driver.find_elements(By.CLASS_NAME, "shelf-stopper")
        for popup in popups:
            try:
                popup.click()
            except:
                driver.execute_script("arguments[0].click();", popup)
    except:
        pass

    # Wait and click each buy button
    buy_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "shelf-item__buy-btn")))
    for button in buy_buttons:
        # scroll the button into view, center of the screen
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.5)
        try:
            wait.until(EC.element_to_be_clickable(button))
            button.click()
        except:
            # fallback JS click if normal click fails
            driver.execute_script("arguments[0].click();", button)
        time.sleep(0.5)

    # Open cart
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bag")))
    cart_icon.click()
    time.sleep(1)

    # Print cart items
    cart_items = driver.find_elements(By.CLASS_NAME, "shelf-item__details")
    for item in cart_items:
        title = item.find_element(By.CLASS_NAME, "title").text
        quantity = item.find_element(By.CLASS_NAME, "desc").text
        print(f"Cart Item: {title} | {quantity}")

    # Verify subtotal
    subtotal = driver.find_element(By.CLASS_NAME, "sub-price__val").text
    print("Subtotal:", subtotal)
    assert subtotal != ""

def test_cart_empty_on_load(driver):
    driver.get("https://testathon.live/")
    wait = WebDriverWait(driver, 10)
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bag")))
    cart_icon.click()
    time.sleep(1)
    cart_items = driver.find_elements(By.CLASS_NAME, "shelf-item__details")
    assert len(cart_items) == 0, "Cart should be empty on initial load"

def test_remove_item_from_cart(driver):
    driver.get("https://testathon.live/")
    wait = WebDriverWait(driver, 20)
    buy_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shelf-item__buy-btn")))
    buy_button.click()
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bag")))
    cart_icon.click()
    time.sleep(1)
    remove_buttons = driver.find_elements(By.CLASS_NAME, "shelf-item__del")
    assert remove_buttons, "Remove button not found in cart"
    remove_buttons[0].click()
    time.sleep(1)
    cart_items = driver.find_elements(By.CLASS_NAME, "shelf-item__details")
    assert len(cart_items) == 0, "Cart should be empty after removing item"

def test_cart_persists_after_page_refresh(driver):
    driver.get("https://testathon.live/")
    wait = WebDriverWait(driver, 20)
    buy_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shelf-item__buy-btn")))
    buy_button.click()
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bag")))
    cart_icon.click()
    time.sleep(1)
    cart_items_before = driver.find_elements(By.CLASS_NAME, "shelf-item__details")
    assert cart_items_before, "Cart should have items after adding"
    driver.refresh()
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bag")))
    cart_icon.click()
    time.sleep(1)
    cart_items_after = driver.find_elements(By.CLASS_NAME, "shelf-item__details")
    assert cart_items_after, "Cart items should persist after page refresh"
