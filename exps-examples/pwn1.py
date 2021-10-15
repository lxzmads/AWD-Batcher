#!/usr/bin/env python
# -*- coding=utf-8 -*-

from pwn import *

# pwn
def pwn1(host, passwd):
    p = remote(host, 2077)
    res = p.recv()
    return res.strip()

