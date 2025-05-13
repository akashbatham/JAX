from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from Utilities.Utils import Utility
from time import sleep

class ForgotPassword:



    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.ut = Utility

    #Fields
    TextField_Email_Xpath = (By.XPATH,'//input[@id="email"]')
    Button_Send_Xpath = (By.XPATH,'//span[@class = "mdc-button__label"]/span[text()=" Send "]')

    #Warnings and Errors
    Text_UnRegEmail_Xpath = (By.XPATH,'//div/fuse-alert/div/div/div/following-sibling::div')
    Text_Success_Xpath = (By.XPATH,'//fuse-alert/div/div/div/following-sibling::div')

    def enteremail(self,email):
        obj = self.ut.expwaitvisible(self,self.TextField_Email_Xpath)
        obj.send_keys(email)

    def sendbuttonclick(self):
        self.ut.expwaitclickable(self,self.Button_Send_Xpath)

    def errorunremail(self):
        obj = self.ut.expwaitvisible(self,self.Text_UnRegEmail_Xpath)
        if (obj.text == "We couldn't process your request. Please verify information and try again."):
            print("Test Pass")
            assert True
        else:
            print("Failed")
            assert False

    def successfulmessage(self):
        obj = self.ut.expwaitvisible(self,self.Text_Success_Xpath)
        print("Success Message: ", obj.text)