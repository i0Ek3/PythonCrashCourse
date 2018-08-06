#!/usr/bin/env python
# coding=utf-8

cnt = 0
while cnt < 10:
    cnt += 1
    if cnt % 2 == 0:
        continue
    elif cnt % 2 != 0:
        cnt += 2 
    else:
        break
    print(cnt)
