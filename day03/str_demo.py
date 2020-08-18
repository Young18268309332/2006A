#字符串拼接
# a = "122"
# b = "4546"
# print(a+b)
# print(a)
# print(b)

#字符串截取
# a = "abcdefghijklmn"
# print(a[-1])  #倒序截取
# print(a[1])
# print(a[1:-3])  #冒号是表示结束的位置
# print(a[1:-2:2])  #2 是步长
# print(a[-1:0:-1])
# print(a[::-1]) #倒序截取整个字符串
# print(a[2:])
# print(a[:-2])

# a = "abcdefghijklmn"
# for i in a :
#     print(i)
#
# s = "    gxbhdy    "
# print(s.strip())  #去前后空格
# print(s.lstrip() )  #去左边空格
# print(s.rsplit() )  #去右边空格

# l = "dgagbbx,htsrhju,loogpobm"
# print(l.split(","))  #快速拆分开字符串
#
# s = "gajgagl/naafiio/nfjdkghidagh"  #换行符用错了，需要重新弄
# print(s.replace("/n","\n"))

#
# with open ("aaa.txt","r") as f:   #with 是上下文管理器
#     lines = f.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace("\n",""))  #在打印的时候把换行符去掉
#         print(i.replace("\n", ""),end="")  #不换行
#

#
# s="agdkgg.groigjg"
# print(s.find("."))  #找点的下标
#


#九九乘法表
# for i in range(1,10):
    # for j in range(1,i+1):
    #     # print(j,"X",i,"=",i*j,end="\t")
    #     print("%d X %d = %d"%(j,i,j*i),end="\t")  #字符串格式化
    # print()


#.format格式化
# for i in range(1,10):
#     for j in range(1,i+1):
#         # print(j,"X",i,"=",i*j,end="\t")
#         print("{} X {} = {}".format(j,i,j*i),end="\t")  #字符串格式化
#     print()
#
# print("{:,}".format(1000000000000))
# print("{:<10}".format("ahakk"))  #左对齐
# print("{:>10}".format("ahakk"))  #右对齐
# # print("{:＝10}".format(123))  #默认右对齐
# print("{:^10}".format(123)) #居中
# print("{:.2f}".format(2.3556578))  #取两位小数

# #列表修改
# l=[1,2,3,5,67,75,79]
# l[1]=20
# print(l)

# l = []
# # l[0]=20  #空列表不能截取 如果想截取空列表，可以用append
# l.append("翠花")  #可以往l里面添加   添加单个值append
# l.extend(('123',457))   #添加多个值用extend  跟可迭代的对象
# l=[1,2,3,4,5]
# l.insert(1,"翠花") #往里面插入数据 1是下表为1的
# print(l)
# #
# print(l.pop())  #默认删除最后一位
# print(l)
#
# print(l.pop(1))  #删除指定下表
# print(l)
#
# l.remove(2)  #不是根据下标删除数据，是根据数据内容删除数据  如果数据有重复的，会先删除最前边的
# print(l)
#
# l=[True,1,2,3,4,5]
# l.remove(1)  #把Ture删了是因为在python 里面 Ture相当于1的概念，而False是0 所以删布尔值的时候最好根据下标删
# print()
#
# l.clear()  #把整个列表的内容都删光
# print(l)




#字典的操作
# d={"name":"tom","age":18,"sex":"men"}  #把字典转化成元祖
# print(d.items())
# for k,v in d.items():  #遍历元祖里的数据就可以拿到key和value了
#     print(k,v)

# d["addr"]="上海松江"  #访问一个不存在的key,没有的话会自动添加  如果key存在就会修改原来的key
# print(d)
# d.update({"addr":"上海浦东","money":100000000})  #可以添加多个数据
# print(d)
#
# print(d.pop("addr"))  #对于字典来说不能直接删除里面不填数据，必须指定删除的key  如果key不存在，会报错
# print(d)
# print(d.clear()) #清空



#不要在遍历字典和列表的时候新增或者删除数据，会报错 ，如果想删，先创建个新的再赋值回来
# s={}
# for key in d:
#     if key.startswith("a"):
#         continue
#     s[key]=d[key]
# print(s)


#异常场景
# try:
#     f = open("bbb.txt","r")  #错误的格式
#     print(f.read())
#     f.close()
# except:
#     print("文件名不存在")  #用try和except就不会报错了
#

# def div(a,b):
#     try:
#         return a / b
#     except:
#         return
# print(div(10 ,0))


#自定义异常
class CustomException(Exception):
    def __init__(self,value="值不能为0"):  #设置默认值
        self.value = value
    def __str__(self):
        return self.value
print(Exception("fakjgdjgf"))

a=0
try:
    if a == 0:
        print("a = {} 触发异常".format(a))
        raise CustomException
    print("a = {} 未触发异常".format(a))
except CustomException as e:
    print(e)
