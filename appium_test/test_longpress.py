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
options.app_activity='com.android.dialer.main.impl.MainActivity'
options.app_package ='com.sh.smart.caller'
options.chromedriver_executable = r"C:\Users\bons\Documents\Website_projects\mobil_automation\appium_test\chromedriver.exe"  # Optional: Specify ChromeDriver path if needed
options.adb_exec_timeout = 60000
appium_service =AppiumService()
appium_service.start()

# Create Appium driver instance
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
element = driver.find_elements(By.ID,"com.sh.smart.caller:id/primary_action_view")
print(len(element))
actions = ActionChains(driver)
actions.click_and_hold(element[2]).perform()

element_click =driver.find_element(By.ID,"com.sh.smart.caller:id/copy_to_clipboard")

actions.click(element_click).perform()




appium_service.stop()