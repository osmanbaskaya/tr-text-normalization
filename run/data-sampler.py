#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys
import random

data = sys.argv[1]
seed = float(sys.argv[2])

random.seed(seed)

lines = open(data).readlines()
random.shuffle(lines)
out = open('tweets-shuffle.txt', 'w')

for line in lines:
    out.write(line)
out.close()




