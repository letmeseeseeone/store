# 2.并将表格数据都存入到集团数据库中。
# 自己创建表

import xlwt
workbook = xlwt.Workbook(encoding='utf-8')
sheet1 = workbook.add_sheet("集团数据库")
workbook.save(r"D:\python\python学习\作业\集团数据库.xls")



# 1.统计和分析以下问题数据：
# a)统计表格中有多少人
import xlrd
wd=xlrd.open_workbook(r"D:\python\python学习\day8\百度数据分析\百度合作单位-人员管理-二期.xls",
                      encoding_override=True)
sheet=wd.sheet_by_index(0)
# print(type(sheet.nrows))           #<class 'int'>

num=sheet.nrows
print("共",num-1,"人")            #共 65534 人
sheet1.write(0,0,'表格中有多少人')
sheet1.write(0,1,num-1)


# b)统计办电信，联通，移动的用户数量（14,17开头为电信）（13开头为移动）（15开头为联通）

dian = 0
yi = 0
lian = 0


# for i in range(num):
#     if sheet.cell_value(i,5)[:2]=="14" or sheet.cell_value(i,5)[:2]=="17":
#         dian+=1
#     elif sheet.cell_value(i,5)[:2]=="13":
#         yi+=1
#     elif sheet.cell_value(i,5)[:2]=="15":
#         lian+=1
# print("电信用户数量为：",dian,"\n"                 #电信用户数量为： 6521
#       "移动的用户数为：",yi,"\n"                   #移动的用户数为： 22084
#       "联通的用户数为：",lian,"\n")                #联通的用户数为： 19483


for i in range(sheet.ncols):
    if sheet.col_values(i)[0]=="电话号码":
        for j in range(sheet.nrows):
            if sheet.cell_value(j,i)[:2]=="14" or sheet.cell_value(j,i)[:2]=="17":
                dian+=1
            elif sheet.cell_value(j,i)[:2]=="13":
                yi+=1
            elif sheet.cell_value(j,i)[:2]=="15":
                lian+=1
print("电信用户数量为：",dian,"\n"                 #电信用户数量为： 6521
      "移动的用户数为：",yi,"\n"                   #移动的用户数为： 22084
      "联通的用户数为：",lian,"\n")                #联通的用户数为： 19483
sheet1.write(1,0,'电信用户数量为')
sheet1.write(1,1,dian)
sheet1.write(2,0,"移动的用户数为")
sheet1.write(2,1,yi)
sheet1.write(3,0,'联通用户数量为')
sheet1.write(3,1,lian)

# c)总公司男女人数
wo=0
man=0
for m in range(sheet.ncols):
    if sheet.col_values(m)[0]=="性别":
        for n in range(sheet.nrows):
            if sheet.cell_value(n,m)=="女":
                wo+=1
            elif sheet.cell_value(n,m)=="男":
                man+=1
print("总公司男生共：",man,"\n"              #总公司男生共： 35665
      "总公司女生共：",wo,"\n")              #总公司女生共： 29869
sheet1.write(4,0,'总公司男生共')
sheet1.write(4,1,man)
sheet1.write(5,0,'总公司女生共')
sheet1.write(5,1,wo)

# d)年龄超过45岁的老员工人数

old_num=0
for a in range(sheet.ncols):
    if sheet.col_values(a)[0]=="年龄":
        for b in range(sheet.nrows):
            age = sheet.cell_value(b, a)
            if b>0:
                if age > 45.0:
                    old_num+=1
print("年龄超过45岁的老员工人数为：",old_num,"\n")              #年龄超过45岁的老员工人数为： 23859
sheet1.write(6,0,'年龄超过45岁的老员工人数为')
sheet1.write(6,1,old_num)

# e)薪资高于8000元的高薪人员数量和薪资低于3000的底薪人员数量

money_high=0
money_low=0
for c in range(sheet.ncols):
    if sheet.col_values(c)[0]=="薪资":
        for d in range(sheet.nrows):
            if d>0:
                if sheet.cell_value(d, c)>8000 :
                    money_high+=1
                elif sheet.cell_value(d, c)<3000:
                    money_low+=1
print("薪资高于8000元的高薪人员数量为",money_high,"\n"         #薪资高于8000元的高薪人员数量为 43859
      "薪资低于3000的底薪人员数量为",money_low,"\n")          #薪资低于3000的底薪人员数量为 3597

sheet1.write(7,0,'薪资高于8000元的高薪人员数量为')
sheet1.write(7,1,money_high)
sheet1.write(8,0,'薪资低于3000的底薪人员数量为')
sheet1.write(8,1,money_low)


# f)统计去传媒(有限)公司的工作的人员数量

company_num=0
for o in range(sheet.ncols):
    if sheet.col_values(o)[0]=="外包公司":
        for p in range(sheet.nrows):
            if "传媒有限公司" in sheet.cell_value(p, o):
                company_num+=1
print("去传媒(有限)公司的工作的人员数量:",company_num,"\n")             #16411
sheet1.write(9,0,'去传媒(有限)公司的工作的人员数量')
sheet1.write(9,1,company_num)

# g)统计一下可能在疫情高危地区的人数（高危地区：黑龙江，北京，福建，四川）

people_num=0
for x in range(sheet.ncols):
    if sheet.col_values(x)[0]=="居住地址":
        for y in range(sheet.nrows):
            if "黑龙江" in sheet.cell_value(y, x) or "北京" in sheet.cell_value(y, x) or "福建" in sheet.cell_value(y, x) or "四川" in sheet.cell_value(y, x) :
                people_num+=1
print("在疫情高危地区的人数:",people_num)           #在疫情高危地区的人数: 8683
sheet1.write(10,0,'在疫情高危地区的人数')
sheet1.write(10,1,people_num)



workbook.save('集团数据库.xls')
