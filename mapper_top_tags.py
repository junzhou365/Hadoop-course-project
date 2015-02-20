#!/usr/bin/python
import sys

record = ''
for i, line in enumerate(sys.stdin):
    if i == 0 :
    	continue
    record += line
    data = None
    if record[-1] == '\n':
        data = record.split('	')
        if len(data) != 19:
            continue
    try:
        tags, node_type = data[2], data[5]
        tags = tags.strip()[1:-1].split(' ')
        node_type = node_type[1:-1]
    except IndexError:
        print i, line
        break

    if node_type == "question":
        for tag in tags:
            print "%s\t1" %tag

    record = ''


