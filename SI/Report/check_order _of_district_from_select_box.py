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
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        driver =cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_school_infrastructure()
        time.sleep(5)
    def test_url(self):
        list =[]
        names = []
        dist = self.driver.find_elements_by_xpath("//select[@name='myDistrict']/options")
        for i in range(len(dist)):
            list =dist[i].text
            names =+list
        print(names)
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()