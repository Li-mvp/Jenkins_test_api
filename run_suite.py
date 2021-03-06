from tool.HTMLTestRunner import HTMLTestRunner
import unittest
import time

suite=unittest.defaultTestLoader.discover('./script',pattern='test_baidu.py')
print(suite)
file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
with open(file_path,"wb") as f:
    HTMLTestRunner(stream=f,verbosity=2,title="测试报告").run(suite)