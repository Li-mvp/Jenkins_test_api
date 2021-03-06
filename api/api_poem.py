import requests

class ApiPoem(object):
    def api_poem(self,url,para):
        return requests.get(url,para)

