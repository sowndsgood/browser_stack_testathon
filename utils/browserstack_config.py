import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def get_driver():
    USERNAME = os.getenv("BROWSERSTACK_USERNAME")
    ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

    if USERNAME and ACCESS_KEY:
        options = ChromeOptions()
        # Set BrowserStack capabilities
        options.set_capability("browserName", "Chrome")
        options.set_capability("browserVersion", "latest")
        options.set_capability("bstack:options", {
            "os": "Windows",
            "osVersion": "11",
            "projectName": "Testathon",
            "buildName": "Hackathon Build",
            "sessionName": "Homepage Tests",
        })

        driver = webdriver.Remote(
            command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
            options=options
        )
    else:
        # Local fallback
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return driver
