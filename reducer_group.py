#!/usr/bin/python
import sys
import heapq

oldKey = None
sdu_list = []
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    thisKey = data[0]
    if oldKey and oldKey != thisKey:
        print "%s\t%s" %(oldKey, sdu_list)
        sdu_list = []

    oldKey = thisKey
    try:
        sdu_list.append(int(data[1]))
    except ValueError:
        sdu_list.append(int(data[1][1:-1]))
    else:
        print "oops", line
        break


if oldKey:
    print "%s\t%s" %(oldKey, sdu_list)










