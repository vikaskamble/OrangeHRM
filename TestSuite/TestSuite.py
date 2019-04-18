import unittest
import os
import sys
from POMProjectDemo.Tests.Login import Login_Test
from POMProjectDemo.Tests.TC_002_AddEmployee import AddEmpoyee


sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from pyunitreport import HTMLTestRunner
from os.path import dirname, abspath


d = dirname(dirname(dirname(abspath(__file__))))

# get the directory path to output report file
dir = os.getcwd()
# print(dir)

# Load test Case
login = unittest.TestLoader().loadTestsFromTestCase(Login_Test)
add_Employee = unittest.TestLoader().loadTestsFromTestCase(AddEmpoyee)

# Create Test Suite
test_Suite = unittest.TestSuite([login, add_Employee])


htmlReportPath = os.path.join(dirname(dirname(abspath(__file__))), 'ReportTest')
# unittest.main(testRunner=HTMLTestRunner(output=htmlReportPath))
# unittest.TestSuite(test_Suite)
# unittest.main(testRunner=HTMLTestRunner(output=htmlReportPath))



# test_Suite = unittest.TestSuite([login])
unittest.TextTestRunner(verbosity=2).run(test_Suite)




