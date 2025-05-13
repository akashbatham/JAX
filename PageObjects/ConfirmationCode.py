from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from Utilities.Utils import Utility


class ConfirmCode:

    #Need the code from Forgot Mailosauras so need to create a method to get the code

    def __init__(self,driver = WebDriver):
        self.driver = driver
        self.ut = Utility

    Textfield_Code_ID = (By.ID,'Code')
    Textfield_Password_ID = (By.ID, 'password')
    Textfield_ConfirmPass_ID = (By.ID,'ConfirmPassword')
    Button_Submit_Xpath = (By.XPATH,'//span[@class="mdc-button__label"]')

    def Codefield(self,key):
        obj = self.ut.expwaitvisible(self.Textfield_Code_ID)
        obj.send_keys(key)

    def Password(self,firstpass):
        obj = self.ut.expwaitvisible(self.Textfield_Password_ID)
        obj.send_keys(firstpass)

    def ConfirmPassword(self,confirmpass):
        obj = self.ut.expwaitvisible(self.Textfield_ConfirmPass_ID)
        obj.send_keys(confirmpass)

    def Submitbutton(self):
        self.ut.expwaitclickable(self.Button_Submit_Xpath)