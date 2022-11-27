#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 导入模块
import myemail
import requests
from requests.auth import HTTPBasicAuth
# 现在可以调用模块里包含的函数了
# myemail.sendemail("title","content")

auth = HTTPBasicAuth("oggadmin", "ChinaHarbourP6__123")


def getServiceStatus(url):
    try:
        r = requests.get(url, auth=auth)
        return r.json()["response"]["status"]
    except:
        return "error"


monitored_URLS = {
    "EXTP6_1_URL": "http://10.2.137.14:9012/services/v2/extracts/EXTP6_1/info/status",
    "EXP6_2_URL": "http://10.2.137.19:9012/services/v2/extracts/EXP6_2/info/status",
    "EXP6_3_URL": "http://10.2.137.35:9012/services/v2/extracts/EXP6_3/info/status",
    "REPP61_URL": "http://10.2.60.38:9012/services/v2/replicats/REPP61/info/status",
    "REPP62_URL": "http://10.2.60.38:9012/services/v2/replicats/REPP62/info/status",
    "REPP63_URL": "http://10.2.60.38:9012/services/v2/replicats/REPP63/info/status",
}

for k in monitored_URLS.keys():
    theURL = monitored_URLS.get(k)
    status = getServiceStatus(theURL)
    if (status == 'running'):
        print("running")
    else:
        print("not running")
        content = k + ": not running :"+theURL
        myemail.sendemail("OGG service ERROR!!!", content)
