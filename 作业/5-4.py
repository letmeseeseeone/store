Friuts = {
    "苹果":12.3,  # 水果和单价
    "草莓":4.5,
    "香蕉":6.3,
    "葡萄":5.8,
    "橘子":6.4,
    "樱桃":15.8
}
info = {
    '小明': {'fruits': {'苹果':4, '草莓':13, '香蕉':10},'money':"??"},
    '小刚': {'fruits': {"葡萄":19, "橘子":12, "樱桃":30},'money': "??"}
}


# a=info['小明']['fruits']['苹果']
# print(a)
for j in info:
    sum=0
    for i in info[j]['fruits']:
        # print(i)
        sum+=Friuts[i]*info[j]['fruits'][i]
    info[j]['money']=sum
print(info)


