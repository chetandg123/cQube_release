import os
import time
import unittest

from selenium.webdriver.support.select import Select

from get_dir import pwd


class SchoolsPerClusterCsvDownload():
    def __init__(self, driver,year,month):
        self.driver = driver
        self.year = year
        self.month = month
        self.filename =''

    def check_csv_download(self):
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster = Select(self.driver.find_element_by_name('myCluster'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            time.sleep(2)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                time.sleep(2)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    time.sleep(2)
                    self.driver.find_element_by_id('download').click()
                    time.sleep(3)
                    p=pwd()
                    self.filename =p.get_download_dir() +"/Schools_per_cluster_report_"+self.month +"____"+self.year+ "_"+".csv"
                    if os.path.isfile(self.filename) != True:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    if os.path.isfile(self.filename) == True:
                        os.remove(self.filename)

        return count







