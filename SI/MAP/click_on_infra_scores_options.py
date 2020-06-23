import time
import unittest

from selenium import webdriver
from selenium.common import exceptions
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
        driver.navigate_to_school_infrastructure_map()
        time.sleep(5)
    def test_infrascores(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        for x in range(1, len(chooseinfra.options)):
            time.sleep(2)
            chooseinfra.select_by_index(x)
            time.sleep(3)



    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()