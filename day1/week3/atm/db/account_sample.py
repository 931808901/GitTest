#!_*_coding:utf-8_*_


import json
acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2017-01-02',
    'expire_date': '2023-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

print(json.dumps(acc_dic))