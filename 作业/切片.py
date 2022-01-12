# 容器 有增删改查
list_name=["a",2,3,"b",[5,6],"c",8,9,0]
# 角标       0  1 2  3    4    5  6 7 8
# 查：（通过角标来获取内容）
print(list_name[0])
print(list_name)
print(list_name[4][0])
print(list_name[-1])
print(list_name[:3])
print(list_name[3:])
print(list_name[-3:])
print(list_name[:-3])
print(list_name[1:5])          # [左闭右开)
print(list_name[5::-1])
print(list_name[:5:-1])
print(list_name[5::1])
print(list_name[:5:1])
