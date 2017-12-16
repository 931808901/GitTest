# -*- coding:utf-8 -*-

product_list=[
    ('Iphone',5600),
    ('MAC PRO',7800),
    ('SUMSUNG',3216),
    ('Dalla Corte',135),
    ('GIME',600),
    ('Spazoale',60),
    ('Rocket',1200)
]
shopping_list=[]
salary=input('请输入你的工资：')
if salary.isdigit():
    salary=int(salary)
    while True:
        print('----------product list----------')
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice=input('请选择要买商品的编号：')
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<len(product_list) and user_choice>=0:
                p_item=product_list[user_choice]
                if p_item[1]<=salary:
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print ('把%s加入购物车，工资余额为:\033[31;1m%s\033[0m'%(p_item,salary))
                else:
                    print('\033[41;1m工资余额不足，无法购买该商品，请选择其他商品\033[0m')
            else:
                print('你输入的商品编号%s无对应商品，请重新输入'%user_choice)
        elif user_choice =='q':
            print('----------shopping list----------')
            for p in shopping_list:
                print(p)
            print('购物结束，你的余额为',salary)
            exit()
        else:
            print('你输入的内容无效，请重新输入商品编号')
else:
    print('你输入的工资无效，不能进行购物')