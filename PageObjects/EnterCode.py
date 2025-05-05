from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from Utilities.Utils import Utility
from Utilities.MailosaursUsingAPI import Mailosaurs


class EnterCodes:

    TextField_Code_Xpath = (By.XPATH,'//input[@id="Code"]')
    TextField_NewPassword_Xpath = (By.XPATH, '//input[@id="password"]')
    TextField_ConfirmPassword_Xpath = (By.XPATH, '//input[@id="ConfirmPassword"]')

    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.ut = Utility
        self.co = Mailosaurs

    def inputcode(self,code):
        obj = self.ut.expwaitvisible(self.TextField_Code_Xpath)
        obj.send_keys(code)

    def inputnewpassword(self,password):
        obj = self.ut.expwaitvisible(self.TextField_NewPassword_Xpath)
        obj.send_keys(password)

