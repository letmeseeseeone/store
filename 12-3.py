# 定义一个学生类和对应的测试类
# 要求：
# 1、学生有姓名和年龄两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
# 2、提供一个无返回值的无参数的自我介绍的方法，内容打印一句话：
# “大家好，我叫xxx，今年xxx岁了！”
# 3、提供一个返回值为String类型，参数为学生类型的比较年龄差值的方法，如果当前对象的年龄比参数中的学生的年龄大，
#    则返回：“我比同桌大xxx岁！”；如果当前对象的年龄比参数中的学生的年龄小，则返回：“我比同桌小xxx岁！”；
#    如果当前对象的年龄和参数中的学生的年龄一样大，则返回：“我和同桌一样大！”
# 4、在测试类中分别创建你和你同桌两个人的对象，并分别给你和你同桌的姓名和年龄属性赋上对应的值；
# 5、调用你自己的对象的自我介绍的方法，展示出你自己的姓名和年龄；
# 6、用你自己的对象调用比较年龄差值的方法，把你同桌作为参数使用，并打印方法返回的字符串的内容；

class Student:
    __Name=""
    __Age=0

    def setName(self,Name):
        self.__Name = Name
    def getName(self,Name):
        return self.__Name

    def setAge(self,Age):
        self.__Age = Age
    def getAge(self,Age):
        return self.__Age

    def introduce(self):
        print("大家好，我叫",self.__Name,"，今年",self.__Age,"岁了！")

    def CompareAges(self,Name,Age):
        Age=20
        if Age == self.__Age:
            print("我和同桌",Name,"一样大！")
        else:
            flag=abs(Age-self.__Age)
            if Age > self.__Age:
                print("我比同桌",Name,"小",flag,"岁")
            else :
                print("我比同桌",Name,"大",flag,"岁")



class test:

      me = Student()
      me.setName("露露")
      me.setAge(22)
      me.introduce()
      me.CompareAges("小红",20)


