from tkinter import *


# 认识tk窗口，了解消息循环
def simpleGUI():
    # 创建程序窗口
    window = Tk()

    # 创建控件实例
    lable = Label(
        window,  # 父容器
        text="Hello"  # 选配的关键字参数（详见源码注释）
    )
    button = Button(
        window,  # 父容器
        text="Click me"  # 选配的关键字参数（详见源码注释）
    )

    # 将控件打包到父容器中
    lable.pack()
    button.pack()

    # 死循环等待用户操作
    window.mainloop()


# 处理按钮点击事件
def dealBtnOk():
    print("dealBtnOk")
    pass


# 处理按钮点击事件
def dealBtnCancel():
    print("dealBtnCancel")
    pass


# 在窗口放置按钮，并设置其点击事件
def processBtnEvent():
    # 创建窗口
    window = Tk()

    # 创建两个按钮实例
    btnOk = Button(
        window, text="OK", foreground="red",
        command=dealBtnOk  # 按钮的点击事件监听器，指向一个响应函数名，不要加()，否则语法上不正确
    )
    btnCancel = Button(window, text="Cancel", background="red", command=dealBtnCancel)

    # 将实例打包到父容器当中
    btnOk.pack()
    btnCancel.pack()

    # 开启消息（死）循环（等候用户输入）
    window.mainloop()
    pass


# 将窗口和按钮事件封装为类
class EventProcessButton():
    # 在初始化方法中添加窗口和事件监听
    def __init__(self):
        window = Tk()
        btnOk = Button(window, text="OK", foreground="red", command=self.processBtnOk)
        btnCancel = Button(window, text="Cancel", background="#0000ff", command=self.processBtnCancel)
        btnOk.pack()
        btnCancel.pack()
        window.mainloop()
        pass

    # 事件监听函数也封装在类中
    def processBtnOk(self):
        print("processBtnOk")
        pass

    # 事件监听函数也封装在类中
    def processBtnCancel(self):
        print("processBtnCancel")
        pass


# 本类展示了Checkbutton、Radiobutton、Entry、Message、Label、Text的使用方式
# 并使用表格布局将它们布局在界面中
class WidgetDemo():
    def __init__(self):
        # 窗口和标题
        window = Tk()
        window.title("Widgets Demo")

        # 使用面板并添加到窗口
        frame1 = Frame(window)
        frame2 = Frame(window)
        frame1.pack()
        frame2.pack()

        # 构造Checkbutton并绑定数据和监听
        self.cbValue = IntVar()
        cb = Checkbutton(frame1, text="Bold", variable=self.cbValue, command=self.onCheckbuttonChanged)

        # 构造Radiobutton并绑定数据和监听
        # 将两个Radiobutton置为一个单选按钮组
        self.rbValue = IntVar()
        rb1 = Radiobutton(frame1, text="Red", background="Red", variable=self.rbValue, value=1,
                          command=self.onRadioButtonChanged)
        rb2 = Radiobutton(frame1, text="Yellow", background="Yellow", variable=self.rbValue, value=2,
                          command=self.onRadioButtonChanged)
        rb3 = Radiobutton(frame1, text="Blue", background="blue", variable=self.rbValue, value=3,
                          command=self.onRadioButtonChanged)

        # 表格布局控件，不必再pack
        cb.grid(row=1, column=1)
        rb1.grid(row=1, column=2)
        rb2.grid(row=1, column=3)
        rb3.grid(row=1, column=4)

        # 标签
        lable = Label(frame2, text="Enter your name")

        # 输入框及数据绑定
        self.entryValue = StringVar()
        entry = Entry(frame2, textvariable=self.entryValue)

        # Message
        btnGet = Button(frame2, text="Get Name", command=self.onBtnGetnameClick)
        msg = Message(frame2, text="its a msg")

        # 将控件以行列形式布局在界面中，不必再pack
        lable.grid(row=1, column=1)
        entry.grid(row=1, column=2)
        btnGet.grid(row=1, column=3)
        msg.grid(row=1, column=4)

        # 文本域，插入文字内容
        text = Text(window, width=50, height=10)
        text.insert(END, "Abcdefg\n")
        text.insert(END, "Hijklmn\n")
        text.insert(END, "Okqrst\n")
        text.pack()

        window.mainloop()

    # Checkbutton的事件监听函数，从绑定的数据中获取数据
    def onCheckbuttonChanged(self):
        print(self.cbValue.get())
        print("onCheckbuttonChanged:" + ("checked" if self.cbValue.get() == 1 else"unchecked"))
        pass

    # RadioButton的单选事件监听
    def onRadioButtonChanged(self):
        print("您当前选中的是%d号Radiobutton" % (self.rbValue.get()))
        # print("onRadioButtonChanged:" + ("rb1" if self.rbValue.get() == 1 else"rb2"))
        pass

    # 按钮的事件监听，获取Entry所绑定的数据
    def onBtnGetnameClick(self):
        print(self.entryValue.get())
        pass


class ChangeLableDemo():
    def __init__(self):
        window = Tk()
        window.title("Change Lable Demo")

        self.lable = Label(window, text="Programming is fun")
        self.lable.pack()

        frame1 = Frame()
        frame1.pack()

        self.rbValue = StringVar()
        self.entValue = StringVar()
        self.rbValue.set("R")

        lable2 = Label(frame1, text="Enter text:")
        entInput = Entry(frame1, textvariable=self.entValue)
        btnChange = Button(frame1, text="Change Text", command=self.onBtnChangeClick)
        rb1 = Radiobutton(frame1, text="Red", variable=self.rbValue, value="R", bg="red", command=self.onRadioChanged)
        rb2 = Radiobutton(frame1, text="Yellow", variable=self.rbValue, value="Y", bg="yellow",
                          command=self.onRadioChanged)

        lable2.grid(row=1, column=1)
        entInput.grid(row=1, column=2)
        btnChange.grid(row=1, column=3)
        rb1.grid(row=1, column=4)
        rb2.grid(row=1, column=5)

        window.mainloop()

        pass

    def onBtnChangeClick(self):
        print("onBtnChangeClick:" + (self.entValue.get()))
        pass

    def onRadioChanged(self):
        # print("onRadioChanged:" + ("Red" if self.rbValue.get()=="R" else "Yellow"))
        if self.rbValue.get() == "R":
            self.lable["fg"] = "red"  # 改变标签前景色
        else:
            self.lable["fg"] = "yellow"
        pass


if __name__ == '__main__':
    simpleGUI()
    # processBtnEvent()
    # EventProcessButton()
    # WidgetDemo()
    # ChangeLableDemo()
    pass
