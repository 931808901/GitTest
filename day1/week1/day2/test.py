#coding=utf-8
s='7 /3*99/4*2998'
flag=False
while not flag:
    if '/' in s or '*'in s:
        if '/' in s[s.find('/')+1:] or '*'in s[s.find('/')+1:] or '/' in s[s.find('*')+1:] or '*'in s[s.find('*')+1:]:
            if s.find('*')>s.find('/') and s.find('/')>0:
                n=0
                if s[s.find('/')+1:].find('/')>s[s.find('/')+1:].find('*') and s[s.find('/')+1:].find('*')>0:
                    n=s[s.find('/')+1:].find('*')
                if s[s.find('/')+1:].find('/')>s[s.find('/')+1:].find('*') and s[s.find('/')+1:].find('*')<0:
                    n=s[s.find('/')+1:].find('/')
                if s[s.find('/')+1:].find('/')<s[s.find('/')+1:].find('*') and s[s.find('/')+1:].find('/')>0:
                    n = s[s.find('/') + 1:].find('/')
                if s[s.find('/')+1:].find('/')<s[s.find('/')+1:].find('*') and s[s.find('/')+1:].find('/')<0:
                    n = s[s.find('/') + 1:].find('*')
                result=int(s[:s.find('/')])/int(s[s.find('/')+1:s.find('/')+n+1])
                s = s.replace(s[:s.find('/') + n + 1], str(int(result)))
            if s.find('*')<s.find('/') and s.find('*')>0:
                n=0
                if s[s.find('*')+1:].find('/')>s[s.find('*')+1:].find('*') and s[s.find('*')+1:].find('*')>0:
                    n=s[s.find('*')+1:].find('*')
                if s[s.find('*')+1:].find('/')>s[s.find('*')+1:].find('*') and s[s.find('*')+1:].find('*')<0:
                    n=s[s.find('*')+1:].find('/')
                if s[s.find('*')+1:].find('/')<s[s.find('*')+1:].find('*') and s[s.find('*')+1:].find('/')>0:
                    n = s[s.find('*') + 1:].find('/')
                if s[s.find('*')+1:].find('/')<s[s.find('*')+1:].find('*') and s[s.find('*')+1:].find('/')<0:
                    n = s[s.find('*') + 1:].find('*')
                result=int(s[:s.find('*')])*int(s[s.find('*')+1:s.find('*')+n+1])
                s = s.replace(s[:s.find('*') + n + 1], str(int(result)))
            if s.find('*')>s.find('/') and s.find('/')<0:
                n=s[s.find('*') + 1:].find('*')
                if n==-1:
                    flag = True
                    result=int(s[:s.find('*')])*int(s[s.find('*')+1:])
                    s = s.replace(s, str(int(result)))
                else:
                    result=int(s[:s.find('*')])*int(s[s.find('*')+1:s.find('*')+n+1])
                    s = s.replace(s[:s.find('*') + n + 1], str(int(result)))
            if s.find('*') < s.find('/') and s.find('*') < 0:
                n = s[s.find('/') + 1:].find('/')
                if n==-1:
                    flag = True
                    result = int(s[:s.find('/')]) / int(s[s.find('/') + 1:])
                    s = s.replace(s, str(int(result)))
                else:
                    result = int(s[:s.find('/')]) /int(s[s.find('/') + 1:s.find('/') + n + 1])
                    s=s.replace(s[:s.find('/') + n + 1],str(int(result)))
        else:
            if '*' in s:
                result=int(s[:s.find('*')])*int(s[s.find('*')+1:])
            if '/' in s:
                result = int(s[:s.find('/')]) / int(s[s.find('/') + 1:])
            s=s.replace(s,str(int(result)))
    else:
        flag=True
print(s)