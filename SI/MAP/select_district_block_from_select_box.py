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
        driver.navigate_to_school_infrastructure()
        time.sleep(5)
    def test_dist_blocks(self):
        Districts = self.driver.find_elements_by_xpath(Data.sc_choosedist)
        blocks = self.driver.find_elements_by_xpath(Data.sc_chooseblock)
        for i in range(1,len(Districts)):
            Districts[i].click()
            time.sleep(4)
            for j in range(1,len(blocks)):
                blocks[j].click()
                time.sleep(4)
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()