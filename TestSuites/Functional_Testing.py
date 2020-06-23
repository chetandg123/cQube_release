
import sys
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
from Data.parameters import Data
from SAR import sar, run_sar
from SR import semester_report
from get_dir import pwd
p = pwd()
sys.path.append(p.get_system_path())

class MyTestSuite(unittest.TestCase):

    # def test_Issue(self,month):
    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(run_sar)
            # unittest.defaultTestLoader.loadTestsFromTestCase(sar.cQube_Student_Attendance),
            # unittest.defaultTestLoader.loadTestsFromTestCase(semester_report.cQube_Semester_Report),


        ])
        #html_report_generate_path = Data()
        p = pwd()
        outfile = open(p.get_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream = outfile,
            #title = month + 'Test Report',
            verbosity = 1,
            description = 'Functional Testing'

        )

        runner1.run(smoke_test)
        outfile.close()

if __name__ == '__main__':
    unittest.main()