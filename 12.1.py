# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class PerComputer:
    ScreenSize=0.0
    Price=0
    CpuType='默认'
    MemorySize=0
    Time=0

    def Typing(self,DocName,PerName,hour):
        print(PerName,"已经给",DocName,"打字",hour,"小时了！！！")
        print("电脑屏幕",self.ScreenSize,"是英寸的，价格是",self.Price,"元，cpu型号是",self.CpuType,
              "，内存大小是",self.MemorySize,"GB，待机时长是",self.Time,"小时？？")

    def PlayGame(self,PerName,GameName,hour):
        print(PerName,"在",self.ScreenSize,"英寸的电脑屏幕上玩",GameName,"已经",hour,"小时了！！")

    def WatchVideo(self,PerName,VideoName,hour):
        print(PerName,"在",self.ScreenSize,"英寸的电脑屏幕上看",VideoName,"已经",hour,"小时了！！")

p=PerComputer()
p.ScreenSize=14.4
p.Price=5400
p.CpuType="intel"
p.MemorySize=800
p.Time=20
p.Typing("测试文档","小明",2)
p.PlayGame("小红","纸人",5)
p.WatchVideo("露露","家有喜事",1)