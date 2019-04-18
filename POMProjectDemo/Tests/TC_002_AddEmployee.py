from selenium import webdriver
from POMProjectDemo.BaseClass.BaseClass import BaseClass
from POMProjectDemo.Tests.Login import Login_Test
import os
import unittest
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from pyunitreport import HTMLTestRunner
from os.path import dirname, abspath
from POMProjectDemo.Pages.LoginPage import LoginPage
from POMProjectDemo.Pages.HomePage import HomePage

d = dirname(dirname(dirname(abspath(__file__))))


class AddEmpoyee(BaseClass):

    def test_add_Employee(self):
        print("Start Login valid Test....")
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter__password("admin123")
        login.click_login()
        login.isLoginSuccess()
        print("Login Test Executed Successfully...")
        homePage = HomePage(driver)
        homePage.clickOnPIM_Tab()
        time.sleep(4)





if __name__ == "__main__":
    # unittest.main(testRunner=HTMLTestRunner(output="C://Users//vikas.k//PycharmProjects//UIAutomationFrameWork//ReportTest"))
    d = os.path.join(dirname(dirname(dirname(abspath(__file__)))), 'ReportTest')
    unittest.main(testRunner=HTMLTestRunner(output=d))