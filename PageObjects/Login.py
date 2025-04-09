from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

from Utilities.Utils import Utility


class LoginClass:

    #All xpaths are here for login page
    Icon_LogoLoading_Xpath = (By.XPATH, '//img[@class="logo"]')
    Icon_JaxLogo_Xpath = (By.XPATH, '//img[@alt="JAX Logo"]')
    Text_SignIn_Xpath = (By.XPATH, '//div[text()="Sign In"]')
    Text_NoAccount_Xpath = (By.XPATH, '//div[text()="Dont have an account?"]')
    Textfield_Email_Xpath = (By.XPATH, '//input[@id="email"]')
    Textfield_Password_Xpath = (By.XPATH, '//input[@id="password"]')
    Button_Signin_Xpath = (By.XPATH, '//span[text()=" Sign In "]')
    LinkText_ReqAccess_Xpath = (By.XPATH,'//div/a[text()="Request Access "]')
    LinkText_ForgotPassword_Xpath = (By.XPATH,'//div/a[text()="Forgot password? "]')
    CheckBox_RememberMe_Xpath = (By.XPATH,'//div/input[@type="checkbox"]')

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.ut = Utility

    def sendemail(self,email):
        obj = Utility.expwaitvisible(self,self.Textfield_Email_Xpath)
        obj.send_keys(email)

    def sendpswrd(self,paswrd):
        obj = Utility.expwaitvisible(self,self.Textfield_Password_Xpath)
        obj.send_keys(paswrd)

    def signinclick(self):
        obj = Utility.expwaitvisible(self,self.Button_Signin_Xpath)
        obj.click()

    def requestclick(self):
        obj = Utility.expwaitvisible(self, self.LinkText_ReqAccess_Xpath)
        obj.click()

    def forgotpwdclick(self):
        obj = Utility.expwaitvisible(self, self.LinkText_ForgotPassword_Xpath)
        obj.click()
