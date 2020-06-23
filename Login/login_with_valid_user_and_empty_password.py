import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from get_dir import pwd


class login_test(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        self.driver.implicitly_wait(30)

    def test_url(self):
        self.driver.maximize_window()
        self.driver.get(Data.url)
        self.driver.find_element_by_id(Data.email).send_keys("xyz@gmail.com")
        time.sleep(2)
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        errormsg = self.driver.find_element_by_xpath(Data.fieldReq).text
        print(errormsg)
        self.assertEqual(errormsg,"This field is required" , msg="Failed")

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()