# from day02 import module1
# from day02.module1 import a as module_1_a,name as module_1_name,Test as module_1_Test   #为了不重名，可以取别名

# print(a)
# name()
# print(Test.name )


a="我是模块2中的a变量"
def name():
    print("我是模块2中的name方法")

class Test():
    name = "我是模块2中的Test类"

# #取别名后用就不会报错
if __name__ == "__main__":  #如果不想把这些都导入module1里面的话，可以用main方法
    name()
    print(Test.name )