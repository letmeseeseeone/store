# 实现输入10个数字，并打印10个数的和
sum=0
n=10
while n>0:
    num=input(f"请输入第{n}位数字:")
    num=int(num)
    sum=sum+num
    n-=1#n=n-1
print("所有数字的和为：",format(sum))  #十个数字的和



