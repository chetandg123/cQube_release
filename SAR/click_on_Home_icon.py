import time

from Data.parameters import Data


class Home():
    def __init__(self, driver):
        self.driver = driver

    def click_HomeButton(self):
            self.driver.find_element_by_id(Data.homeicon).click()
            time.sleep(3)
            return self.driver.page_source

    def click_on_blocks_click_on_home_icon(self):
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        time.sleep(5)




