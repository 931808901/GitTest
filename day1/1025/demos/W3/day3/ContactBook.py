#! C:\Python36\python.exe
# coding:utf-8
'''
# about what
'''
import pickle
from tkinter import *


class Contact:
    def __init__(self, name, tel, qq, email, address):
        self.name = name
        self.tel = tel
        self.qq = qq
        self.email = email
        self.address = address
        pass


class ContactBook:
    FILE_PATH = "./contact.dat"

    def __init__(self):
        window = Tk()
        window.title("通讯录")

        # 定义联系人数据变量，动态绑定到输入框控件
        self.nameVar = StringVar()
        self.telVar = StringVar()
        self.qqVar = StringVar()
        self.emailVar = StringVar()
        self.addressVar = StringVar()

        # 创建上下两个面板
        fTop = Frame(window)
        fBottom = Frame(window)
        fTop.pack(padx=10, pady=10)
        fBottom.pack(padx=10, pady=10)

        # c1
        Label(fTop, text="姓名").grid(row=1, column=1)
        Label(fTop, text="QQ").grid(row=2, column=1, pady=5)
        Label(fTop, text="地址").grid(row=3, column=1)

        # c2
        entWidth = 17
        Entry(fTop, width=entWidth, textvariable=self.nameVar).grid(row=1, column=2)
        Entry(fTop, width=entWidth, textvariable=self.qqVar).grid(row=2, column=2)
        Entry(fTop, width=41, textvariable=self.addressVar).grid(row=3, column=2, columnspan=3)

        # c3
        Label(fTop, text="电话").grid(row=1, column=3, padx=(5, 0))
        Label(fTop, text="邮箱").grid(row=2, column=3, padx=(5, 0))

        # c4
        Entry(fTop, width=entWidth, textvariable=self.telVar).grid(row=1, column=4)
        Entry(fTop, width=entWidth, textvariable=self.emailVar).grid(row=2, column=4)

        # btns
        btnWidth = 7
        Button(fBottom, width=btnWidth, text="|<<").grid(row=1, column=1)
        Button(fBottom, width=btnWidth, text="Prev", command=self.readPrev).grid(row=1, column=2)
        Button(fBottom, width=btnWidth, text="Next", command=self.readNext).grid(row=1, column=3)
        Button(fBottom, width=btnWidth, text=">>|").grid(row=1, column=4)
        Button(fBottom, width=btnWidth + 3, text="Add", command=self.writeContact).grid(row=1, column=5, padx=(5, 0))

        # 数据逻辑
        # 读取所有联系人数据，并缓存到内存中（以提高访问速度）
        file = open(self.FILE_PATH, "rb")
        self.contactList = []
        while True:
            try:
                contact = pickle.load(file)
                self.contactList.append(contact)

            # 捕获到【读你妹异常】说明加载已完毕，就跳出循环
            except EOFError:
                break
        file.close()

        # 将第一个contact的信息显示到界面上
        self.readContact(0)
        self.index = 0

        window.mainloop()

    def readContact(self, index):
        if len(self.contactList) > 0:
            contact = self.contactList[index]
            self.nameVar.set(contact.name)
            self.telVar.set(contact.tel)
            self.qqVar.set(contact.qq)
            self.emailVar.set(contact.email)
            self.addressVar.set(contact.address)

    def writeContact(self):
        # 从界面控件中读取联系人信息，封装为一个Contact实例
        name = self.nameVar.get()
        tel = self.telVar.get()
        qq = self.qqVar.get()
        email = self.emailVar.get()
        address = self.addressVar.get()
        contact = Contact(name, tel, qq, email, address)

        # 使用二进制IO工具，将Contact实例写入指定文件
        file = open("./contact.dat", "ab")
        pickle.dump(contact, file)
        file.close()

        # 缓存一份在内存
        self.contactList.append(contact)
        self.index = len(self.contactList) - 1
        pass

    def readPrev(self):
        if self.index > 0:
            self.index -= 1
            self.readContact(self.index)

    def readNext(self):
        if self.index < len(self.contactList) - 1:
            self.index += 1
            self.readContact(self.index)
        pass


if __name__ == "__main__":
    ContactBook()
    print("main over")
