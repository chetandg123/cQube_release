import csv
import os
import re
import time
import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class crc(unittest.TestCase):
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
    def test_schools(self):
        p = pwd()
        District_wise = Select(self.driver.find_element_by_id("downloader"))
        District_wise.select_by_visible_text(" Dist_Wise Report ")
        time.sleep(5)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.filename = p.get_download_dir() + "/District_level_CRC_Report.csv"
        self.assertTrue(os.path.isfile(self.filename), msg="File is not downloaded")
        with open(self.filename) as fin:
            csv_reader = csv.reader(fin, delimiter=',')
            header = next(csv_reader)
            total = 0
            for row in csv.reader(fin):
                total += int(row[5])
            visit = self.driver.find_element_by_id("visited").text
            time.sleep(3)
            res = re.sub('\D',"",visit)
            self.assertEqual(total,int(res),msg="total no of visited are mismatching in district level")
            time.sleep(5)
            os.remove(self.filename)

    def tearDown(self):
        self.driver.close()
