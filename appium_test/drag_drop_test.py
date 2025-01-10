import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'com.mobeta.android.demodslv'
desired_caps['appActivity'] = '.Launcher'

# Set up the driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

# Click on the first element
driver.find_elements_by_id('com.mobeta.android.demodslv:id/activity_title')[0].click()

# Find the draggable elements
elements = driver.find_elements_by_id('com.mobeta.android.demodslv:id/drag_handle')

# Create TouchAction object
action = TouchAction(driver)

# Perform the drag-and-drop action
action.press(elements[0]).wait(3000).move_to(elements[3]).release().perform()

# Wait for a moment before quitting
time.sleep(2)
driver.quit()
