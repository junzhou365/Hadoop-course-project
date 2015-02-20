#!/usr/bin/python
import sys
import heapq

oldTag = None
frequency = 0
topList = []
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    thisTag = data[0]
    if oldTag and oldTag != thisTag:
        heapq.heappush(topList, (frequency, oldTag))
        if len(topList) == 11:
            heapq.heappop(topList)
        frequency = 0
   
    oldTag = thisTag
    frequency += 1

if oldTag:
    heapq.heappush(topList, (frequency, oldTag))
    if len(topList) == 11:
        heapq.heappop(topList)

for l in sorted(topList, reverse=True):
    print "%s\t%s" %(l[1], l[0])







