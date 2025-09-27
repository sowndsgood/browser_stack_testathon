from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME = "sowndaryas_WzuHaA"
ACCESS_KEY = "8QYpvFDqgwNPowj8dQru"

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub"

def test_title():
    options = webdriver.ChromeOptions()

    bstack_options = {
        "os": "Windows",
        "osVersion": "11",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "sessionName": "Testathon Home Page Test"
    }
    options.set_capability('bstack:options', bstack_options)

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    driver.get("https://testathon.live/")

    title = driver.title
    print("Title is:", title)
    assert "StackDemo" in title  

    driver.quit()