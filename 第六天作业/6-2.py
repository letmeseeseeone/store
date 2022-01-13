# 随机生成1000个整数;
# 数字范围[20,100];
# 输出所有不同的数字及其每个数字重复的次数,
# 有能力的话升序排序打印所有数字{“数字”:”次数”}

import random
a=[]
b=[]
n=0
while n<1000:
    n=n+1
    a.append(random.randint(20,30))

# for i in a:
#     num=0
#     for j in a:
#         if i==j:
#             num+=1
#     b.append([i,num])
#
# c=[]
# d=[]
# for x in b:
#     c.append(x)
#     if x not in d:
#         d.append(x)
# print(d)
# dict={}
# for i in d:
#     # dict[i[0]]=i[1]
# #     dict[键]=值
#     dict.update({i[0]:i[1]})
# print(dict)
#
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)