import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class test_logout(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        self.driver.implicitly_wait(15)
        self.driver.get(Data.url)
        self.driver.find_element_by_id(Data.email).send_keys(Data.username)
        self.driver.find_element_by_id(Data.passwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)

    def test_url(self):

        self.driver.find_element_by_id(Data.Logout).click()
        time.sleep(5)
        if "login" in self.driver.current_url:
            print("login page visible")
        else:
            print("login page not visible")
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()