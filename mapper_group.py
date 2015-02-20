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
        node_id, author_id, abs_parent_id = data[0], data[3], data[7]
    except IndexError:
        print i, line
        break

    if abs_parent_id == '\N':
        print "%s\t%s" %(node_id, author_id)
    else:
        print "%s\t%s" %(abs_parent_id, author_id)

    record = ''


