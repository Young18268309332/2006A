#
# #把字符串转成数字
# a=123
# b="456"
# print(a + int(b))
#
# #把数字转成字符串
# print(str(a)+b)
#
# #把字符串转成列表
# print(list(b))
# #元祖转列表
# t = (1,2,3,4)
# print(list(t))
# #列表转元祖
# l = [1,43,56,35,4]
# #列表转集合
# print(tuple(l))
# print(set(l))

#总结：字符串，列表，集合，元祖都可以互转

#print()是一种输出方式

#打开模式：r 读取   w 清空写入   a 追加写入  b 二进制模式
#写入
# f = open("aaa.txt",'w')  #open后面跟文件名＋打开方式
# f.write("hello kitty")  #输出  这是第二中输出方式   write 后跟字符串
# f.write("fartag\ndsdhnn\nfgfbxffhs\nfegxbcbadhtr")  #\n是换行的意思
# f.writelines(["","","",""])  #writelines后跟列表
# print(f.writable())#如果不确定当前文件是以读取方式打开的还是以写入的方式打开的，可用writable确认是否可写一下
# f.close



#读取
f = open("aaa.txt",'r')
# print(f.read())  #默认读取全部字符，也可以指定读取多少个字符
# print(f.readable()) #确认是否可读
print(f.readline() )  #按行读取，读取一行
print(f.readlines())  #按行读取，读取全部行
f.close()
