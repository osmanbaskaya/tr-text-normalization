#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import gzip
import sys

TARGET=' __XX__ '

dataset = sys.argv[1]

#input_file = 'parsed_OB.txt'
#lines = open(input_file).readlines()

index_file = gzip.open(dataset+'.index.gz', 'w')
token_file = gzip.open(dataset+'.token.gz', 'w')

def slide_index(elements, remove):
    remove.sort()
    arr = []
    for e in elements:
        count = 0
        for r in remove:
            if r < e:
                count += 1
        arr.append(e - count)
    return arr

def parselist2int(str_list):
    if str_list[0] != '':
        str_list = map(int, str_list)
    else:
        str_list = []
    return str_list

for i, line in enumerate(sys.stdin):

    # reading 
    line = line.split('||')
    text = line[0].split()
    if len(text) == 0:
        continue

    mentions = line[1][1:-1].split(', ')
    hashtags = line[2][1:-1].split(', ')
    ivs = line[3][1:-1].split(', ')
    oovs = line[4][1:-1].split(', ')
    punct = line[5][1:-1].split(', ')

    mentions, hashtags, ivs, oovs, punct = map(parselist2int, \
                                    [mentions, hashtags, ivs, oovs, punct])

    new_oovs = slide_index(oovs, punct)
    new_ivs = slide_index(ivs, punct)

    # removing punctuation
    t = line[0].split()
    #t = t.translate(string.maketrans('', ''), string.punctuation)
    #t = t.split()
    for p in punct:
        t.remove(text[p])

    for j, oov_ind in enumerate(new_oovs):
        word = t[oov_ind]
        right_ind = max(0, oov_ind - 1)
        left_ind = min(len(t) - 1, oov_ind + 1)
        context = ""
        if right_ind in new_ivs:
            context += t[right_ind]
        context += TARGET
        if left_ind in new_ivs:
            context += t[left_ind]

        if context != TARGET:
            context = context.strip()
            print context
            index_file.write('{},{}\n'.format(i, oovs[j]))
            token_file.write("%s\n" % word)

    
