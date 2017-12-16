from tkinter import *
import tkFontChooser

class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("画布")

        self.canvas = Canvas(window, width=400, height=300, bg="#FFFFFF")
        self.canvas.pack()

        frame1 = Frame()
        frame1.pack()

        btnRect = Button(frame1, text="矩形", command=self.drawRect)
        btnOval = Button(frame1, text="椭圆", command=self.drawOval)
        btnArc = Button(frame1, text="弧形", command=self.drawArc)
        btnPoly = Button(frame1, text="多边形", command=self.drawPolygon)
        btnLine = Button(frame1, text="线条", command=self.drawLine)
        btnStr = Button(frame1, text="字符", command=self.drawString)
        btnClear = Button(frame1, text="清空", command=self.clearAll)

        btnRect.grid(row=1, column=1)
        btnOval.grid(row=1, column=2)
        btnArc.grid(row=1, column=3)
        btnPoly.grid(row=1, column=4)
        btnLine.grid(row=1, column=5)
        btnStr.grid(row=1, column=6)
        btnClear.grid(row=1, column=7)

        window.mainloop()

        pass

    def drawRect(self):
        # 左上角坐标（10,10）、右下角坐标（190,90）、别名rect、填充为黄色
        self.canvas.create_rectangle(10, 10, 190, 90, tag="rect",width=9,fill="yellow")

    def drawOval(self):
        # 左上角坐标（10,10）、右下角坐标（190,90）、别名oval、填充为red
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tag="oval")

    def drawArc(self):
        # 所属圆左上角坐标（10,10）、右下角坐标（190,90）、别名arc、填充为red、起始角度0-359
        self.canvas.create_arc(10, 10, 190, 90, start=0, extent=120, fill="red", tag="arc")

    def drawPolygon(self):
        # 左上角坐标（10,10）、右下角坐标（190,90）、别名polygon、填充为red
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, fill="red", tag="polygon")

    def drawLine(self):
        self.canvas.create_line(10, 10, 190, 90, 30, 50, tag="line")
        # 依次经过（10,10）（190,90）（30,50）、线粗9，别名line、填充为blue，激活态为red，箭头指向始端（还可以是last）
        self.canvas.create_line(10, 90, 190, 10, 30, 50, width=9, arrow="first", fill="blue", activefill="red",tag="line")

    def drawString(self):
        # 字符中心在（100,100），内容为Hello，字体华文20号，别名string
        self.canvas.create_text(100, 100, text="Hello Tkinter!", font=("华文行楷",20),tag="string")

    def clearAll(self):
        # 清除指定别名的图形
        self.canvas.delete("rect","oval","arc","line","string","polygon")


class GridManagerDemo:
    def __init__(self):
        window = Tk()
        window.title ("网格布局管理器")

        msg = Message(window, text="我是消息,我是消息,我是消息,我是消息",bg="red")
        label1 = Label(window, text="First Name")
        label2 = Label(window, text="Last Name")
        ent1 = Entry(window, width=20)
        ent2 = Entry(window,width=20)
        btn = Button(window, text="Get Name")

        # rowspan=3横跨三行，columnspan=3横跨三列
        # sticky=NSEW，靠北南东西(上下右左)对齐
        # padx=5 x方向间距为5， pady=5 y方向间距为5
        msg.grid(row=1, column=1, rowspan=3, sticky=N, padx=(5,0))
        label1.grid(row=1, column=2)
        ent1.grid(row=1, column=3, padx=5, pady=5,sticky=W)
        label2.grid(row=2, column=2)
        ent2.grid(row=2, column=3)
        btn.grid(row=3, column=3, padx=5, pady=5, sticky=E)

        window.mainloop()
        pass


class PackManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("包管理器")

        Label(window, text="Red", bg="red").pack()
        # Label(window, text="Green", bg="green").pack(fill=BOTH, expand=0)
        Label(window, text="Green", bg="green").pack(fill=BOTH, expand=2)
        Label(window, text="Blue", bg="blue").pack()

        window.mainloop()
        pass


class PackManagerWithSide:
    def __init__(self):
        window = Tk()
        window.title("PackManager With Side")

        Label(window, text="Red", bg="red").pack(side=TOP)
        Label(window, text="Green", bg="green").pack(side=LEFT, fill=BOTH, expand=1)
        Label(window, text="Blue", bg="blue").pack(side=BOTTOM)

        window.mainloop()
        pass


class PlaceManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("PackManager With Side")

        Label(window, text="Red", bg="red").place(x=10, y=10)
        Label(window, text="Green", bg="green").place(x=50, y=50)
        Label(window, text="Blue", bg="blue").place(x=80, y=80)

        window.mainloop()
        pass


if __name__ == '__main__':
    # CanvasDemo()
    # GridManagerDemo()
    # PackManagerDemo()
    # PackManagerWithSide()
    PlaceManagerDemo()
    pass
