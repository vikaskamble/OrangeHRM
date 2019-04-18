import time
from selenium.common.exceptions import NoSuchElementException
from POMProjectDemo.Locators.Locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.signinBtn_id = Locators.signinBtn_id
        self.homePageWelcomeLink = Locators.homePageWelcomeLink
        self.logOutLink = Locators.logOutLink

    def enter_username(self, uername):
        print("Enter User Name")
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(uername)

    def enter__password(self, passsword):
        print("Enter Password")
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(passsword)
        time.sleep(2)

    def click_login(self):
        print("Click on Login button.")
        self.driver.find_element_by_id(self.signinBtn_id).click()

    def isLoginSuccess(self):
        print("Check is login success.")
        try:
            self.driver.find_element_by_id(self.homePageWelcomeLink)
            time.sleep(2)
        except NoSuchElementException:
            return False
        return True

    def logOutApplictaion(self):
        print("Log Out Apllication.")
        self.driver.find_element_by_id(self.homePageWelcomeLink).click()
        self.driver.find_element_by_link_text(self.logOutLink).click()





