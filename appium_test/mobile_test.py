import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By

# Define capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platform_name = "Android"  # Specify the platform
options.device_name = "Android Emulator"  # Use "Android Emulator" or actual device name
options.browser_name = "Chrome"  # Specify Chrome browser
options.chromedriver_executable = r"C:\Users\bons\Documents\Website_projects\mobil_automation\appium_test\chromedriver.exe"  # Optional: Specify ChromeDriver path if needed
options.adb_exec_timeout = 60000
appium_service =AppiumService()
appium_service.start()

# Create Appium driver instance
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

try:
    # Navigate to a website
    driver.get("https://nextdev.netryde.com/")

    # Print the title of the webpage
    print("Page title is:", driver.title)
    print("hello mobile automation")
    # time.sleep(5)
    driver.find_element(By.XPATH, "(//img[@alt='Light Mode'])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//img[@alt='Dark Mode'])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//img[@alt='Light Mode'])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//img[@alt='Dark Mode'])[1]").click()

    # Wait for 5 seconds
    time.sleep(5)

finally:
    # Quit the driver
    driver.quit()
appium_service.stop()
