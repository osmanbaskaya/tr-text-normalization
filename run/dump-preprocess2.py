#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"


import re

data = open('tweets.txt').read()
dd =re.findall('ObjectID\((.*)\),"(.*)"', data)
for tid, text in dd:
    print "{} {}".format(tid,text)



