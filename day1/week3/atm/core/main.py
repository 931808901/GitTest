#!_*_coding:utf-8_*_

'''
main program handle module , handle all the user interaction stuff
'''

from core import auth
from core import accounts
from core import logger
from core import accounts
from core import transaction
import time,os

#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')


#temp account data ,only saves the data in memory
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None

}

def account_info(acc_data):
    print(user_data)
def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    #for k,v in account_data.items():
    #    print(k,v )
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) >0 and repay_amount.isdigit():
            print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay', repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)

        if repay_amount == 'b':
            back_flag = True
def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True

def transfer(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    print(account_data)
    back_flag = False
    while not back_flag:
        transfer_acc = input('请输入转账账号：')
        if transfer_acc.isdigit():
            try:
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                acc_dir = base_dir + r'\db\accounts\%s.json'%transfer_acc
                acc_dir1 = base_dir + r'\db\accounts\%s.json' % str(account_data["id"])
                trans_file = open(acc_dir, 'r')
                trans_content = trans_file.read()
                trans_file.close()
                trans_content = eval(trans_content)
                transfer_num=input('请输入转账金额：')
                if transfer_num.isdigit() and int(transfer_num)>0 and int(transfer_num)<=account_data["balance"]:
                    trans_content["balance"]+=int(transfer_num)
                    account_data["balance"]-=int(transfer_num)
                    trans_content=(str(trans_content)).replace('\'','"')
                    f = open(acc_dir, 'w')
                    f.write(trans_content)
                    f.close()
                    account_data = (str(account_data)).replace('\'', '"')
                    f = open(acc_dir1, 'w')
                    f.write(str(account_data))
                    f.close()
                    print('\033[32;1m转账成功!\033[0m')
                else:
                    print('\033[42;1m转账金额不合法！\033[0m')
            except:
                print('\033[31;1m转账账号不存在\033[0m')
        else:
            if transfer_acc=='b':
                back_flag=True
            print('输入账号不合法，请重新输入')
def pay_check(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    if float(account_data['credit'])<=float(account_data['balance']):
        print('账单为0,无欠款')
    else:
        print('账单为%s'%(float(account_data['credit'])-float(account_data['balance'])))
def logout(acc_data):
    exit('退出程序')
def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    -------  Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")
def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)
