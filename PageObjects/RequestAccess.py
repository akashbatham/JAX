from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from Utilities.Utils import Utility


class RequestAccess:

    #Field Xpaths
    Textfield_Email_Xpath = (By.XPATH, '//input[@id="email"]')
    Textfield_Name_Xpath = (By.XPATH, '//input[@id="name"]')
    Textfield_Company_Xpath = (By.XPATH, '//input[@id="company"]')
    Button_RqstAcs_Xpath = (By.XPATH, '//button/span/span[text()="Request Access"]')
    TextLink_SignIn_Xpath = (By.XPATH, '//div/a[text()="sign in"]')

    #Text Warning Xpaths
    TextWar_AlreadyExistEmail_Xpath = (By.XPATH, '//div/div[text()=" Access Request with this email already exists. "]')
    TextWar_RequiredEmail_Xpath = (By.XPATH,'//div/mat-error[text()="Email address is required"]')
    TextWar_InvalidEmail_Xpath = (By.XPATH, '//div/mat-error[text()="Please enter a valid email address"]')
    TextWar_RequiredName_Xpath = (By.XPATH, '//div/mat-error[text()="Name is required"]')
    TextWar_InvalidName_Xpath = (By.XPATH, '//div/mat-error[text()="Name can only contain letters, numbers and spaces"]')
    TextWar_RequiredCompany_Xpath = (By.XPATH, '//div/mat-error[text()="Company is required"]')
    TextWar_InvalidCompany_Xpath = (By.XPATH, '//div/mat-error[text()="Company can only contain letters, numbers and spaces"]')

    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.ut = Utility

    def inputemail(self,email):
        obj = self.ut.expwaitvisible(self,self.Textfield_Email_Xpath)
        obj.send_keys(email)

    def inputname(self,name):
        obj = self.ut.expwaitvisible(self,self.Textfield_Name_Xpath)
        obj.send_keys(name)

    def inputcompany(self,company):
        obj = self.ut.expwaitvisible(self,self.Textfield_Company_Xpath)
        obj.send_keys(company)

    def submitclick(self):
        self.ut.expwaitclickable(self,self.Button_RqstAcs_Xpath)

    def emailexisttxt(self):
        obj = self.ut.expwaitvisible(self,self.TextWar_AlreadyExistEmail_Xpath)
        if (obj.text == "Access Request with this email already exists."):
            print(obj.text)
            assert True
        else:
            print("Email was added successfully")
            assert False

