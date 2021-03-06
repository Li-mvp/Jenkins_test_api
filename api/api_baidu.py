import requests

class ApiBaidu(object):
    def api_baidu(self,url,para):
        return requests.get(url,para)
