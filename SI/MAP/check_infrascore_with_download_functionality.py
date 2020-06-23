import csv
import os
import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class SchoolInfra(unittest.TestCase):
    # @classmethod
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_school_infrastructure_map()
        time.sleep(5)

    def test_infra_score(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(1)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("Infra score percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count-1, msg='Failed')

    def test_Boys_toilet_percentage(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(2)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("Boy's toilet percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count-1, msg='Failed')

    def test_drinking_water(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(3)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("Drinking water percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count-1, msg='Failed')

    def test_Electricity(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(4)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("Electricity percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count - 1, msg='Failed')

    def test_girls_toilet(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(5)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("girls toilet percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count - 1, msg='Failed')

    def test_Handpump(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(6)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("Hand pump percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count - 1, msg='Failed')

    def test_Handwash(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(7)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("Handwash percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count - 1, msg='Failed')

    def test_Library(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(8)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("Library percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count - 1, msg='Failed')

    def test_Solar_panel(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(9)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("solar panel percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count - 1, msg='Failed')
    def test_Tapwater(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(10)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("Tapwater percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count - 1, msg='Failed')

    def test_Toilet(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(11)
        self.driver.find_element_by_id('download').click()
        time.sleep(3)
        p = pwd()
        filename = p.get_download_dir() + "/District_wise_report.csv"
        row_count = 0
        with open(filename, 'rt')as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        os.remove(filename)
        print("Toilet percentage is selected and csv file is downloaded")
        self.assertNotEqual(0, row_count - 1, msg='Failed')
    def tearDown(self):
        self.driver.close()