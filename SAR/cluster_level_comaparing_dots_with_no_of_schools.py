import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data


class ClusterDotsWithNoOfSchools():
    def __init__(self, driver):
        self.driver = driver

    def comapre_cluster(self):
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster = Select(self.driver.find_element_by_name('myCluster'))
        count = 0
        for x in range(32, len(select_district.options)):
            select_district.select_by_index(x)
            time.sleep(2)
            for y in range(len(select_block.options)-1, len(select_block.options)):
                select_block.select_by_index(y)
                time.sleep(2)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    time.sleep(2)
                    list = self.driver.find_elements_by_class_name(Data.dots)
                    elem = self.driver.find_element_by_id(Data.schoolcount).text
                    res = re.sub("\D", "", elem)
                    if int(len(list) - 1) != int(res):
                        count = count + 1
                        print("no of schools and number of dots are mis matched at" + " "+ select_district.first_selected_option.text+" "+ select_block.first_selected_option.text+" "+select_cluster.first_selected_option.text)
        return count


