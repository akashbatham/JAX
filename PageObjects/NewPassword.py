from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from Utilities.Utils import Utility

class NewPassword:

    TextField_NewPassword_Xpath = (By.XPATH,'//input[@id="password"]')
    TextField_ConfirmPassword_Xpath = (By.XPATH,'id="password-confirm"')
    Button_SignIn_Xpath = (By.XPATH,'//span[@class="mdc-button__label"]')

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.ut = Utility

    def enternewpassword(self,newpassword):
        obj = self.ut.expwaitvisible(self,self.TextField_NewPassword_Xpath)
        obj.send_keys(newpassword)

    def enterconfirmpassword(self,confirmpassword):
        obj = self.ut.expwaitvisible(self,self.TextField_ConfirmPassword_Xpath)
        obj.send_keys(confirmpassword)

    def clickSignIn(self):
        self.ut.expwaitclickable(self.Button_SignIn_Xpath)