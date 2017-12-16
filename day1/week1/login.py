# -*- coding: UTF-8 -*-
#读取用户的信息
files=open('user_info.txt','r')
userInfo=files.readlines()
files.close()
users=[]
for i in userInfo:
    i=i.strip('\n')
    s= i.split(' ')
    users.append(s)
error_login_num=0#记录登录错误的次数
while True: 
    userName=input('please input userName:')
    passWord=input('please input password:')
    #读取被锁用户的信息
    files=open('lock_user_info.txt','r')
    lock_user_Info=files.readlines()
    files.close()
    lock_users=[]
    for i in lock_user_Info:
        i=i.strip('\n')
        lock_users.append(i)
    #判断用户是否被锁定
    if userName in lock_users:
        print ('用户名密码输错3个，用户被锁定，请解锁后登录')
        break
    flag=False
    for i in users:
        if userName==i[0] and passWord==i[1]:
            flag=True
            print ('login sucessful')
            break
    if flag:
        break
    else:
        print ('userName or password is wrong,please input again')
        error_login_num+=1
        #用户密码输错3次用户被锁定
        if error_login_num==3:
            lock_user_file = open('lock_user_info.txt', 'a')
            lock_user_file.write(userName)
            lock_user_file.write('\n')
            lock_user_file.close()
            print ('用户名秘密输错3个，用户被锁定，退出登录')
            break
        
    