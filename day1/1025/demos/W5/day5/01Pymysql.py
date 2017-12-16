#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import pymysql


def helloPymysql():
    # 取得数据库连接
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="world",
                           charset="utf8")
    # 获取数据游标
    cursor = conn.cursor()
    # 执行SQL语句
    rows = cursor.execute("select * from t_student")
    result = cursor.fetchall()
    # 提交
    conn.commit()
    # 关闭游标、连接
    cursor.close()
    conn.close()
    # 打印结果
    print(rows, result)


if __name__ == "__main__":
    # helloPymysql()
    rows = 0
    conn = pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="world",charset="utf8")
    cursor = conn.cursor()

    try:
        # conn.begin()
        rows += cursor.execute("insert into t_student(name,age) values(%s,%d);"%('"李逵"',30))
        rows += cursor.execute("delete from t_student where name=%s;"%('"时迁"'))
        rows += cursor.execute("update t_student set name=%s where name=%s;"%('"秦明"','"关胜"'))
        conn.commit()

    except Exception as e:
        print(e)

        # 一旦发生异常，事务回滚，所有操作回到事务前的状态（！并没有发现对已经commit了的操作实现回滚）
        conn.rollback()
        rows = 0

    cursor.close()
    conn.close()

    print("执行成功，%d记录受影响"%(rows))
    print("main over")