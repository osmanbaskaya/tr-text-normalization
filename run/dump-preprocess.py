#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

data="collection.csv"
#data="a"
lines = open(data).readlines()
sent = ""
for line in lines:
    if line.startswith('ObjectID'):
        if len(sent) == 0:
            sent = line
        else:
            print sent.replace('\n', ' ')
            sent = line
    else:
        sent = sent + line
        #print sent.replace('\n', '')
    







