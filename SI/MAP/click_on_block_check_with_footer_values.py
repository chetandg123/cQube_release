import re
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
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        driver =cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_school_infrastructure_map()
        time.sleep(5)
    def test_url(self):
        self.driver.find_element_by_id(Data.scm_block).click()
        time.sleep(10)
        schools = self.driver.find_element_by_id(Data.sc_no_of_schools).text
        time.sleep(3)
        res =re.sub("\D","",schools)
        print(int(res))
        self.assertNotEqual(0,int(res),msg="wrong schools count")
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()