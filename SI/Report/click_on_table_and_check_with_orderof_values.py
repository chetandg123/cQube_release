import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class School_infrastructure(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver =cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_school_infrastructure()
        time.sleep(5)
    def test_url(self):
        self.driver.find_element_by_xpath(Data.d_names).click()
        time.sleep(2)
        values = self.driver.find_elements_by_xpath("//th[1]")
        for i in values:
            print(i.get_attribute("aria-sort"))

        time.sleep(10)
        self.driver.find_element_by_xpath(Data.d_names).click()
        time.sleep(2)
        value = self.driver.find_elements_by_xpath("//th[1]")
        for i in value:
            print(i.get_attribute("aria-sort"))

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()