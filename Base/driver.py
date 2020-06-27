"""声明driver"""
from appium import webdriver


class Driver:
    driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            desired_caps = {
                'platformName': 'android',
                'platformVersion': '5.1',
                'deviceName': 'huawei',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            return cls.driver
        else:
            return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
