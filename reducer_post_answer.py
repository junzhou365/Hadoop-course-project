#!/usr/bin/python
import sys

old_q_id = None
a_num = 0
a_total_len = 0
q_len = 0
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 3:
        continue
    
    q_id = data[0]
    if old_q_id and old_q_id != q_id:
        print "%s\t%s\t%s" %(old_q_id, q_len, (a_total_len / (a_num - 1) if a_num > 1 else 0))
        a_num = 0
        a_total_len = 0
        q_len = 0
        
    if int(q_len) == 0:
        q_len = data[1]  
    a_total_len += int(data[2])
    a_num += 1

    old_q_id = q_id

if old_q_id:
        print "%s\t%s\t%s" %(q_id, q_len, (a_total_len / (a_num - 1) if a_num > 1 else 0))





