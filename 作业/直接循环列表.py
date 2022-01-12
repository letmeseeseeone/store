a=[1,5,2,1,4,6,3,2,1,4,5,45]
# 循环一个列表，判断列表中每个元素是否在另一个列表中粗壮乃，若不存在则添加
b=[]
c=[]
for i in a:#循环列表的内容
    c.append(i)
    if i not in b:#如果元素i不再b这个列表中的话
        b.append(i)#添加进列表
print(b)
print(c)