#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"


import sys
import gzip

data = sys.argv[1]
lines = gzip.open(data)

for line in lines:
    try:
        line.decode('utf-8')
        print line,
    except:
        pass



