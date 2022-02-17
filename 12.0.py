# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体

class cup:
    __high = 0
    __volume = 0.0
    __color = ''
    __Material = ''

    def sethigh(self,high):
        if high>30 or high<0:
            print("您输入的高度有误！！！！！")
        else:
            self.__high=high
    def gethigh(self,high):
        return self.__high


    def setvolume(self,volume):
        if volume>5000 or volume<0:
            print("您输入的容积有误？？？？？")
        else:
            self.__volume=volume
    def getvolume(self,volume):
        return self.__volume


    def setcolor(self,color):
        print("很棒，颜色输入正确*******")
        self.__color=color
    def getcolor(self,color):
        return self.__color

    def setMaterial(self,Material):
        print("很棒，材料输入正确@@@@@@")
        self.__Material=Material
    def getMaterial(self,Material):
        return self.__Material



    def StoreLiquids(self,liquidName):
        print("一个颜色是：",self.__color,"材质是",self.__Material,"高度是",self.__high,"厘米的水杯中，盛放了",
              self.__volume,"毫升的",liquidName)

c=cup()

c.setcolor("粉色的")
c.sethigh(90)
c.setvolume(90000)
c.setMaterial("不锈钢")
c.StoreLiquids("可乐")
