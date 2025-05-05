import pytest

from PageObjects.ForgotPassword import ForgotPassword
from PageObjects.Login import LoginClass
from PageObjects.RequestAccess import RequestAccess
from Utilities.readProperties import ReadConfig
from PageObjects.AccessRequested import AccessRequested
from Utilities.Utils import Utility

@pytest.mark.usefixtures("setup")
class TestCases:

    @pytest.fixture(autouse=True)

    def class_setup(self,setup):
        self.driver = setup
        self.url = ReadConfig.getURL()
        self.email = ReadConfig.emails()
        self.unremail = ReadConfig.unregisteredemail()
        self.name = ReadConfig.names()
        self.company = ReadConfig.companies()
        self.password = ReadConfig.passwords()
        self.lo = LoginClass(self.driver)
        self.ut = Utility(self.driver)
        self.ra = RequestAccess(self.driver)
        self.rac = AccessRequested(self.driver)
        self.fp = ForgotPassword(self.driver)

    @pytest.mark.happypath
    def test_logincustomer(self):
        self.driver.get(self.url)
        self.lo.sendemail(self.email)
        self.lo.sendpswrd(self.password)
        self.lo.signinclick()

    @pytest.mark.happypath
    def test_rqstaccesserror(self):
        self.driver.get(self.url)
        self.lo.requestclick()
        self.ra.inputemail(self.email)
        self.ra.inputname(self.name)
        self.ra.inputcompany(self.company)
        self.ra.submitclick()
        self.ra.emailexisttxt()

    @pytest.mark.happypath
    def test_rqstaccesssuccess(self):
        self.driver.get(self.url)
        self.lo.requestclick()
        self.ra.inputemail(self.unremail)
        self.ra.inputname(self.name)
        self.ra.inputcompany(self.company)
        self.ra.submitclick()
        self.rac.accesstext()

    @pytest.mark.happypatherror
    def test_frgtpswrd(self):
        self.driver.get(self.url)
        self.lo.forgotpwdclick()
        self.fp.enteremail(self.email)
        self.fp.sendbuttonclick()
        self.fp.errorunremail()

    @pytest.mark.regression
    def test_frgtpswrd(self):
        self.driver.get(self.url)
        self.lo.forgotpwdclick()
        self.fp.enteremail(self.email)
        self.fp.sendbuttonclick()
        self.fp.successfulmessage()