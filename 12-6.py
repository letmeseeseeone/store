# 人类：
# 属性:
# 姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，
# 手机最大待机时长，所拥有的积分。
# 行为：
# 发短信（要求参数传入短信内容）。
# 打电话（要求传入要打的电话号码和要打的时间长度。程序里判断号码是否为空或者本人的话费是否小于1元，
# 若为空或者小于1元则报相对应的错误信息，否则的话拨通。结束后，按照时间长度扣费并返回扣费
# （0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，其他：0.65元/钟、48个积分/钟））
import time


class book:

    book = {
            "1859633644841":"赵亮",
            "1357845614561":"拜登"}

    def catchkey(self):
        data = set(self.book)
        return data



class people:
    Name=''
    Sex=''
    Age=0
    PhoneWords=0.0  #话费：分钟
    PhoneBrand=''
    PoneBttery=0.0 #电池容量
    PhoneSize=0.0
    PhoneTime=0.0  #待机时间
    Integral=0.0   #积分
    Number=""      #Number是本人的号码
    PhoneNum=""     #PhoneNum是其他人的号码

    def intrduce(self):
        print("我的名字是",self.Name,"性别为",self.Sex,"年纪为",self.Age,
              "我的话费为",self.PhoneWords,"我的手机品牌为",self.PhoneBrand,"\n"
              "我的电池容量为",self.PoneBttery,"我的手机尺寸为",self.PhoneSize,
              "手机待机时间为",self.PhoneTime,"手机好的积分目前为",self.Integral)

    def Texing(self,con):
        print("发短信啦，内容是：",con)

    def Calling(self,Time):
        if self.PhoneWords > 1:
            if self.PhoneNum in book().catchkey():
                if self.PhoneNum != self.Number:
                    for i in range(8):
                        print(".", end="")
                        time.sleep(1)
                    print("通话成功！！！！",self.Number, "正在给", self.PhoneNum,
                    "( ",book().book[self.PhoneNum],")打电话。")
                    b.call(Time)
                else:print("与本人的号码相同？？？？")
            else:print("此号码是空号@@@@")
        else:
            print("您的话费余额不足一元￥￥￥￥￥")

    def call(self,time):
        if time>=0 and time<=10:
            self.PhoneWords = self.PhoneWords-time
            self.Integral = self.Integral + 15*time
        elif time>10 and time<=20:
            self.PhoneWords = self.PhoneWords - 0.8*time
            self.Integral = self.Integral + 39 * time
        else:
            self.PhoneWords = self.PhoneWords - 0.65*time
            self.Integral = self.Integral + 48 * time
        print("剩余话费为",self.PhoneWords)
        print("现在的积分为",self.Integral)

class Newpeople(people):
    address = ""
    voice = ""
    picture = ""
    mic = False

    def Called(self):
        # super(Newpeople, self).Calling(Time=10)
        print("本机号码归属地：",self.address, ",正在响铃：",self.voice)
        self.mic = True
        string = ""
        if self.mic == True:
            string = "开启"
        else:
            string = "关闭"
        print("对方头像为：", self.picture)
        print("(录音功能已", string, ")！")

# a=people()
b=Newpeople()
b.Name="小红"
b.Age=18
b.Sex="女"
b.PhoneWords=200
b.PhoneBrand="华为"
b.PoneBttery=30.0
b.PhoneSize=15.5
b.PhoneTime=30.5
b.Integral=20
b.Number="1859633644841"
b.PhoneNum="1357845614561"
# b.intrduce()
# b.Texing("哦哈哈")
b.Calling(50)
b.address = "北京移动 5G"
b.voice = "月亮之上"
b.picture = "野猪佩奇"
b.Called()
