# -*- coding:utf-8 -*-


with open('ha_config.txt','r') as f:
    backend_no=0
    for line in f:
        if 'backend' in line and 'www.oldboy.org' in line :
            backend_no+=1
            break
        backend_no += 1
    f.seek(0)
    num=0
    for line in f:
        if num<=backend_no+1:
            num+=1
            continue
        print(line)
        if 'server' not in line:
            break

