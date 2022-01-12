# 有下列人员数据库，请按要求实现
# # 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
# # 1.统计每个人的平均薪资
# sum1=0
# for i in names:
#     sum1=sum1+i[5]
#     ave= sum1 / len(names)
# print(ave)
#
# # 2.统计每个人的平均年龄
# sum=0
# for j in names:
#     sum=sum+int(j[1])
#     age=sum / len(names)
# print(age)
# # 3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
# names.append(["刘备","45","男","220","alibaba",500,"30"])
# print(names)
# # 4.统计公司男女人数
# sum2=0
# sum3=0
# for k in names:
#     if k[2]=="女":
#         sum2=sum2+1
#     else:
#         sum3+=1
# print("女生的人数是",sum2)
# print("男生的人数是",sum3)


# 5.每个部门的人数
# sum4=0
# sum5=0
# sum6=0
# for kl in names:
#     if kl[6]=="50":
#         sum4=sum4+1
#     elif kl[6]=="60":
#         sum5+=1
#     else:
#         sum6+=1
# print("50",sum4)
# print("60",sum5)
# print("10",sum6)
a=[]
for x in names:
    num=0
    for y in names:
        if x[-1]==y[-1]:
            num+=1
    a.append([x[-1],num])
print(a)
b=[]
c=[]
for i in a:
    b.append(i)
    if i not in c:
        c.append(i)
        print("ok")
print(b)
print(c)

# 50
# 1
# 60
# 2
# 60
# 2
# 10
# 1