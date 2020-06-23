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
        time.sleep(5)
    def test_url(self):
        self.driver.find_element_by_id(Data.Dashboard).click()
        text = self.driver.find_element_by_xpath(Data.header).text
        self.assertEqual("cQube - Dashboard",text,msg="Dashboard is not exists!")
        self.driver.find_element_by_xpath(Data.School_infra).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.Report).click()
        time.sleep(3)
        if "school-infrastructure" in self.driver.current_url:
            print("Shool infrastructure report page")
        else:
            print("School infrastructure report page is not exist")
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()