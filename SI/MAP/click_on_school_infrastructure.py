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
        # p = pwd()
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # self.driver = webdriver.Chrome(p.get_driver_path(), chrome_options=options)
        driver =cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        time.sleep(5)
    def test_url(self):
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.School_infra).click()
        time.sleep(2)
        schoolinfra=self.driver.find_element_by_xpath(Data.School_infra).text
        self.assertEqual("School Infrastructure",schoolinfra,msg="School infra is not exist!")

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()