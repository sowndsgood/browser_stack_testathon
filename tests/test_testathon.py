import pytest
from selenium.webdriver.common.by import By
from utils.browserstack_config import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

# ------------------ TEST CASES ------------------

def test_homepage_title(driver):
    """TC01: Verify homepage title"""
    driver.get("https://testathon.live/")
    assert "Testathon Live" in driver.title

def test_homepage_buttons(driver):
    """TC02: Verify main homepage buttons are visible"""
    driver.get("https://testathon.live/")
    buttons = {
        "Offers": "//a[text()='Offers']",
        "Order": "//a[text()='Order']",
        "Favorites": "//a[text()='Favorites']",
        "Sign In": "//a[text()='Sign In']"
    }
    for name, xpath in buttons.items():
        element = driver.find_element(By.XPATH, xpath)
        assert element.is_displayed(), f"{name} button is not visible"

def test_sign_in(driver):
    """TC03: Sign In functionality test"""
    driver.get("https://testathon.live/signin")  # adjust if actual URL differs
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("TestPass123")
    driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

    # Example check: welcome text or dashboard title
    assert "Welcome" in driver.page_source or "Dashboard" in driver.title

def test_favorites_button(driver):
    """TC04: Favorites button navigation"""
    driver.get("https://testathon.live/")
    driver.find_element(By.XPATH, "//a[text()='Favorites']").click()
    assert "Favorites" in driver.title or "favorites" in driver.current_url

def test_order_button(driver):
    """TC05: Order button navigation"""
    driver.get("https://testathon.live/")
    driver.find_element(By.XPATH, "//a[text()='Order']").click()
    assert "Order" in driver.title or "order" in driver.current_url

def test_offers_button(driver):
    """TC06: Offers button navigation"""
    driver.get("https://testathon.live/")
    driver.find_element(By.XPATH, "//a[text()='Offers']").click()
    assert "Offers" in driver.title or "offers" in driver.current_url
