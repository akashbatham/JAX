from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.wait import WebDriverWait


class Utility:

    def __init__(self,setup):
        self.driver = setup

    def implisitwait(self):
        self.driver.implicitly_wait(5)

    def expwaitclickable(self,element):
        wait = WebDriverWait(self.driver,10)
        eleme = wait.until(es.element_to_be_clickable(element))
        eleme.click()

    def expwaitvisible(self,element):
        wait = WebDriverWait(self.driver,10)
        eleme = wait.until(es.visibility_of_element_located(element))
        return eleme

    def waitafterclick(self,element):
        wait = WebDriverWait(self.driver,5,2,ignored_exceptions=None)
        eleme = wait.until(es.presence_of_all_elements_located(element))
        return eleme