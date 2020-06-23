import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select

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
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        time.sleep(3)
        block = Select(self.driver.find_element_by_name("myBlock"))
        block.select_by_index(1)
        time.sleep(3)
        cluster = Select(self.driver.find_element_by_name("myCluster"))
        cluster.select_by_index(1)
        time.sleep(5)
        self.driver.find_element_by_id(Data.homeicon).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.logout).click()


    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()