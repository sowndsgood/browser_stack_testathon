from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME = "sowndaryas_WzuHaA"
ACCESS_KEY = "8QYpvFDqgwNPowj8dQru"
BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub"

def test_print_ids():
    options = webdriver.ChromeOptions()
    bstack_options = {
        "os": "Windows",
        "osVersion": "11",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "sessionName": "Print Element IDs"
    }
    options.set_capability('bstack:options', bstack_options)

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    driver.get("https://testathon.live/")

    # List of element IDs
    element_ids = ["offers", "favorites", "orders"]
    
    for eid in element_ids:
        element = driver.find_element(By.ID, eid)
        print(f"Element ID: {eid}, Text: {element.text}")

    driver.quit()
