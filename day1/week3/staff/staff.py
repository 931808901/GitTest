#coding=utf-8
import csv,time
def staff_info():
    """
    读取员工信息表的信息
    :return:
    """
    f=open('staff_table.txt','r')
    staff=f.readlines()
    f.close()
    staff_message=[]
    for i in staff:
        i=i.strip('\n')
        s= i.split(',')
        staff_message.append(s)
    return staff_message
#员工信息表头
staff_table={'staff_id':0,'name':1,'age':2,'phone':3,'dept'	:4,	'enroll_date':5}
def seek(SQL):
    """
    查询员工信息
    :param SQL:
    :return:
    """
    staff=staff_info()
    def show_result(index):
        if '*' in SQL:
            print(staff[index])
        else:
            list=[]
            table=['staff_id','name','age','phone','dept','enroll_date']
            SQL_content=SQL.split('from')[0].split('select')[1]
            for i in table:
                if i in SQL_content:
                    list.append(staff[index][staff_table[i]])
            print(list)
    if '<' in SQL:
        condition = SQL.split('where')[1].split('<')
        count=0
        i=0
        for st in staff:
            if i==0:
                i+=1
                continue
            if st[staff_table[condition[0].strip()]]<condition[1].strip():
                count+=1
                show_result(i)
            i += 1
        print('共查询到%s个数据'%count)
    if '>' in SQL:
        condition = SQL.split('where')[1].split('>')
        count = 0
        i = 0
        for st in staff:
            if i==0:
                i+=1
                continue
            if st[staff_table[condition[0].strip()]] > condition[1].strip():
                count += 1
                show_result(i)
            i += 1
        print('共查询到%s个数据' % count)
    if '=' in SQL:
        condition = SQL.split('where')[1].split('=')
        count = 0
        i = 0
        for st in staff:
            if i==0:
                i+=1
                continue
            if st[staff_table[condition[0].strip()]] == condition[1].strip():
                count += 1
                show_result(i)
            i += 1
        print('共查询到%s个数据' % count)
    if 'like' in SQL:
        condition = SQL.split('where')[1].split('like')
        count = 0
        i = 0
        for st in staff:
            if i==0:
                i+=1
                continue
            if condition[1].strip() in st[staff_table[condition[0].strip()]] :
                count += 1
                show_result(i)
            i += 1
        print('共查询到%s个数据' % count)
def new_staff():
    """
    新建员工信息
    :return:
    """
    staff = staff_info()
    name=input('请输入员工的姓名：')
    age=input('请输入员工的年龄：')
    phone=input('请输入员工的电话：')
    dept = input('请输入员工的部门：')
    enroll_date=input('请输入员工的入职日期：')
    staff_file = open(u'staff_table.txt', 'a')
    staff_file.write(str(len(staff))+','+name+','+age+','+phone+','+dept+','+enroll_date+'\n')
    staff_file.close()
    staff=staff_info()
    for i in staff:
        print (i)
def del_staff(id):
    """
    删除员工信息，传入员工的id
    :param id:
    :return:
    """
    staff=staff_info()
    staff_file = open(u'staff_table.txt', 'w')
    staff_file.write('staff_id,name,age,phone,dept,enroll_date\n')
    staff_file.close()
    count=1
    for i in range(1,len(staff)):
        if i==int(id):
            continue
        staff_file = open(u'staff_table.txt', 'a')
        staff_file.write(str(count) + ',' + staff[i][1] + ',' + staff[i][2] + ',' +staff[i][3]  + ',' + staff[i][4]  + ',' + staff[i][5]  + '\n')
        staff_file.close()
        count+=1
    print('删除成功')
def modify(SQL):
    """
    修改员工信息
    :param SQL:
    :return:
    """
    staff = staff_info()
    modify_content=SQL.split('where')[0].split('SET')[1].split('=')
    condition = SQL.split('where')[1].split('=')
    i = 0
    for st in staff:
        if i == 0:
            i += 1
            continue
        if st[staff_table[condition[0].strip()]] == condition[1].strip():
            print(st[staff_table[modify_content[0].strip()]])
            st[staff_table[modify_content[0].strip()]]=modify_content[1].strip()
        i+=1
    staff_file = open(u'staff_table.txt', 'w')
    staff_file.write('staff_id,name,age,phone,dept,enroll_date\n')
    staff_file.close()
    for i in range(1,len(staff)):
        staff_file = open(u'staff_table.txt', 'a')
        staff_file.write( staff[i][0] + ',' + staff[i][1] + ',' + staff[i][2] + ',' +staff[i][3]  + ',' + staff[i][4]  + ',' + staff[i][5]  + '\n')
        staff_file.close()
    print('\033[31;1m修改成功！\033[0m')
    staff = staff_info()
    for i in staff:
        print(i)
operate="""
\033[32;1m查询员工信息：1
新建员工信息：2
删除员工信息：3
修改员工信息：4
退出程序：5\033[0m
"""
while True:
    print(operate)
    op=input('请选择你想要的操作：')
    if op=='1':
        SQL=input('请输入查询的SQL语句')
        seek(SQL)
    if op=='2':
        new_staff()
    if op=='3':
        id=input('请输入删除员工的id:')
        del_staff(id)
    if op=='4':
        SQL=input('请输入修改的SQL语句')
        modify(SQL)
    if op=='5':
        exit('\033[41;1m退出程序！\033[0m')





