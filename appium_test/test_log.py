import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Set up Chrome WebDriver
    Service_obj = Service(r"C:\Users\bons\Documents\Website_projects\mobil_automation\appium_test\CHROMEDRIVER.EXE")
    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_login_and_trip_list(driver):
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)

    # Perform login actions
