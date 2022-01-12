# 小明去超市购买水果，账单如下
# 苹果  32.8
# 香蕉  22
# 葡萄  15.5
# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
# 用水果名称做key，金额做value，创建一个字典
info = {
    '苹果':32.8,
    '香蕉': 22,
    '葡萄': 15.5
}
while 1:
    # print(info)
    # fruit=input("请输入您要查询的水果名称")
    for i in info:
        if i==input("请输入您要查询的水果名称"):
            print(info[i])
        else:
            break
