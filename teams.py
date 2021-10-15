#!/usr/bin/env python
# -*- coding=utf-8 -*-
import random,string,re,itertools,sys

from IPy import IP

def ip_parser_with_ipy(ipstr):
    try:
        ips = IP(ipstr)
        return ips
    except Exception as _:
        return False

def ip_parser_custom(ipstr):
    # parse format like 192.168.7.1-2, 192.168.1-20.1, 192.168.1-3.10-20
    ip_pattern = "^(\d{1,3}(-\d{1,3})?)\.(\d{1,3}(-\d{1,3})?)\.(\d{1,3}(-\d{1,3})?)\.(\d{1,3}(-\d{1,3})?)$"
    if not re.match(ip_pattern, ipstr):
        return False
    ips = ipstr.split(".")
    iters = []
    for seg in ips:
        if "-" in seg:
            l = int(seg.split("-")[0])
            r = int(seg.split("-")[1])
            if not (0 <= l <= 255) or not (0 <= r <= 255):
                return False
            it = [i for i in range(l, r + 1)]
            iters.append(it)
        else:
            if not (0 <= int(seg) <= 255):
                return False
            iters.append([seg])
    res = itertools.product(*iters)
    res = [".".join([str(i) for i in r]) for r in res]
    return res

def ip_parser(ipstr):
    # first parse with IPy
    ips = ip_parser_with_ipy(ipstr)
    if not ips:
        ips = ip_parser_custom(ipstr)

    return ips

def randpass():
    return ''.join(random.choices(string.ascii_letters, k=8))

def main():
    blacklist = ("172.35.14.10",) # 自己队伍的IP/师弟队伍的IP

    ipstr = "172.35.1-20.10" if len(sys.argv) < 2 else sys.argv[1]
    ips = ip_parser(ipstr)
    with open("teams.conf", 'w') as f:
        for ip in ips:
            if ip in blacklist:
                continue
            line = str(ip) + " " + randpass()
            f.write(line + "\n")

if __name__ == "__main__":
    main()


