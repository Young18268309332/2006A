# a=10
# b=20
# print(a+b)
# #python 里考缩进识别代码块，一个代码块是一个整体
# # def/class/lamde 这三种是内部创建内部销毁
#
# a = 1,2,3,4,5
# print(a)


# a,b,c = [1,2,3]   #这种是解包赋值
# print(a)
# print(b)
# print(c)
#
#
# a = 11324
# print (a//10)
#
# a //= 10
# print (a//10)
#
#
# #判定成绩表0-60不及格  60-70 及格  71-80 良好  81-100 优秀
# score = 76
# if (score > 0 and score < 60):
#     print("不及格")
# elif (score >= 60 and score <= 70 ):
#     print("及格")
# elif(score > 70 and score <= 80):
#     print("良好")
# else:
#     print("优秀")
#
# score_l = [23,45,67,89,35,65] #有可迭代对象的 用 for 循环
# for score in score_l:
#     if (score > 0 and score < 60):
#         print("不及格")
#     elif (score >= 60 and score <= 70 ):
#         print("及格")
#     elif(score > 70 and score <= 80):
#         print("良好")
#     else:
#         print("优秀")
#
#
# #求100以内的和 不包含100
# w = 0
# for i in range (100):
#     w = w + i
# print(w)
#
#
# #求出10*9*8..*1的积数之和   也叫10的阶乘
# i = 1
# for y in range (1,11):
#     i = i * y
# print(i)
#
#
#
# #猜数字第一种方法
# flag = True
# a = 58
# while flag:
#     b = int (input("请输入正确的数字"))
#     if(b > a ):
#         print("big")
#     elif(b < a ):
#         print("small")
#     else:
#         print("bingo")
#         flag =  False

#第二种方法

#
# a = 58
# while True:
    # b = int (input("请输入正确的数字"))
    # if(b > a ):
    #     print("big")
    # elif(b < a ):
    #     print("small")
    # else:
    #     print("bingo")
    #     break

#求出100以内能被3整除的数
# for i in range(1,100):
#     if(i % 3 != 0):
#         continue
#     print(i)

# #方法的定义，也叫封装
# def level(score):
#     if (score > 0 and score < 60):
#         print("不及格")
#     elif(score >= 60 and score <= 80):
#         print("及格")
#     else:
#         print("优秀")
# level(50)
# level(90)


#求两个数的商和余数
#方法1
# a = 10
# b = 2
# print("商:",a // b,",余数:",a % b)

#方法2
# def shang_yu(a,b):     #方法的定义   a,b 是形参
#     if (b == 0):
#         print("除数不能为0")
#     else:
#         print("商:", a // b, ",余数:", a % b)
#
# shang_yu(10,2)    #方法的调用  10，2 是实参  传参方式是按照位置传参
# shang_yu(89,6)
# shang_yu(89,0)

#做求和，不知道有多少参数，只要给到了就加一起，求最终的结果
#
# c = 1,2,3,4
# a,*b = (1,2,3,4)
# def sum1(name,*args,**kwargs):
#     print(**kwargs)
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum1(name='young'))


# a = 19   #全局变量
# def aaa():
#
#     global a  #局部变量
#     a = 12
#
# aaa()
# print(a)
#面向对象
# class calc():
#     a=None
#     b=None
#     res=None
#     def input (self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res=self.a+self.b
#     def div(self):
#         self.res=self.a/self.b
#     def get_result(self):
#         print(self.res)
# c=calc()  #类的实例化
#
# c.input(20,30)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()
#
# class calc():
#     res=None
#     def __init__(self,a,b):  # 构造方法 在类里，双下划线开头双下划线结尾叫魔法函数
#         self.a=a
#         self.b=b
#
#     def sum(self):
#         self.res=self.a+self.b
#     def div(self):
#         self.res=self.a/self.b
#
#     @classmethod  #类方法定义的要求：必须添加名字@classmethod的装饰器，第一个名字是cls cls代表当前类本身
#     def get_result(cls):
#         print(cls.res)
#
#
#     #静态方法定义，必须使用staticmetod装饰器，无默认参数
#     @staticmethod
#     def static():
#         print("我是静态方法")
# c=calc(19,40)  #如果想直接传参的话，可以用def_init_()
# c.sum()
# c.get_result()
#
# calc.static()    #直接通过方法调用

#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="\t")
#     print()

#冒泡排序
# l = [34,5,6,78,1,435,74,42,7568,7897,695,45]
# length = len(l)  #python的内置函数，固定写法
# for i in range(length-1,0,-1):   #遍历列表中的所有元素
#     for j in range (i):    #遍历列表中的下标
#         if (l[j]>l[j+1]):  #判断列表中的位置大小
#             l[j],l[j+1]=l[j+1],l[j]  #得出结论，如果前面的比后面的大，就交换位置
# print(l)

#封装   继承    多态

#封装
# class aaa():
#     pub_res = "公有变量"  #对外界开放的，可以随便修改的
#     _pri_res_ = "私有变量1" #表示类内部有特殊作用的，不能随便动的东西
#     __pri__res = "私有变量2"  #在print的时候不能自己出来，要手打出来 双下划线开始的，在外界无法访问
# #
#     #方法的公有和私有
#     def pub_function(self):
#         print("公有方法")
#     def _pri_function(self):
#         print("私有方法1")
#     def __pri_function(self):
#         print("私有方法2")
#
# print(aaa.pub_res )
# print(aaa._pri_res_)
# print(aaa.__pri_res)
# print(aaa().pub_function())
# print(aaa()._pri_function() )



#继承 是存在与python的面向对象类的继承里面
class Parent():
    money = 100000000
    house = 100

    def __init__(self,a):  #如果父类中实现了__init__的方法，子类中必须重写
        self.a=a

    __yi_wu = "kuzi"   #无法继承私有变量
    def skill(self):
        print("无限印钞机")

class Clild(Parent):
    ai_hao= "huaqian"
    def __init__(self,*args,**kwargs):   #子类重写了__init__方法
        super().__init__(*args,**kwargs)  #把接收到的数据原封不动地传给上面



    #如果不仅想继承父类的方法，还想自己创建个方法
    #调用父类的方法用super, 用法如下：
    def skill(self):
        super().skill()  #调用继承父类
        print(" 变废为宝") #自己再学的其他手艺

    def shou_yi(self):   #方法重写，称为多态
        print("分身术")

    pass
c=Clild(123)
print(c.ai_hao)
print(c.money)
print(c.house )
print(c.skill() )
c.shou_yi()
print(c.a)











