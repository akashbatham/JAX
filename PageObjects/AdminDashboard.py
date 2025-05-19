from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.Utils import Utility as ut


class AdminDash:

    def __init__(self,driver=WebDriver):
        self.driver = driver
        self.ut = ut

    #buttons
    Button_HideMenu_Xpath = (By.XPATH,'//*[name()="mat-icon" and @data-mat-icon-name="bars-3"]')
    Button_SignoutMenu_Xpath = (By.XPATH,'//span[@class="mdc-button__label"]')
    Button_SignoutMenuOption_Xpath = (By.XPATH,'////button[@role="menuitem"]')
    Button_Calendar_Xpath = (By.XPATH,'//mat-icon[@role="img" and @svgicon="heroicons_solid:calendar-days"]')
    Button_YearSelect_Xpath = (By.XPATH,'//button[@aria-describedby="mat-calendar-period-label-5"]/span[@class="mdc-button__label"]')
    Button_PrevMonth_Xpath = (By.XPATH,'//button[@aria-label="Previous month"]//*[name()="svg"]')
    Button_NextMonth_Xpath = (By.XPATH,'//button[@aria-label="Next month"]//*[name()="svg"]')
    Buttonlist_Dates_XPath = (By.XPATH,'//td[@role="gridcell"]/button/span[contains(@class,"mat-focus-indicator")]')
    Buttonlist_Years_Xpath = (By.XPATH,'//button[contains(@class,"mat-calendar-body-cell")]/span[contains(@class,"mat-focus-indicator")]')
    Dropdown_Companies_Xpath = (By.XPATH,'//div[@id="mat-select-value-0"]')
    List_Companies_Xpath = (By.XPATH,'//div[@role="listbox"]/mat-option/span')
    Check_Companies_Xpath = (By.XPATH,'//div[@role="listbox"]/mat-option/mat-pseudo-checkbox') #check the property state="checked"
    List_ComponentType_Xpath = (By.XPATH,'//div[text()="Component Type"]/following-sibling::*[name()="app-dashboard-donut-chart"]/div/div/div/div/span[contains(@class,"text")]')
    List_ComponentTypeCount_Xpath = (By.XPATH,'//div[text()="Component Type"]/following-sibling::*[name()="app-dashboard-donut-chart"]/div/div/div/span[not(contains(@class,"jax-dark-grey"))]') #You can use the webelement of component name and use that to find the count and percentage using parent-sibling bond
    Single_ComponentTypeCount_Xpath = (By.XPATH, 'webelement of single component and parent then sibling to find xpath')
    List_ComponentTypePercent_Xpath = (By.XPATH,'//div[text()="Component Type"]/following-sibling::*[name()="app-dashboard-donut-chart"]/div/div/div/span[contains(@class,"jax-dark-grey")]')
    List_PerformanceRatio_Xpath = (By.XPATH,'//div[text()="Performance Ratio"]/following-sibling::*[name()="app-dashboard-donut-chart"]/div/div/div/div/span[contains(@class,"text")]')
    List_PerformanceRatioCount_Xpath = (By.XPATH,'//div[text()="Performance Ratio"]/following-sibling::*[name()="app-dashboard-donut-chart"]/div/div/div/span[not(contains(@class,"jax-dark-grey"))]')
    List_PerformanceRatioPercent_Xpath = (By.XPATH,'//div[text()="Performance Ratio"]/following-sibling::*[name()="app-dashboard-donut-chart"]/div/div/div/span[contains(@class,"jax-dark-grey")]')

    #text
    Text_MonthInCalender_Xpath = (By.XPATH,'//tr[@class="ng-star-inserted"]/td[@role=not("gridcell")]')
    Text_CountCritical_Xpath = (By.XPATH,'//app-kpi-cards/div/div[contains(@class,"high-alert-secondary")]/div[contains(@class,"font-extrabold")]')
    Text_CriticalText_Xpath = (By.XPATH, '//app-kpi-cards/div/div[contains(@class,"high-alert-secondary")]/div[contains(@class,"font-medium")]')
    Text_CountMid_Xpath = (By.XPATH,'//app-kpi-cards/div/div[contains(@class,"medium-alert-secondary")]/div[contains(@class,"font-extrabold")]')
    Text_MidText_Xpath = (By.XPATH, '//app-kpi-cards/div/div[contains(@class,"medium-alert-secondary")]/div[contains(@class,"font-medium")]')
    Text_CountLow_Xpath = (By.XPATH,'//app-kpi-cards/div/div[contains(@class,"low-alert-secondary")]/div[contains(@class,"font-extrabold")]')
    Text_LowText_Xpath = (By.XPATH,'//app-kpi-cards/div/div[contains(@class,"low-alert-secondary")]/div[contains(@class,"font-medium")]')
    Text_AUsersCount_Xpath = (By.XPATH,'//div[text()="Active Users"]/preceding-sibling::div')
    Text_AUsersText_Xpath = (By.XPATH,'//div[text()="Active Users"]')
    Text_TestsCount_Xpath = (By.XPATH,'//div[text()="Total Tests"]/preceding-sibling::div')
    Text_TestsTex_Xpath = (By.XPATH, '//div[text()="Total Tests"]')

    #Graph
    Bar_GraphBar_Xpath = (By.XPATH,'//*[name()="g" and @class="apexcharts-inner apexcharts-graphical"]/*[name()="rect"]')
    Bar_GraphHigh_Xpath = (By.XPATH,'//*[name()="path" and @fill="var(--jax-high-alert)" and @class="apexcharts-bar-area "]')
    Bar_GraphMid_Xpath = (By.XPATH,'//*[name()="path" and @fill="var(--jax-medium-alert)" and @class="apexcharts-bar-area "]')
    Bar_GraphLow_Xpath = (By.XPATH,'//*[name()="path" and @fill="var(--jax-low-alert)" and @class="apexcharts-bar-area "]')
    Pie_Graph_Xpath = (By.XPATH,'//*[name()="g" and @class="apexcharts-pie"]')
    Pie_GraphLow_Xpath = (By.XPATH, '//*[name()="g" and @seriesName="AllxsxWell"]')
    Pie_GraphMid_Xpath = (By.XPATH, '//*[name()="g" and @seriesName="ActionxRequired"]')
    Pie_GraphCritical_Xpath = (By.XPATH, '//*[name()="g" and @seriesName="ImmediatexActionxRequired"]')
    Pie_TooltipLableLow_Xpath = (By.XPATH,'//div[@class="apexcharts-tooltip-series-group apexcharts-tooltip-series-group-0 apexcharts-active"]/div[@class="apexcharts-tooltip-text"]/div[@class="apexcharts-tooltip-y-group"]/span[@class="apexcharts-tooltip-text-y-label"]')
    Pie_TooltipValueLow_Xpath = (By.XPATH,'//div[@class="apexcharts-tooltip-series-group apexcharts-tooltip-series-group-0 apexcharts-active"]/div[@class="apexcharts-tooltip-text"]/div[@class="apexcharts-tooltip-y-group"]/span[@class="apexcharts-tooltip-text-y-value"]')
    Pie_TooltipLabelMid_Xpath = (By.XPATH,'//div[@class="apexcharts-tooltip-series-group apexcharts-tooltip-series-group-1 apexcharts-active"]/div[@class="apexcharts-tooltip-text"]/div[@class="apexcharts-tooltip-y-group"]/span[@class="apexcharts-tooltip-text-y-label"]')
    Pie_TooltipValueMid_Xpath = (By.XPATH,'//div[@class="apexcharts-tooltip-series-group apexcharts-tooltip-series-group-1 apexcharts-active"]/div[@class="apexcharts-tooltip-text"]/div[@class="apexcharts-tooltip-y-group"]/span[@class="apexcharts-tooltip-text-y-value"]')
    Pie_TooltipLabelCritical_Xpath = (By.XPATH,'//div[@class="apexcharts-tooltip-series-group apexcharts-tooltip-series-group-2 apexcharts-active"]/div[@class="apexcharts-tooltip-text"]/div[@class="apexcharts-tooltip-y-group"]/span[@class="apexcharts-tooltip-text-y-label"]')
    Pie_TooltipValueCritical_Xpath = (By.XPATH,'//div[@class="apexcharts-tooltip-series-group apexcharts-tooltip-series-group-2 apexcharts-active"]/div[@class="apexcharts-tooltip-text"]/div[@class="apexcharts-tooltip-y-group"]/span[@class="apexcharts-tooltip-text-y-value"]')

    def companyselect(self):
        ut.expwaitclickable(self,self.Dropdown_Companies_Xpath)

    def companylist(self):
        wait = WebDriverWait(self.driver, 30)
        expected_count = 2
        wait.until(lambda driver: len(self.driver.find_elements(By.XPATH, '//div[@role="listbox"]/mat-option/span')) >= expected_count)
        companiesoptions = self.driver.find_elements(By.XPATH, '//div[@role="listbox"]/mat-option/span')
        companylistcount = []
        for company in companiesoptions:
            company.click()
            company_name = company.text
            # self.countevry()
            criticalcount = ut.expwaitvisible(self, self.Text_CountCritical_Xpath).text
            midcount = ut.expwaitvisible(self, self.Text_CountMid_Xpath).text
            lowcount = ut.expwaitvisible(self, self.Text_CountLow_Xpath).text
            company_name = [criticalcount,midcount,lowcount]
            self.companyselect()
            companylistcount.append(company_name)
        print(companylistcount)


    def countevry(self):
        criticalcount = ut.expwaitvisible(self,self.Text_CountCritical_Xpath).text
        midcount = ut.expwaitvisible(self,self.Text_CountMid_Xpath).text
        lowcount = ut.expwaitvisible(self,self.Text_CountLow_Xpath).text
