import unittest

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData
class CqubeLogin(unittest.TestCase):

    def setUp(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.data.get_domain_name())

    def test_search(self):
        self.driver.find_element_by_xpath(Data.email).send_keys(self.data.get_username())
        self.driver.find_element_by_xpath(Data.pwd).send_keys(self.data.get_password())
        self.driver.find_element_by_xpath(Data.loginbtn).click()

    def tearDown(self):
        self.driver.close()
