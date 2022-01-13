# 输出商品列表，用户输入序号，显示用户选中的商品
# 商品列表：
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "显示器", "price": 120},
         {"name": "内存", "price": 230}, ]
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如
        # 1 电脑 1999
        # 2 鼠标 10
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入
# 4：用户输入Q或者q，退出程序

print("序号","","商品名称","  ","价格\n"
      "1","  ","电脑","      ","1999","元\n""2","  ","鼠标","      ","10","元\n"
      "3","  ","显示器","    ","120","元\n""4","  ","内存","      ","230","元\n")

dict={}
num=0
for i in goods:
    num+=1
    dict[num]={i["name"]:i["price"]}

while True:
    n=input("请输入您要选中的商品序号")
    if n.isdigit():
        n=int(n)
        if n in dict:
            print(n)
            print(dict[n])
        else:
            print("您输入的商品序号有误,请重新输入")
            continue
    else:
        if n=="q" or n=="Q":
            break
        else:
            print("您输入的商品序号有误,请重新输入")
            continue




#

