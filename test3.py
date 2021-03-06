import requests
import json


def post1():
    url = "https://mod-api.xinpianchang.com/mod/api/v2/media/o36Jm4ao1G27yjzB/like?appKey=61a2f329348b3bf77"
    data = {'appKey': '61a2f329348b3bf77'}
    reponse = requests.post(url)
    print(reponse.text)
    print(reponse.status_code)

def get2():
    url = "https://www.baidu.com/s"
    para = {"wd": "nba"}
    reponse = requests.get(url, params=para)
    print(reponse.text)
    print(reponse.status_code)

def get1():
    url = "https://www.vmovier.com/search"
    para = {"kw":"nba"}
    reponse = requests.get(url,params=para)
    print(reponse.text)
    print(reponse.status_code)

if __name__ == '__main__':
   post1()