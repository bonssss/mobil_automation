import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Define capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platform_name = "Android"  # Specify the platform
options.device_name = "Android Emulator"  # Use "Android Emulator" or actual device name
options.browser_name = "Chrome"  # Specify Chrome browser
options.chromedriver_executable = r"C:\Users\bons\Documents\Website_projects\mobil_automation\appium_test\chromedriver.exe"  # Optional: Specify ChromeDriver path if needed

# Create Appium driver instance
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

try:
    # Navigate to a website
    driver.get("https://www.google.com")

    # Print the title of the webpage
    print("Page title is:", driver.title)

    # Wait for 5 seconds
    time.sleep(5)

finally:
    # Quit the driver
    driver.quit()
