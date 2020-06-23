import os
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
    def test_schollevel(self):
        print("")
    # def test_search(self):
    #     select_district = Select(self.driver.find_element_by_name('myDistrict'))
    #     select_block = Select(self.driver.find_element_by_name('myBlock'))
    #     select_cluster = Select(self.driver.find_element_by_name('myCluster'))
    #     count = 0
    #     p =pwd()
    #     for x in range(1, len(select_district.options)):
    #         select_district.select_by_index(x)
    #         time.sleep(2)
    #         for y in range(1, len(select_block.options)):
    #             select_block.select_by_index(y)
    #             time.sleep(2)
    #             for z in range(1, len(select_cluster.options)):
    #                 select_cluster.select_by_index(z)
    #                 time.sleep(2)
    #                 self.driver.find_element_by_id('download').click()
    #                 time.sleep(3)
    #                 filename = p.get_download_dir() + "/schoolPerCluster_report.csv"
    #                 if os.path.isfile(filename) != True:
    #                     print("District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
    #                     count = count + 1
    #                 if os.path.isfile(filename) == True:
    #                     os.remove(filename)
    #
    #     self.assertEqual(0, count, msg="Some files are not downloaded")









    def tearDown(self):
        self.driver.close()