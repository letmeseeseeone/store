car=[]  #购物小票
shop=[
    ["辣条","5"],
    ["牛奶","40"],
    ["海绵","3"],
    ["饮料","3"]
]
for i in enumerate(shop):
    print(i)
a=input("请输入您要找的商品")
a=int(a)
print(shop[a])
car.append(shop[a])
print(car)
