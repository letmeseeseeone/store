# i.定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
# 行为：学习（要求参数传入学习的时间），玩游戏（要求参数传入游戏名），
# 编程（要求参数传入写代码的行数），数的求和（要求参数用变长参数来做，返回求和结果）变长参数是字典和元组


class Student:
    Sno=''
    Name=''
    Age=''
    Sex=''
    Height=0.0
    Weight=0.0
    Grades=0.0
    Adress=""
    Tel=""

    def Study(self,time):
        print("学习了",time,"了！！")

    def PlayGame(self,name):
        print("在玩",name)

    def Programming(self,rows):
        print("写了",rows,"行代码")

    def Sum(self,*p):
        sum=0
        for i in range(0,len(p)):
            sum=sum+int(p[i])
        return sum
        print(sum)

a=Student()
a.Study(20)
a.PlayGame("王者")
a.Programming(152)
a.Sum(1,2,3,4,5,6,54)
# ii.车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。
# 功能：跑（要求参数传入车的具体功能，比如越野，赛车）
# 创建：法拉利，宝马，铃木，五菱，拖拉机对象
#
class cars:
    type=""
    num=4
    color=""
    weight=0.0
    rongji=0

    def run(self,name):
        print("一辆",name,"在路上")

b=cars()
b.run("法拉利")
b.run("宝马")
b.run("铃木")
b.run("五菱")
b.run("拖拉机")







# iii.笔记本：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。
# 行为：打游戏（传入游戏的名称）,办公。
#
class computer:
    type=''
    time=0.0
    color=""
    weight=0.0
    cputype=""
    GB=0.0

    def play(self,name):
        print("打游戏",name)
    def work(self):
        print("办公啊")

c=computer()
c.play("逃生1")
c.work()





# iv.猴子类：属性：类别，性别，身体颜色，体重。行为：造火（要求传入造火的材料：比如木棍还是石头），
# 学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）

class monkey:
    type=""
    sex=""
    color=""
    weight=0.0

    def Fire(self,materia):
        print("用",materia,"造火")
    def study(self,*name):
        print("学习",*name)


d=monkey()
d.Fire("木材")
d.study("写字","使用工具","打猎")

