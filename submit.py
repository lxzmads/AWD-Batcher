#!/usr/bin/env python
#coding: utf-8

import sys
import os
import json

import requests

host = 'http://192.168.1.200/api/v1/att_def/web/submit_flag/?event_id=3'
port = 80
team_token = 'Nwj5sdHk5avSDChCVNYejmcgfBdmTXjGNXtf2t6A8GbhC'

def submit(flag):
    data = {
        "flag": flag,
        "token": team_token
    }
    res = requests.post(host, data=data)
    r = json.loads(res.text.encode())
    if r["success"] == True:
        return True

flags = os.listdir("flags")

if __name__ == '__main__':
    suc = 0

    for flag_file in flags:
        with open("flags/"+flag_file, "r") as f:
            flag = f.read().strip()
            if submit(flag):
                print("[+]"+flag_file[:-4]+" success")
                suc += 1
    print("success "+str(suc) + "/20")


