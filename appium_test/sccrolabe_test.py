import time

from selenium.webdriver.support import  expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By


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

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    '.scrollIntoView( new UiSelector().textContains("System ").instance(0));').click()

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
#     'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
#     '.scrollIntoView(new UiSelector().textContains("System ").instance(0));').click()

time.sleep(4)

appium_service.stop()