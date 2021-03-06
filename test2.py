import requests

url = "https://passport.cnblogs.com/user/signin"

session = requests.Session()

reponse = session.get(url,verify=False)
print(reponse.text)