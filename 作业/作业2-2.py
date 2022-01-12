# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
n=10
sum=0
# flag=0
c=0
while n>0:
    num = input(f"请输入第{n}位数")
    num=int(num)
    if num>c:
        c=num
    # if num>flag:
    #     flag=num
    sum=sum+num
    n=n-1# n-=1
if n==0:
    avg=sum/10
    # print(sum,int(avg))
    print(sum, int(sum/10),flag)