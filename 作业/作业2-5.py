# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# Time。Sleep（）

# while True:
#     username=input("请输入用户名")
#     password=input("请输入密码")
#     if password == "admin" and username == "root":
#         print("输入成功")
#         break
#     else:
#         print("输入错误，请重新输入")
n=0
import time
while n<3:
    username=input("请输入用户名")
    password=input("请输入密码")
    if password != "admin" or username != "root":
        print("输入错误，请重新输入")
        n = n + 1
        if n==3:
            print("三次输入错误，请5s后再试")
            time.sleep(5)
            n=0
    else:
        print("输入成功")
        break









