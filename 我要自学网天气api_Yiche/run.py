import unittest
import time
from BSTestRunner import BSTestRunner

test_dir='./test_case'
report_dir='./report'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='yiche_api_test.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+'test_report.html'

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title='Yiche API Test Report',description='China yiche report')
    runner.run(discover)