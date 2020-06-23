import time
import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class SchoolInfraReport(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_school_infrastructure()
        time.sleep(5)
    def test_data(self):
        print("")
    # def test_table_data(self):
    #     select_district = Select(self.driver.find_element_by_name('myDistrict'))
    #     count = 0
    #     for k in range(1, len(select_district.options)):
    #         select_district.select_by_index(k)
    #         time.sleep(2)
    #         table_data = []
    #
    #         li2 = self.driver.find_elements_by_xpath('//*[@id="table"]/tbody/tr')
    #         for x in li2:
    #             table_data_rows = x.text
    #             table_data_rows = table_data_rows.split()
    #             table_data.append(table_data_rows)
    #
    #         for i in range(len(table_data)):
    #             for j in range(len(table_data[i])):
    #                 if table_data[i][j].isalpha() and table_data[i][j + 1].isalpha():
    #                     table_data[i][j] = table_data[i][j] + table_data[i][j + 1]
    #
    #         for x in range(len(table_data)):
    #             for y in range(len(table_data[x])):
    #                 if table_data[x][y].isalpha() and table_data[x][y + 1].isalpha():
    #                     del (table_data[x][y + 1])
    #                 break
    #
    #         df = pd.DataFrame(table_data)
    #
    #         index = df.index
    #         number_of_rows = len(index)
    #         table_data.clear()
    #         if number_of_rows ==0:
    #             count = count + 1
    #             print("District" + select_district.first_selected_option.text + "table data not found")
    #
    #     if count !=0:
    #         raise self.failureException('Data not found on table')

    def tearDown(self):
        self.driver.close()
