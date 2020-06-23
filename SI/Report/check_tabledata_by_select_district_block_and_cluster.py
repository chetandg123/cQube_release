import time
import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


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
    def test_tabledata(self):
        print("")
    # def test_table_data(self):
    #     select_district = Select(self.driver.find_element_by_name('myDistrict'))
    #     select_block = Select(self.driver.find_element_by_name('myBlock'))
    #     select_cluster = Select(self.driver.find_element_by_name('myCluster'))
    #     count = 0
    #     for k in range(1, len(select_district.options)):
    #         select_district.select_by_index(k)
    #         time.sleep(2)
    #         for l in range(1, len(select_block.options)):
    #             select_block.select_by_index(l)
    #             time.sleep(2)
    #             table_data = []
    #             for m in range(1, len(select_cluster.options)):
    #                 select_cluster.select_by_index(m)
    #                 time.sleep(2)
    #
    #                 li2 = self.driver.find_elements_by_xpath('//*[@id="table"]/tbody/tr')
    #                 for x in li2:
    #                     table_data_rows = x.text
    #                     table_data_rows = table_data_rows.split()
    #                     table_data.append(table_data_rows)
    #
    #                 for i in range(len(table_data)):
    #                     for j in range(len(table_data[i])):
    #                         if table_data[i][j].isalpha() and table_data[i][j + 1].isalpha():
    #                             table_data[i][j] = table_data[i][j] + table_data[i][j + 1]
    #
    #                 for x in range(len(table_data)):
    #                     for y in range(len(table_data[x])):
    #                         if table_data[x][y].isalpha() and table_data[x][y + 1].isalpha():
    #                             del (table_data[x][y + 1])
    #                         break
    #
    #                 df = pd.DataFrame(table_data)
    #
    #                 index = df.index
    #                 number_of_rows = len(index)
    #                 table_data.clear()
    #                 if number_of_rows ==0:
    #                     count = count + 1
    #                     print("District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "school" +select_cluster.first_selected_option.text + "table data is not found")
    #
    #     if count !=0:
    #         raise self.failureException('Data not found on table')

    def tearDown(self):
        self.driver.close()
