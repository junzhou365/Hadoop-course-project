#!/usr/bin/python
import sys
import re
import string
from datetime import datetime

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
        node_id, body, node_type, abs_parent_id = data[0][1:-1], data[4][1:-1], data[5][1:-1], data[7][1:-1]
    except IndexError:
        print i, line
        break

    if node_type == "question":
        print "%s\t%s\t%s" %(node_id, len(body), 0)
    elif node_type == "answer":
        print "%s\t%s\t%s" %(abs_parent_id, 0, len(body))

    record = ''


