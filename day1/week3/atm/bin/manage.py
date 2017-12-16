#coding=utf-8
import os,time
#注册账号
def register():
    """
    注册账户
    :return:
    """
    data={"pay_day": 22, "enroll_date": "2016-01-02", "status": 0, "password": "abc", "expire_date": "2021-01-01", "credit": 15000, "balance": 15000, "id": 5678}
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_dir = base_dir + r'\db\accounts'
    db_data=os.listdir(db_dir)
    flag=False
    while not flag:
        account=input('请输入注册账号：')
        if account.isdigit():
            if account+'.json' in db_data:
                print('你注册的账号已存在，请重新注册')
                continue
            password=input('请输入密码：')
            data['password']=password
            data['id']=int(account)
            data["enroll_date"]=str(time.strftime("%Y-%m-%d", time.localtime()))
            data["expire_date"] = str(time.strftime('%Y-%m-%d',time.localtime(int(time.time())+5*365*24*60*60)))
            print('\033[31;1m注册成功!\033[0m')
            print('账号信息为：',data)
            account_data = (str(data)).replace('\'', '"')
            acc_dir = base_dir + r'\db\accounts\%s.json' % account
            f = open(acc_dir, 'w')
            f.write(str(account_data))
            f.close()
            flag=True
        else:
            print('输入账号不合法，请重新输入')
def  log_off():
    """
    注销账号
    :return:
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_dir = base_dir + r'\db\accounts'
    db_data = os.listdir(db_dir)
    flag = False
    while not flag:
        account=input('请输入要注销的账号：')
        if account + '.json' in db_data:
            acc_dir = base_dir + r'\db\accounts\%s.json' % account
            os.remove(acc_dir)
            print('\033[32;1m注销成功！\033[0m')
            flag=True
        else:
            print('输入的账号不存在，无法注销')
#注册账号
# register()
#注销账号
log_off()