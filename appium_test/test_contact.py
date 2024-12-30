import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By

# Define capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platform_name = "Android"  # Specify the platform
options.device_name = "Android Emulator"  # Use "Android Emulator" or actual device name
# options.browser_name = "Chrome"  # Specify Chrome browser
options.app_activity='.Calculator'
options.app_package ='com.transsion.calculator'
options.chromedriver_executable = r"C:\Users\bons\Documents\Website_projects\mobil_automation\appium_test\chromedriver.exe"  # Optional: Specify ChromeDriver path if needed
options.adb_exec_timeout = 60000
appium_service =AppiumService()
appium_service.start()

# Create Appium driver instance
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

driver.find_element(By.ID,"com.transsion.calculator:id/digit_5").click()
driver.find_element(By.ID,"com.transsion.calculator:id/op_add").click()
driver.find_element(By.ID,"com.transsion.calculator:id/digit_7").click()

# driver.find_element(By.ID,"")


time
print('contact start')
appium_service.stop()

