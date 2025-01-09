import time
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

from scroll_util import Scroll_Util

# Define capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Emulator"
options.app_activity = 'flipboard.activities.LaunchActivity'
options.app_package = 'flipboard.app'
options.chromedriver_executable = r"C:\Users\bons\Documents\Website_projects\mobil_automation\appium_test\chromedriver.exe"
options.adb_exec_timeout = 60000

# Start Appium service
appium_service = AppiumService()
appium_service.start()

# Create Appium driver instance
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# Wait for the first launch button and click it
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "flipboard.app:id/first_launch_get_started_button"))
).click()

# Wait for the topic picker items and click them
topics = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.ID, "flipboard.app:id/topic_picker_topic_row_topic_tag"))
)

# Click the first three topics (ensure there are enough elements)
for i in range(min(3, len(topics))):
    topics[i].click()

# Wait for the continue button and click it
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "flipboard.app:id/topic_picker_continue_button"))
).click()

# Wait for the "Skip for Now" link and click it
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "flipboard.app:id/icon_button_text"))
).click()

time.sleep(2)
Scroll_Util.scrolldown(4,driver)
time.sleep(2)
Scroll_Util.scrollup(3,driver)


# Stop Appium service
appium_service.stop()
