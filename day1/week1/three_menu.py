# -*- coding: UTF-8 -*-
video={
    'movie':{
        "area":{
            "Euramerican":["TerrorTrain","Alana","Manley"],
            "Continent":["Howard ","Swanson"]
        },
        "type":{
            "suspense":["Harry Potter"," Moonstruk"],
            "comedy":["Love in a Puff","Gone with the wind"],
            "history":["Advent",".Legend.Of.The.Guardians"],
        },
        "hot":{"createdBy":100000410020,"createdDate":"2017-03-22 11:34:51"},
    },
    'TVplay':{
        "literary":{"fname":"AutoTest","id":100006847442},
        "adventure":{"createdBy":100000410020,"createdDate":"2017-05-18 17:11:16"},
        "Magic":{"fname":"AutoTest3477349","id":100008054375}
    },
    'manga':{
        "swordsman":{"firstname":"刘备","deptId":100005075009},
        "literature ":{"firstname":"唐僧","deptId":100005082289},
        "bizarre":{"createdDate":"2017-05-19 16:46:04","id":"591eb0cc0cf2b75475a7271d"},
    }   
}
exitFlag=False
while not exitFlag:
    while not exitFlag:
        print (video.keys())
        choice=input('请选择要进入的一级菜单：')
        if choice in video.keys():
            while not exitFlag:
                print (video[choice].keys())
                choice2=input('请选择要进入的二级菜单：')
                if choice2 in video[choice].keys():
                    while not exitFlag:
                        print (video[choice][choice2].keys())
                        choice3=input('请选择要进入的三级菜单：')
                        if choice3 in video[choice][choice2].keys():
                            print ('你所选择的三级菜单内为',video[choice][choice2][choice3])
                        #输入b返回上一层
                        elif choice3=='b':
                            print ('程序返回上一级菜单')
                            break
                        #输入退出
                        elif choice3=='q':
                            print('程序成功退出')
                            exitFlag =True
                        else:
                            print ('你输入的内容超出展示的范围，请重新输入')
                #输入b返回上一层
                elif choice2=='b':
                    print ('程序返回上一级菜单')
                    break
                #输入退出
                elif choice2=='q':
                    print ('程序成功退出')
                    exitFlag =True
                else:
                    print ('你输入的内容超出展示的范围，请重新输入')
        #输入b返回上一层
        elif choice=='b':
            print ('程序返回上一级菜单')
            break
        #输入退出
        elif choice=='q':
            print ('程序成功退出')
            exitFlag =True
        else:
            print ('你输入的内容超出展示的范围，请重新输入')
