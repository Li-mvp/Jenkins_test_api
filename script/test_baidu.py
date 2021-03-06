from api.api_baidu import ApiBaidu
import unittest
from parameterized import parameterized
from script.test_poem import TestPoem
import requests
class TestBaidu(unittest.TestCase):
    def testBaidu(self):
        url = "http://www.baidu.com/s"
        #data = TestPoem().test_Poem()

        #para = {"wd":TestPoem().test_Poem()}
        para = {"wd":"da"}

        data=ApiBaidu().api_baidu(url,para)
        print(data.url)
        print(data.text)