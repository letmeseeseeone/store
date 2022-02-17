# 人类：
# 属性:
# 姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，
# 手机最大待机时长，所拥有的积分。
# 行为：
# 发短信（要求参数传入短信内容）。
# 打电话（要求传入要打的电话号码和要打的时间长度。程序里判断号码是否为空或者本人的话费是否小于1元，
# 若为空或者小于1元则报相对应的错误信息，否则的话拨通。结束后，按照时间长度扣费并返回扣费
# （0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，其他：0.65元/钟、48个积分/钟））

pn=["123456789","111111111","222222222"]
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

    def Texing(self,con):
        print("发短信啦，内容是：",con)

    def Calling(self,Number,PhoneNum,time):#Number是本人的号码，PhoneNum是其他人的号码
        if self.PhoneWords > 1:
            if PhoneNum  in pn:
                if PhoneNum != Number:
                    print("通话成功！！！！")
                    a.call(time)
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


a=people()
a.Name="小红"
a.Age=18
a.Sex="女"
a.PhoneWords=20
a.PhoneBrand="华为"
a.PoneBttery=30.0
a.PhoneSize=15.5
a.PhoneTime=30.5
a.Integral=20
a.Texing("哦哈哈")
a.Calling("222222222","111111111",10)
