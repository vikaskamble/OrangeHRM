from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import unittest
from POMProjectDemo.Pages.LoginPage import LoginPage
from pyunitreport import HTMLTestRunner
from os.path import dirname, abspath
from POMProjectDemo.BaseClass.BaseClass import BaseClass


d = dirname(dirname(dirname(abspath(__file__))))
print("Test Path", d)
print(d+"\ReportTest")

class Login_Test(BaseClass):

    def test_Login_Valid(self):
        print("Start Login valid Test....")
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter__password("admin123")
        login.click_login()
        login.isLoginSuccess()
        login.logOutApplictaion()

if __name__ == "__main__":
    # unittest.main(testRunner=HTMLTestRunner(output="C://Users//vikas.k//PycharmProjects//UIAutomationFrameWork//ReportTest"))
    d = os.path.join(dirname(dirname(dirname(abspath(__file__)))), 'ReportTest')
    unittest.main(testRunner=HTMLTestRunner(output=d))

