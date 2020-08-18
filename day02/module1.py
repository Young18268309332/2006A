from day02.module2 import a as module_2_a


a="我是模块1中的a变量"
def name():
    print("我是模块1中的name方法")

class Test():
    name = "我是模块1中的Test类"

#只导入module_2_a但是打印了Test,name是因为from import语句会把导入的模块先执行一遍之后再导入当前的模块中
# print(module_2_a)

import os  #路径操作
import sys
import re  #执行正则表达式模块用的
import random #随机模块  生成随机数用的

print(os.listdir("."))  #显示给定目录下的所有文件，相当于linux中的ls
# print(os.path.exists())  #判断给定的路径是否存在
print(os.path.abspath("."))  #获取当前文件夹的绝对路径
print(os.path.dirname(os.path.abspath("module2.py")))   #返回的是文件夹的路径
print(os.path.join("e:\\workspace","python","2006A","__init__.py"))  #可以拼接路径
# print(os.system(""))  #执行cmd命令用的  可执行windows的命令和Linux的命令

r = re.compile("(\d+)")  #主要是编译正则表达式用的
res = r.findall("erjrga121324rhhyvgyjzf67578sdhh")
print(res)

print(random.randint (1,10))  #随机生成整数的
print(random.choice (['1','2','4','6','9']))  #随机取一位
print(random.choices(['1','2','3','4','5','6','7'],k=10))   #随机取多位数

print(random.choices("fgrgfyjhn",k=10)) #生成的是字符串，但是可以用join方法转成一串字符串
print("".join(random.choices("fgrgfyjhn",k=10))) #转成字符串


#第三方模块的概念
'''
不是自己写的
不是python解释器提供的
是第三方开发者提供的

先使用pip install  包名  安装  然后用from import的语法导入到当前模块
'''

