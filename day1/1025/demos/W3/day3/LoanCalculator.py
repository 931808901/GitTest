#! C:\Python36\python.exe
# coding:utf-8
'''
房贷计算器
'''
from tkinter import Tk, Frame, Label, Entry, Button, StringVar


class LoanCalculator:
    def calculate(self):
        amount = eval(self.amountVar.get())
        monthRate = eval(self.rateVar.get()) / 12
        years = eval(self.yearsVar.get())

        monthPay = (amount * monthRate) / (1 - (1 / (1 + monthRate) ** (years * 12)))
        totalPay = monthPay * years * 12
        print("monthPay=%.2f" % monthPay)
        print("totalPay=%.2f" % totalPay)

        # 丢回结果给控件显示
        # self.monthPayVar.set("您的月供是：%.2f" % monthPay)
        # self.totalPayVar.set("还款总额是：%.2f" % totalPay)
        self.monthPayVar.set(format(monthPay, ">11.2f"))
        self.totalPayVar.set(format(totalPay, ">11.2f"))

    def __init__(self):
        window = Tk()
        window.title("房贷计算器")

        self.amountVar = StringVar()
        self.yearsVar = StringVar()
        self.rateVar = StringVar()
        self.monthPayVar = StringVar()
        self.totalPayVar = StringVar()

        self.monthPayVar.set("000000.00元")
        self.totalPayVar.set("00000000.00元")

        frame = Frame(window)
        frame2 = Frame(window)
        btn = Button(window, text="开始计算", width=30, command=self.calculate)

        frame.pack(padx=10, pady=(10,0))
        frame2.pack(padx=10, pady=(10,10))
        btn.pack(pady=(5, 10))

        Label(frame, text="贷款金额：").grid(row=1, column=1)
        Entry(frame, textvariable=self.amountVar,justify="right").grid(row=1, column=2)
        Label(frame, text="贷款年限：").grid(row=2, column=1)
        Entry(frame, textvariable=self.yearsVar,justify="right").grid(row=2, column=2)
        Label(frame, text="年化利率：").grid(row=3, column=1)
        Entry(frame, textvariable=self.rateVar,justify="right").grid(row=3, column=2)

        Label(frame2, text="您的月供是：").grid(row=1, column=1,sticky="W")
        Label(frame2, textvariable=self.monthPayVar).grid(row=1, column=2,sticky="E")
        Label(frame2, text="还款总额是：").grid(row=2, column=1,sticky="W")
        Label(frame2, textvariable=self.totalPayVar).grid(row=2, column=2,sticky="E")

        window.mainloop()


if __name__ == "__main__":
    # calculate()
    LoanCalculator()

    print("main over")
