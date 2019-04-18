from selenium import webdriver
from POMProjectDemo.Locators.HomePageLocators import HomePageLocator


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.PIM_Tab_id = HomePageLocator.PIM_Tab_id
        self.PIM_SUB_Tab_AddEmployee_id = HomePageLocator().PIM_SUB_Tab_AddEmployee_id

    def clickOnPIM_Tab(self):
        try:
            self.driver.find_element_by_id(self.PIM_Tab_id).click()
            self.driver.find_element_by_id(self.PIM_SUB_Tab_AddEmployee_id).click()
        except:
            print('An error occurred.')


