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
    def test_url(self):
        driver= cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_crc_report()
        self.assertIn(" School infrastructure for: ",self.driver.page_source,msg="School infrastructure report not exist ")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()