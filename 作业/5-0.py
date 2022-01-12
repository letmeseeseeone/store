# a=[1,2,1,2,3,4,5,1,2,3]
# for i in a:
#     print(i,a.count(i))
# #
dict_name1={"键1":"值","键":"123"}
dict_name={"键1":"值","键": {"键":"值","键":"123"}}
# # print(dict_name)
# # print(dict_name1)
# # print(dict_name["键"])
# # print(dict_name["键"]["键"])

# # 增加（更新） update
# dict_name.update({"姓名":"杀毒"})
# print(dict_name)
# # 如果键存在 更新值；
# dict_name["键"]="789"
# print(dict_name)


# # 删除（弹出） pop
# print(dict_name.pop("键1"))
# dict_name.pop("键")
# print(dict_name)
#

#
# 删除  popitem  生成一对元组可以赋值
a={}
a=dict_name1.popitem()
print(a)

