from appium.webdriver.common.appiumby import AppiumBy


class Scroll_Util():


    @staticmethod
    def howmanytimetoscroll(text,driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    f'.scrollIntoView( new UiSelector().textContains("{text}").instance(0));')



    @staticmethod
    def scrollup(howmanytime,driver):
        for i in range(1,howmanytime + 1):
            driver.swipe(500, 800, 500, 1000, 1000)



    def scrolldown(howmanytime,driver):
        for i in range(1,howmanytime + 1):
            driver.swipe(500, 800, 500, 300, 1000)

    def scrollright(howmanytime,driver):
        for i in range(1,howmanytime + 1):
            driver.swipe(200, 600, 700, 600, 1000)

    def scrollleft(howmanytime,driver):
        for i in range(1,howmanytime + 1):
            driver.swipe(700, 600, 200, 600, 1000)

