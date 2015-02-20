#!/usr/bin/python
import sys

oldKey = None
maxHoursMap = {}
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    thisKey = data[0]
    thisHour = data[1]

    if oldKey and oldKey != thisKey:
        output = []
        maxHourPosts = -1
        for hour in maxHoursMap:
            posts = maxHoursMap[hour]
            maxHourPosts = max(maxHourPosts, posts)
        
        for hour in maxHoursMap:
            posts = maxHoursMap[hour]
            if posts  == maxHourPosts:
                output.append(hour)
        for posts in output:
            print "%s\t%s" %(oldKey, posts)

        maxHoursMap = {}

    if maxHoursMap.get(thisHour):
        maxHoursMap[thisHour] += 1
    else:
        maxHoursMap[thisHour] = 1

    oldKey = thisKey


output = []
maxHourPosts = -1
if oldKey:
    for hour in maxHoursMap:
        posts = maxHoursMap[hour]
        maxHourPosts = max(maxHourPosts, posts)

    for hour in maxHoursMap:
        posts = maxHoursMap[hour]
        if posts == maxHourPosts:
            output.append(hour)
    for posts in output:
        print "%s\t%s" %(oldKey, posts)


