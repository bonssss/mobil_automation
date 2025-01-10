import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.touch_actions import TouchActions


# Define capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platform_name = "Android"  # Specify the platform
options.device_name = "Android Emulator"  # Use "Android Emulator" or actual device name
# options.browser_name = "Chrome"  # Specify Chrome browser

# org.chromium.chrome.browser.webapps.SameTaskWebApkActivit
options.app_activity='org.chromium.chrome.browser.ChromeTabbedActivity'
options.app_package ='com.android.chrome'
options.chromedriver_executable = r"C:\Users\bons\Documents\Website_projects\mobil_automation\appium_test\chromedriver.exe"  # Optional: Specify ChromeDriver path if needed
options.adb_exec_timeout = 60000
appium_service =AppiumService()
appium_service.start()

# Create Appium driver instance
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
driver.get("https://google.com")
time.sleep(3)
# contexts = driver.contexts

# for context in contexts:
#     print(contexts)

# driver.switch_to.context('WEBVIEW_chrome')

# other to crear web view

webview =driver.contexts[1]
driver.switch_to.context(webview)

# driver.find_element(By.CLASS_NAME,"android.widget.EditText").send_keys('hello appium')


appium_service.stop()