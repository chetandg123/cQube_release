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
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_school_infrastructure_map()
        time.sleep(5)

    def test_url(self):
        school = self.driver.find_element_by_id(Data.sc_no_of_schools).text
        res = re.sub('\D', "", school)

        self.driver.find_element_by_id(Data.scm_block).click()
        time.sleep(4)
        bschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
        bres = re.sub('\D',"",bschool)
        self.assertEqual(int(res),int(bres),msg="mis match found in no of school in block level")
        time.sleep(5)

        self.driver.find_element_by_id(Data.scm_cluster).click()
        time.sleep(10)
        cschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
        time.sleep(2)
        cres = re.sub('\D', "", cschool)
        self.assertEqual(int(res), int(cres), msg="mis match found in no of school in cluster level")

        time.sleep(5)
        self.driver.find_element_by_id(Data.scm_school).click()
        time.sleep(20)
        sschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
        time.sleep(3)
        sres = re.sub('\D', "", sschool)
        self.assertEqual(int(res), int(sres), msg="mis match found in no of school in school level")

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()