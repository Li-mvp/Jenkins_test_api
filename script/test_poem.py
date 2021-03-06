import unittest
from api.api_poem import ApiPoem
from tool.read_json import ReadJson
from parameterized import parameterized

def get_data():
    data = ReadJson("poem.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                data.get("page"),
                data.get("count")))
    return arrs

def get_more_data():
    datas = ReadJson("poem_more.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("page"),
                     data.get("count")))
    return arrs


class TestPoem(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_Poem(self,url,page,count):

        url=url
        para={"page":page,"count":count}


        data = ApiPoem().api_poem(url,para)
        data1 = data.json()["message"]
        return data1



