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
        author_id, added_at = data[3][1:-1], data[8][1:-1]
    except IndexError:
        print i, line
        break

    added_at = datetime.strptime(added_at, '%Y-%m-%d %H:%M:%S.%f+%W').hour
    print "%s\t%s" %(author_id, added_at)
    record = ''

