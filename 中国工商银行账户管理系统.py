# 账号
# users={账号:{姓名:是的，密码：123456，地址：幸福大街，存款余额：100，开户行：中国工商银行})
import random
# 界面
print("*"*30,"\n""*"," "*6,"中国工商银行"," "*9,"*")
print("*"," "*6,"账户账户系统"," "*9,"*")
print("*"," "*9,"V 1.0"," "*11,"*")
print("*"*30)
print("*","1.开户"," "*20,"*")
print("*","2.存钱"," "*20,"*")
print("*","3.取钱"," "*20,"*")
print("*","4.转账"," "*20,"*")
print("*","5.查询"," "*20,"*")
print("*","6.Bye！"," "*19,"*")
print("*"*30)
bank_name="工商银行**分行"
userinfo={}
# userinfo={11111111:
#               {'username': 'sss', 'password':"123456", 'country': 'dd',
#                'province': 'dd', 'street': 'd', 'door': 'dd', 'money':500,
#                'bank_name': '工商银行**分行'},
#           22222222:
#               {'username': 'sss', 'password': 123456, 'country': 'dd',
#                'province': 'dd', 'street': 'd', 'door': 'dd', 'money': 700,
#                'bank_name': '工商银行**分行'}
#           }
# 构造函数：
def useradd():
    account=random.randint(10000000,100000000)
    # account=int(input("请输入您的账号"))
    username=input("请输入您的姓名")
    password=input("请输入您的密码")
    country=input("\t请输入您的国家")
    province=input("\t请输入您的省份")
    street=input("\t请输入您的街道")
    door=input("\t请输入您的门牌号")
    flag=bandadd(account,username,password,country,province,street,door)
    if flag==1:
        print("添加成功")
        print(userinfo)
    elif flag==2:
        print("该用户已存在，添加失败")
    elif flag==3:
        print("用户库已满，添加失败")


def bandadd(account,username,password,country,province,street,door):
    if len(userinfo) == 100:
        return 3
    # if userinfo.key==username:  错误，不是等于，而是要这个账号存在于数据库中
    elif account in userinfo.keys():
        return 2
    else:
        userinfo[account] = {
           "username":username,
           "password":password,
           "country":country,
           "province":province,
           "street":street,
           "door":door,
           "money":0,
           "bank_name":bank_name
        }
        return 1



def addmoney():
    add_account=int(input("请输入您的账号"))#输入的账号为字符串
    add_money=input("请输入您要存钱的金额")
    flag1=check_addmony(add_account)
    if flag1==True:
        userinfo[add_account]["money"]=int(add_money)+userinfo[add_account]["money"]
        print("成功存入，您现在的金额为：",userinfo[add_account]["money"])
    elif flag1==False:
        print("您的账户有误")


def check_addmony(add_account):
    if add_account in userinfo:
        return True
    else:
        return False


def reduce_money():
    re_account=int(input("请输入您要取钱的账号"))
    re_password=input("请输入您的密码")
    re_money=int(input("请输入您要取钱的金额"))
    flag2=check_re_money(re_account,re_password,re_money)
    if flag2 == 1:
        print("您输入的账号不存在")
    elif flag2 == 2:
        print("您输入的密码有误")
    elif flag2 == 3:
        print("您输入的金额大于账户余额")
    elif flag2 == 0:
        userinfo[re_account]["money"]=userinfo[re_account]["money"]-re_money
        print("您已成功取钱，您的账户余额为",userinfo[re_account]["money"])


def check_re_money(re_account,re_password,re_money):
    if re_account in userinfo:
        if re_password == userinfo[re_account]["password"]:
            if re_money <= userinfo[re_account]["money"]:
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


def trans_money():
    tra_out_account=int(input("请输入您要转出的账号"))
    tra_in_account=int(input("请输入您要转入的账号"))
    trs_out_password=input("请输入您要转出账号的密码")
    trs_out_money=int(input("请输入您要转账的金额"))
    flag3=check_tra_money(tra_out_account,tra_in_account,trs_out_password,trs_out_money)
    if flag3 == 0:
        userinfo[tra_out_account]["money"]=userinfo[tra_out_account]["money"]-trs_out_money
        userinfo[tra_in_account]["money"]=userinfo[tra_in_account]["money"]+trs_out_money
        print("成功转账")
        print("转出账户余额为：",userinfo[tra_out_account]["money"])
        print("转入账户余额为：",userinfo[tra_in_account]["money"])
    elif flag3 == 1:
        print("您输入的账号有误")
    elif flag3 == 2:
        print("您输入的密码有误")
    elif flag3 == 3:
        print("您转出的金额大于您的账户余额")


def check_tra_money(tra_out_account,tra_in_account,trs_out_password,trs_out_money):
    if tra_out_account in userinfo.keys() and tra_in_account in userinfo.keys():
        if trs_out_password == userinfo[tra_out_account]["password"]:
            if trs_out_money <= userinfo[tra_out_account]["money"]:
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


def check_account():
    che_acc_account=int(input("请输入您的账号"))
    che_acc_password=input("请输入您的密码")
    check_che_acc(che_acc_account, che_acc_password)

def check_che_acc(che_acc_account,che_acc_password):
    if che_acc_account in userinfo.keys():
        if che_acc_password == userinfo[che_acc_account]["password"]:
            print("ok")
            print("当前账号：",che_acc_account,"，余额：",userinfo[che_acc_account]["money"],"，用户居住地址：",
                  userinfo[che_acc_account]["country"],
            userinfo[che_acc_account]["province"],
            userinfo[che_acc_account]["street"],
            userinfo[che_acc_account]["door"],
            "当前账户的开户行：",userinfo[che_acc_account]["bank_name"])
        else:
            print("密码错误")
    else:
        print("该用户不存在")




while True:

    num=input("请输入您要办理业务的编号")
    if num=="1":
        print("开户")
        useradd()

    elif num=="2":
        print("存钱")
        addmoney()
    elif num=="3":
        print("取钱")
        reduce_money()
    elif num=="4":
        print("转账")
        trans_money()
    elif num=="5":
        check_account()
    elif num=="6":
        print("成功退出系统")
        break
    else:
        print("您输入的信息有误，请重新输入！")