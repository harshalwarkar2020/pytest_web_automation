import time
from Log_Feature.LogRecord import LogData
from selenium.webdriver.common.by import By
from utilities.element_utils import ElementUtils


class TestHomePageVerification(ElementUtils, LogData):

    search_icon = (By.XPATH,  "//div[@class='header_account_area']/div[1]/a/i")

    def __init__(self, driver):
        self.driver = driver
        ElementUtils.__init__(self, driver)

    def Home_Page_Search_Functionality(self):
        log = self.getLogger()
        self.do_click(self.search_icon)
        log.info("User Clicked On Search Icon")
        time.sleep(10)
