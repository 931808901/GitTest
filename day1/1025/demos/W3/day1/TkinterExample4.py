from tkinter import *#导入tkinter/__init__.py下的所有成员
from tkinter import filedialog # 导入tkinter/filedialog.py
from tkinter.filedialog import * # 导入tkinter/filedialog.py下的所有成员
from tkinter import messagebox


class EnlargeShrinkCircle:
    def __init__(self):
        window = Tk()
        window.title("收缩动画")

        self.radius = 50

        self.canvas = Canvas(window, width=200, height=200, bg="white")
        self.canvas.pack()

        self.drawOval()

        self.canvas.bind(sequence="<Button-1>", func=self.increaseCircle)
        self.canvas.bind(sequence="<Button-3>", func=self.decreaseCircle)

        window.mainloop()
        pass

    def drawOval(self):
        self.canvas.create_oval(100 - self.radius, 100 - self.radius, 100 + self.radius, 100 + self.radius, tag="oval")

    def increaseCircle(self, event):
        if self.radius < 100:
            self.canvas.delete("oval")

            # 重新绘制图像
            self.radius += 2
            self.drawOval()
        pass

    def decreaseCircle(self, event):
        if self.radius > 2:
            self.radius -= 2
            self.canvas.delete("oval")
            self.drawOval()
        pass


class AnimationDemo:
    def __init__(self):
        window = Tk()
        window.title("动画示例")

        offset = 60
        x = -1 * offset
        width = 300
        dx = 2

        canvas = Canvas(window, width=300, height=100, bg="white")
        canvas.pack()

        canvas.create_text(x, 50, text="学Python，得永生", tag="text")

        # 循环播放动画（此处的判断条件可以更改）
        while True:
            canvas.after(30)  # 暂停100毫秒
            canvas.move("text", dx, 0)  # 将文本移动（2,0）
            canvas.update()  # 刷新画布

            # 未越界时，不停更新横坐标
            if x < width + offset:
                x += dx

            # 越界时，清除并重绘画布内容
            else:
                x = -1 * offset
                canvas.delete("text")
                canvas.create_text(x, 50, text="学Python，得永生", tag="text")
                pass

        window.mainloop()


class ScrollText:
    def __init__(self):
        window = Tk()
        window.title("滚动条示例")

        scrollbar = Scrollbar(window, orient=VERTICAL)  # orient默认为纵向

        # 双向绑定
        text = Text(window, yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)

        scrollbar.pack(fill=Y, side=RIGHT)
        text.pack(fill=BOTH,expand=True)

        window.mainloop()
        pass


class DialogDemo:
    def __init__(self):
        # 错误提示对话框
        messagebox.showerror("Title", "showerror showerror")

        # 信息提示对话框
        messagebox.showinfo("Title", "showinfo showinfo")

        # 警告对话框
        messagebox.showwarning("Title", "showwarning showwarning")

        # 确定或取消，有返回值
        res = messagebox.askokcancel("Title", "askokcancel askokcancel")
        print(res)

        # 回答是非题，有返回值
        res = messagebox.askquestion("Title", "askquestion askquestion")
        print(res)

        # 重试或取消
        res = messagebox.askretrycancel("Title", "askretrycancel askretrycancel")
        print(res)

        # 回答是非题，有返回值
        res = messagebox.askyesno("Title", "askyesno askyesno")
        print(res)

        # 是、否或取消，有返回值
        res = messagebox.askyesnocancel("Title", "askyesnocancel askyesnocancel")
        print(res)

        pass


def getLocalPathDialog():
    # 选择打开路径，返回路径
    path = filedialog.askopenfilename()
    print(path)

    # 选择存储路径，返回路径
    path = filedialog.asksaveasfilename()
    print(path)


if __name__ == '__main__':
    # EnlargeShrinkCircle()
    # AnimationDemo()
    # ScrollText()
    # DialogDemo()
    getLocalPathDialog()
    pass
