import os
import time
import unittest

from selenium.webdriver.support.select import Select

from get_dir import pwd


class DistrictCsvDownload():
    def __init__(self, driver):
        self.driver = driver
        self.filename =''

    def check_districts_csv_download(self):
        self.driver.find_element_by_css_selector('p >span').click()
        time.sleep(5)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            time.sleep(3)
            self.driver.find_element_by_id('download').click()
            time.sleep(3)
            p = pwd()
            p.get_download_dir()
            self.filename = p.get_download_dir() + "/Block_Per_dist_report.csv"
            if os.path.isfile(self.filename) != True:
                print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                count = count + 1
            if os.path.isfile(self.filename) == True:
                os.remove(self.filename)

        return count








