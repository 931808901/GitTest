#coding=utf-8
import re
def multiply_divide(expression):
    """
    :param expression: 乘除运算
    :return: 返回乘除的运算结果
    """
    if '*' in expression:
        result=float(expression[:expression.find('*')])*float(expression[expression.find('*')+1:])
    if '/'in expression:
        result = float(expression[:expression.find('/')]) / float(expression[expression.find('/') + 1:])
    return str(float(result))
def add_subtract(expression):
    """
    :param expression: 加减的表达式
    :return: 返回运算的结果
    """
    expression = expression.replace('--', '+')
    expression1 = ''
    #把减前面加
    count=0
    for i in expression:
        if i == '-' and count!=0:
            expression1 = expression1 + '+'
        expression1 = expression1 + i
        count+=1
    expression1 = expression1.replace('++', '+')
    data = expression1.split('+')
    sum = 0
    for i in range(len(data)):
        sum = sum + float(data[i])
    return str(sum)
def  bracket_operation(expression):
    """
    :param expression: 传入有括号的表达式
    :return: 返回运算结果
    """
    expression=expression[1:-1]
    flag=False
    while not flag:
        if '*' in expression or '/' in expression:
            expression1=re.search('[0-9]{1,}[.]?[0-9]*[\*\/][-]?[0-9]{1,}[.]?[0-9]*', expression).group()
            expression=expression.replace(expression1,multiply_divide(expression1))
        else:
            flag=True
    if '+' in expression or '-' in expression:
        if expression[0]=='-' and expression.count('-')==1 and expression.count('+')==0:
            return str(expression)
        expression=add_subtract(expression)
    return str(expression)
def counter(expression):
    """
    :param expression: 计算器运算，支持加减乘除括号运算
    :return: 返回运算结果
    """
    expression1=''
    for i in expression:
        if i==' ':
            continue
        expression1=expression1+i
    expression=expression1
    flag=False
    while not flag:
        if '(' in expression:
            expression1=re.search(r'\([^()]+\)', expression).group()
            expression=expression.replace(expression1,bracket_operation(expression1))
        else:
            flag=True
    flag = False
    while not flag:
        if '*' in expression or  '/' in expression:
            expression1 = re.search('[0-9]{1,}[.]?[0-9]*[\*\/][-]?[0-9]{1,}[.]?[0-9]*', expression).group()
            expression = expression.replace(expression1, multiply_divide(expression1))
        else:
            flag = True
    if expression[0]=='-' and expression.count('-')==1 and expression.count('+')==0:
        return str(expression)
    if '+' in expression or '-' in expression:
        expression=add_subtract(expression)
    return str(expression)
s=' 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
print(counter(s))
flag=False
while not flag:
    s=input('输入运算的表达式：')
    if s=='b':
        print('退出程序')
        flag=True
    else:
        print(counter(s))