import requests
import time
import json
url = "https://passport.xinpianchang.com/api/user-center/user/login/?type=phone"
url1 = "https://www.vmovier.com"
method="post"
data = {
	"phone": "18784182847",
	"password": "qwas0123",
	"regionCode": "+86",
	"loginType": 3,
	"vmovier": True
}
header = {'accept':'application/json,text/html;q=0.9,application/xhtml+xml;q=0.9,application/xml;q=0.8,*/*;q=0.7',
          'content-type':'application/json; charset=utf-8',
          'referer':'https://passport.xinpianchang.com/login?redirect_uri=http%3A%2F%2Fwww.vmovier.com%2Fuser%2FpassportCallback%3Fcallback%3Dhttps%253A%252F%252Fwww.vmovier.com%252F'}

cookies ={'UM_distinctid''176c7e70f50548-0d018b21cbf85c-6d112d7c-13c680-176c7e70f519e3'}
coo=requests.cookies.RequestsCookieJar()
coo.set('UM_distinctid','176c7e70f50548-0d018b21cbf85c-6d112d7c-13c680-176c7e70f519e3')
session = requests.session()
url2 = "https://www.vmovier.com/user/notice"
reponse = requests.post(url1,verify=False,cookies=coo)
reponse1= requests.post(url2,verify=False,cookies=coo)
print(reponse1.text)

