'''
乌龟的教学意义：
·引入和使用系统模块
·API=application procedure interface应用程序接口演示
·感受程序的顺序执行（自上而下）
·程序执行结束会自动退出
·消息循环（死循环），阻塞程序使永不退出，直到用户命令退出
'''

'''
绘制同心圆，
填充颜色
在圆心位置书写座右铭
'''
# 导入系统模块turtle
import turtle

turtle.showturtle()

# 绘制外层圆
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()

# 将外层圆填充为蓝色
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

# 绘制内层圆
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()

# 将外层圆填充为白色
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# 在圆心写字
turtle.penup()
turtle.goto(0,-10)
# turtle.goto(-65,-5)
turtle.pendown()
turtle.color("green")
turtle.write("顺我者昌,逆我者亡,我没醉！",align="center",font=("方正舒体", 20, "normal"))

# 开启消息循环（死循环代码）
turtle.done()