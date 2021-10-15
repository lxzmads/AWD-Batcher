# -*- coding=utf-8 -*-
#!/usr/bin/env python
import os
import importlib
import threading

teams = set()

# 打开所有队伍的IP文件，每个队伍有不一样的密码
with open("teams.conf", "r") as f:
    lines = f.readlines()
    for team in lines:
        teams.add((team.split(" ")[0].strip(), team.split(" ")[1].strip()))

# 列出所有的可用exp
package = 'exps'
exps = os.listdir(package)
exps = list(map(lambda x:x.split('.')[0], exps))

# 动态加载exp
def exploit(ip, passwd):
    with open('flags/'+ip+".txt", "w") as f:
        for exp in exps:
            if '__init__' in exp or '__pycache__' in exp:
                continue
            e = importlib.import_module(package+"."+exp)
            print(ip+": exp: "+exp)
            func = getattr(e, exp)
            flag = func(ip, passwd)
            if flag and len(flag) == 60:
                print(ip+ ": "+exp+": "+flag)
                f.write(flag+"\n")
                break

# 批量验证POC，获取flag
def multi():
    for team in teams:
        ip = str(team[0])
        passwd = team[1]
        print("[*] starting exploiting "+ip)
        # 多线程验证
        t = threading.Thread(target=exploit, args=(ip, passwd))
        t.start()

multi()
