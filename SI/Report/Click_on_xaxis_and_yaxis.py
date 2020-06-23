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
    def test_plots(self):
        print("")
        # x_axis = self.driver.find_element_by_id(Data.x)
        # y_axis = self.driver.find_element_by_id(Data.y)
        # time.sleep(3)
        # for x in range(1, len(x_axis.options)):
        #     time.sleep(2)
        #     x_axis.select_by_index(x)
        #     time.sleep(2)
        #     for y in range(1, len(y_axis.options)):
        #         time.sleep(2)
        #         y_axis.select_by_index(y)
        #         time.sleep(2)
        # select = Select(self.driver.find_element_by_name('xAxis'))
        # #
        # for index in range(len(select.options)):
        #     select = Select(self.driver.find_element_by_name('xAxis'))
        #     time.sleep(2)
        #     select.select_by_index(index)
        #     time.sleep(3)
        #     for index in range(len(select.options)):
        #         select = Select(self.driver.find_element_by_name('yAxis'))
        #         time.sleep(2)
        #         select.select_by_index(index)
        #         time.sleep(3)


    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()