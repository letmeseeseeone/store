# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
a = input("请输入一个数字")
a = int(a)
b = input("请输入两个数字")
b = int(b)
c = input("请输入三个数字")
c = int(c)
if a + b > c and a + c > b and b + c > a:
    # print("能够形成三角形")
    if  a == b and c == a and b == a:
        print("形成等边三角形")
    elif a == b or b == c or c == a:
        print("形成等腰三角形")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("形成直角三角形")
    else:
        print("形成普通三角形")
else:
    print("不能形成三角形")
