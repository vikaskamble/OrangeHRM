import unittest
from selenium import webdriver
from POMProjectDemo.BaseClass.GetConfigData import GetConfig


class BaseClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = GetConfig().getConfig("BROWSER","browser")
        # cls.launchBrowser(cls,"chrome")
        cls.launchBrowser(cls, browser)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        url = GetConfig().getConfig("URL", "url")
        # cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.get(url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        # print("Test Completed.")

    def launchBrowser(self, browser):
        try:
            if browser == "chrome":
                _DriverPath = "C:/Users/vikas.k/PycharmProjects/UIAutomationFrameWork/DRIVER/chromedriver.exe"
                self.driver=webdriver.Chrome(_DriverPath)
            elif browser == "firefor":
                print("launch Firefox Browser")
            elif browser == "ie":
                print("launch Firefox Browser")
            else:
                print("Selected browser is not relevant.")
        except:
            print("An error occur..")
