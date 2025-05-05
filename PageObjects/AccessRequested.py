from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from Utilities.Utils import Utility

class AccessRequested:

    Text_AccessRequested_Xpath = (By.XPATH,'//div[text() = "Access Requested"]')
    Button_SignIn_Xpath = (By.XPATH,'//span[@class="text-black" and text()="Back to Sign in"]')

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.ut = Utility

    def accesstext(self):
        obj = self.ut.expwaitvisible(self,self.Text_AccessRequested_Xpath)
        if (obj.text == "Access Requested"):
            print("acctext")
        else:
            print("Failed to give access")

    def backtologin(self):
        self.ut.expwaitclickable(self,self.Button_SignIn_Xpath)
