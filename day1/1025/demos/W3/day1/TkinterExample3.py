from tkinter import *


class ImageDemo:
    def __init__(self):
        window = Tk()
        window.title("图片实例")

        frame1 = Frame()
        frame2 = Frame()
        frame1.pack()
        frame2.pack()

        # 创建图片对象
        imgCa = PhotoImage(file="../res/img/ca.gif")
        imgChn = PhotoImage(file="../res/img/china.gif")
        imgLeft = PhotoImage(file="../res/img/left.gif")
        imgRight = PhotoImage(file="../res/img/right.gif")
        imgUs = PhotoImage(file="../res/img/usIcon.gif")
        imgUk = PhotoImage(file="../res/img/ukIcon.gif")
        imgX = PhotoImage(file="../res/img/x.gif")
        imgO = PhotoImage(file="../res/img/o.gif")

        # 图片位置（90，50），图片对象imgChn
        canvas = Canvas(frame1, bg="gray", width=200, height=100)
        canvas.create_image(90, 50, image=imgChn)
        canvas.pack(side=LEFT)

        # 作为控件配图使用
        Label(frame1, image=imgCa).pack(side=LEFT)
        Button(frame2, image=imgLeft).pack(side=LEFT)
        Button(frame2, image=imgRight).pack(side=LEFT)
        Checkbutton(frame2, image=imgUs).pack(side=LEFT)
        Checkbutton(frame2, image=imgUk).pack(side=LEFT)
        Radiobutton(frame2, image=imgX).pack(side=LEFT)
        Radiobutton(frame2, image=imgO).pack(side=LEFT)

        window.mainloop()
        pass


class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("菜单示例")

        # 创建菜单对象，锁定到窗口（固定菜单）
        menubar = Menu(window)
        window.config(menu=menubar)

        # 为固定菜单添加【操作、退出】两个主菜单（下拉式）
        menuOper = Menu(menubar, tearoff=0)  # tearoff=0：菜单不能从窗口移走
        menuExit = Menu(menubar, tearoff=1)  # 可以从窗口移走
        menubar.add_cascade(label="操作", menu=menuOper)  # 含有下拉子菜单
        menubar.add_cascade(label="退出", menu=menuExit)

        # 为【操作】添加下拉式子菜单
        menuOper.add_command(
            label="Add",
            command=self.onAddSelected  # 响应函数
        )
        menuOper.add_command(label="Subtract")
        menuOper.add_command()
        menuOper.add_command(label="Multiply")
        menuOper.add_command(label="Divide")

        # 为【退出】添加下拉式子菜单
        menuExit.add_command(label="Quit", command=window.quit)

        # img = PhotoImage(file="../res/img/x.gif", width=200, height=200)
        Label(window, text="fuck", bg="blue", width=50, height=10).pack()

        window.mainloop()
        pass

    def onAddSelected(self):
        print("onAddSelected")
        pass


class PopupMenuDemo:
    def __init__(self):
        window = Tk()
        window.title("弹出菜单示例")

        # 创建菜单对象
        self.popupMenu = Menu(window, tearoff=0)

        # 添加菜单项目，定义文本，定义监听函数
        self.popupMenu.add_command(label="Python", command=self.mPython)
        self.popupMenu.add_command(label="Java", command=self.mJava)
        self.popupMenu.add_command(label="C/C++", command=self.mPython)
        self.popupMenu.add_command(label="English", command=self.mPython)

        # <Button-1/2/3>分别代表鼠标的左中右键
        # canvas = Canvas(window, width=200, height=200, bg="white")
        # canvas.pack()
        # 给控件绑定事件，func=self.popup事件对象会自动传给处理函数
        # canvas.bind(sequence="<Button-3>", func=self.popup)

        # lable = Label(window, width=200, height=200, bg="white")
        # lable.pack()
        # lable.bind(sequence="<Button-3>", func=self.popup)frame

        # 部署面板控件
        frame = Frame(window, width=200, height=200, bg="blue")
        frame.pack()

        # 为面板控件绑定鼠标右键事件，在处理函数中将菜单弹出
        frame.bind(sequence="<Button-3>", func=self.popup)

        window.mainloop()

    def mPython(self):
        print("mPython")

    def mJava(self):
        print("mJava")

    # event=被绑定的事件
    def popup(self, event):
        # print(type(event))

        # 弹出菜单
        self.popupMenu.post(event.x_root, event.y_root)
        # self.popupMenu.post(0, 0)


class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()
        window.title("鼠标键盘事件")

        canvas = Canvas(window, width=200, height=200, bg="white")
        canvas.focus_set()  # 让控件获得焦点
        canvas.pack()

        # 分别绑定鼠标左键和键盘事件，交由相应的函数去处理
        canvas.bind(sequence="<Button-1>", func=self.processMouseEvent)  # 绑定鼠标左键，默认会为处理函数传递鼠标事件对象
        canvas.bind(sequence="<Key>", func=self.processKeyboardEvent)  # 绑定键盘事件，默认会为处理函数传递键盘事件对象

        window.mainloop()
        pass

    # 处理鼠标事件，me为控件传递过来的鼠标事件对象
    def processMouseEvent(self, me):
        print("me=", type(me))
        print("位于屏幕", me.x_root, me.y_root)
        print("位于窗口", me.x, me.y)
        print("位于窗口", me.num)

    # 处理鼠标事件，ke为控件传递过来的键盘事件对象
    def processKeyboardEvent(self, ke):
        print("ke.keysym", ke.keysym)  # 按键别名
        print("ke.char", ke.char)  # 按键对应的字符
        print("ke.keycode", ke.keycode)  # 按键的唯一代码，用于判断按下的是哪个键


if __name__ == '__main__':
    # ImageDemo()
    # MenuDemo()
    # PopupMenuDemo()
    MouseKeyEventDemo()
    pass
