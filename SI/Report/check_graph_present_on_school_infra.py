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
        if "myChart" in self.driver.page_source:
            print("Scattor plot is present")
        else:
            self.assertNotIn("myChart",self.driver.page_source,msg="Does not exist")
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()