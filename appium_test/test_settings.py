import time

from selenium.webdriver.support import  expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
# from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

# Define capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platform_name = "Android"  # Specify the platform
options.device_name = "Android Emulator"  # Use "Android Emulator" or actual device name
# options.app = r"C:\Users\bons\Documents\Website_projects\mobil_automation\appium_test\app\amazon.apk"
# options.browser_name = "Chrome"  # Specify Chrome browser
options.app_activity='com.transsion.settings.homepage.TranSettingsHomepageActivity'
options.app_package ='com.android.settings'
options.chromedriver_executable = r"C:\Users\bons\Documents\Website_projects\mobil_automation\appium_test\chromedriver.exe"  # Optional: Specify ChromeDriver path if needed
options.adb_exec_timeout = 60000
appium_service =AppiumService()
appium_service.start()

# Create Appium driver instance
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# driver.find_element(By.android_uiautomator('new UiSelector().text("My Phone")')).click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("My Phone ")').click()
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Device name")'))
)
element.click()
driver.find_element(By.ID,"com.android.settings:id/oet_edit_text").send_keys("Bons")
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("no_one")').send_keys("Bons")
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("OK")').click()




# driver.find_element(By.ID,"com.android.settings:id/tran_id_content").click()

time.sleep(4)

appium_service.stop()
