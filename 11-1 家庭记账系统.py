# ===========================创建函数===================================
import pymysql
# ======================查询数据====================
def select(sql,info):
    # 连接数据库
    con = pymysql.connect(host="localhost", user="root", password="root", database="keep_accounts")
    cursor = con.cursor()# 使用cursor（）方法创建一个游标对象
    # if x=="":
    #     sql="select * from finance "
    #     cursor.execute(sql)# 使用execute（）方法执行SQL语句
    # else:
    #     sql = "select * from finance where ID=%s"
    cursor.execute(sql, info)
    return cursor.fetchall()#使用fetchall（）获取全部数据
    cursor.close()#关闭游标
    con.close()#关闭数据库

# ======================插入数据====================
def insert(sql, info):
    con = pymysql.connect(host="localhost", user="root", password="root", database="keep_accounts")
    cursor = con.cursor()
    cursor.execute(sql, info)
    con.commit()  # 提交数据
    cursor.close()
    con.close()
# ======================修改数据====================
def update(sql,info):
    con = pymysql.connect(host="localhost", user="root", password="root", database="keep_accounts")
    cursor = con.cursor()
    cursor.execute(sql,info)
    con.commit()
    cursor.close()
    con.close()
# ======================删除数据====================
def delete(sql,info):
    con = pymysql.connect(host="localhost", user="root", password="root", database="keep_accounts")
    cursor = con.cursor()
    cursor.execute(sql, info)
    con.commit()
    cursor.close()
    con.close()
# 添加账务
def add():
    # 类别,账户，金额，时间，说明
    category = input("请输入类别：")
    account = input("请输入账户：")
    money = input("请输入金额")
    time = input("请输入时间")
    explain = input("请输入说明")
    sql = "insert into finance(类别,账户,金额,时间,说明) values(%s,%s,%s,%s,%s)"
    info = [category, account, money, time, explain]
    insert(sql, info) #调用insert函数，插入数据
    return "添加财务成功！"
# 编辑账务
def revamp():
    id=input("请输入ID")
    sql='select * from finance where ID=%s'
    info=[id]
    if len(select(sql,info))==1:   #调用select函数，并判断是否有值
        category = input("请输入新类别：")
        account = input("请输入新账户：")
        money = input("请输入新金额")
        time = input("请输入新时间")
        explain = input("请输入新说明")
        sql='update finance set 类别=%s,账户=%s,金额=%s,时间=%s,说明=%s where ID=%s'
        info=[category,account,money,time,explain,id]
        update(sql,info)  #调用函数，修改数据
        return "编辑财务成功！"
    else:
        return "ID号输入有误，编辑财务失败"   #掉用select函数，没有值的时候返回ID输入有误
# 删除财务
def remove():
    id = input("请输入ID")
    sql='select * from finance where ID=%s'
    info=[id]
    if len(select(sql,info)) == 1: #调用select函数，并判断是否有值
        sql='delete from finance where ID=%s'
        info=[id]
        delete(sql,info) #调用delete函数，并删除内容
        return "删除财务成功！"
    else:
        return "ID号输入有误，删除财务失败"
# 查询财务
def inquire():
    print("1.查询所有   2.按条件查询")
    num=input("请输入查询条件（1-2）")
    while True:
        if num.isdigit():  # 判断输入的是否是数字
            num=int(num)  #num转换为数字类型
            if num==1:#查询所有
                sql='select * from finance'
                list=select(sql, [])
                # 输出查询的内容
                print("ID             ","类别             ","账户             ","金额             ","时间         ","说明             ")
                for i in range(len(list)):
                    for j in range(len(list[0])):
                        # print(list[i][j], end="\t\t")
                        ab=str(list[i][j])
                        print(ab.ljust(15," "),end="")
                    print()
                break
            elif num==2: #按条件查询
                start_time = input("请输入查询起始时间：")
                stop_time=input("请输入查询结束时间：")
                if start_time>stop_time:
                    print("时间输入有误")
                else:
                    sql='select * from finance where 时间>=%s and 时间 <=%s'
                    info=[start_time,stop_time]
                    list=select(sql,info)
                    # print("ID   ", "类别   ", "账户   ", "金额   ", "时间   ", "说明   ")
                    print("ID             ", "类别             ", "账户             ", "金额             ", "时间         ","说明             ")
                    for i in range(len(list)):
                        for j in range(len(list[0])):
                            ab=str(list[i][j])
                            # print(list[i][j], end="\t\t")
                            print(ab.ljust(15, " "), end="")
                        print()
                    break
            else :
                print("输入有误，请重新输入")
                num = input("请输入查询条件（1-2）")
        else:
            print("输入有误，请重新输入")
            num = input("请输入查询条件（1-2）")


while True:
    print("------------------管家婆家庭记账软件------------------")
    print('1.添加账务   2.编辑财务  3.删除财务  4.查询财务  5.退出系统')
    num = input('请输入要操作的功能需要[1-5]:')
    if num.isdigit():
        num = int(num)
        if num == 1:
            print(add())
        elif num == 2:
            print(revamp())
        elif num == 3:
            print(remove())
        elif num == 4:
            inquire()
        elif num == 5:
            print("退出系统成功")
            break
        else:
            print("输入有误，请重新输入")
    else:
        print("输入有误，请重新输入")
        num = input('请输入要操作的功能需要[1-5]:')