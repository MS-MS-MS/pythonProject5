# -*- coding: utf-8 -*-
"""
@Time    : 2021/5/15 16:03
@Author  : ms
@FileName: 问题记录.py
@SoftWare: PyCharm
"""

"""
————————————————————————————————————————str————————————————————————————————————————
"""
"""
str.isalpha()检测字符串是否含有字母, 存在返回True 不存在返回fales, 要保证没有 空格 标点符号 数字
"""
# str = "runoob";
# print(str.isalpha())
#
# str = "runoob菜鸟教程";
# print(str.isalpha())
#
# str = "this is string example....wow";
# print(str.isalpha())
#
# str = "runoob333";
# print(str.isalpha())

"""
str.isdigit() 判断字符是否含有数字  存在返回True  否则返回False
"""
# str="111111"
#
# print(str.isdigit())
# str="11111sss1"
# print(str.isdigit())

"""
str.upper() 字符串大写显示
"""
# str="python"
# print(str.upper())
"""
print(str.upper()) 字符串小写显示
"""
# print(str.upper())
# str1=str.upper()
# print(str1)
# print(str.lower())
"""
str.capitalize()  字符串第一个字母大写显示 
"""
# str="python p"
# print(str.capitalize())
"""
str.title() 字符串每个每个单词的首字母大写
"""
# str="python pycharm"
# print(str.title())

"""
str.replace(old,new,max)   
old 要替换的字符串  
new 新的字符串
max  替换的最大次数  
新的字符串不会改变原有的字符串 
"""
# str ="python pycharm"
# print(str.replace("py", "sa",1))
# print(str)
"""
str.strip()
删除字符串指定头尾的元素 ，默认删除\n,\t 空格  不能删除字符的中间 元素
"""
# str="python pycharm\n"
# str1="python pycharm\t"
# str2="python pycharm/t"
#
# print(str.strip())
# print(str1.strip())
# print(str2.strip("on"))

"""
str.rstrip() 删除字符串末尾的元素，默认删除是空格 
如果字符串结尾以空格 \n ,\t 结尾 默认只删除这些元素 对指定的元素不做删除
"""
# str="python pycharm"
# strsx="python pycharm\n"
# # str1="python pycharm\t"
# # str2="python pycharm/t"
#
# print(strsx.rstrip("arm"))
# # print(str.lstrip("py"))


"""
str.lstrip() 截取字符串左边的空格 或者指定字符 
如指定一个5 截取后 左边的5全部删除 
有默认的参数 指截取默认的参数
"""
# str=" 5  55python pycharm"
# strsx="python pycharm\n"
# str1="python pycharm\t"
# str2="/tpython pycharm/t"
# print(str2.lstrip())


"""

字符串索引的问题
index（）   判断子字符串是否在指定字符串之中，若存在 输出子字符串在指定字符串的位置  不存在报错提示
str -- 指定检索的子字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。

find()     判断子字符串是否在指定字符串之中，若存在 输出0 不存在输出-1 
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。

index() 适用与列表 可以判断指定的元素 是否在列表中
"""
#
# a_list = ['a','b','c','hello']
# print(a_list.index('a'))
# print(a_list.index('a',0,1))
#
# str1='python is on the way'
# str2='on'
# #空格，等其他操作符对其索引位置也有影响
# #在str1中检测字符串中是否含有子字符串str2  str1.index(str2,beg=0,end=len(str1))
#
# #如果包含子字符串 返回检测到的索引值
# print(str1.index(str2))
#
# #从索引1开始检测，检测长度为3
# print(str1.index(str2,1,3))
#
#
# str1='python is on the way'
#
# str2='on'
# str3='nice'
#
# print(str1.index(str2))
#
# #不在字符串str1中
# print(str1.find(str3))
#
# #从索引1开始检测，检测长度为3
# print(str1.find(str2,1,3))


"""
"----------------------------------------------------list-------------------------------------------"
"""
"""
列表删除
list.pop() 返回被删除的值  默认删除最后一个 可指定元素删除
list.remove["a"] 删除列表中的元素
del list(0) 按照索引删除 从0 开始 

"""
# lists=list(range(0,5))
# # print(lists.pop())
# print(lists.pop(1))
# print(lists)
#
# lists=[1,2,3,5,4,5,6]
# del (lists[5])
# print(lists)
#
# lists=[1,2,3,5,4,5,6]
# lists.remove(lists[5])
# print(lists)
#
#
# a=[1,2,3,5,4,5,6]
# a.remove(a[5])
# print(a)
#
# # [1, 3, 5, 4, 2, 6]
# # 说明 remove 移除的是列表中元素的位置。
#
# a=[1,2,3,5,4,2,6]
# del(a[5])
# print(a)
# #  a
# # [1, 2, 3, 5, 4, 6]

"""
判断元素是否在列表内
in   x in list
not in 判断元素不在列表内
"""

"""
lists.extend 合并列表数据
"""
# lists=[1,2]
# lists1=[3,4]
# lists.extend(lists1)
# print(lists)

"""
list.count(1) 记录元素在列表出现的次数
"""
# lists=[1,2,3]
# print(lists.count(1))
# print(lists.count(max(lists)))


"""
——————————————————————————————————————————————切片——————————————————————————
#  切边的操作 用于分隔三个参数（start_index、end_index、step） 中间用：隔开
#  start_index 与step 的符号要一致 同正 同负  正 从左向右   是从0开始   负号 从右向左 从1开始\
# 要取结尾的字符 使用 [-3:]
# [3:] 从左往右  从三开始全
# lst[:-4] 从 -5开始取值
"""
"""
isinstance()  与type 区别  无法判断子类（继承类）的归属问题  
class My_int(int):
    pass
my_int=My_int() 申明一个实例  继承这个类
type  不能判断出实力的类型  <class '__main__.My_int'>
isinstance  可以判断出 类型   True
"""

"""
排序
sort 只对列表的内容排序 不会生产 新的列表  使用时用list.sort()调用   
print(list.sort()) 返回值是none 函数就地改动  

sorted  产生新的列表   使用时sorted(list)   
sorted  可以对字典进行排序  默认是对key进行排序 

按照 value  补 

sotr 与sotred 都有 reverse 参数  默认false 升序  True降序 


reverse 
反序显示  
list.reverse() 
print(list) 
反序显示 要打印显示  直接打印函数返回 none   应为进行了原地的改动 

"""

"""
-----------------------------元组————————————————————————————————————
只有一个元素时，元组必须有","逗号  eg a=(1,)
"""
# a=(1,)
# print(type(a))

"""
for 循环

补一个 双重for循环 用计数控制的方式
"""
# 双重for循环 可以列表表达式代替
#
# for user in new_users:
#     if user.lower() in [current_user.lower() for current_user in current_users]:
#         print('该用户名已被使用，请输入别的用户名')
#     else:
#         print('该用户名未被使用')


"""
———————————————————————————字典Dict————————————————————————————————————————————————————————
"""
"""
dict.items() 
以列表返回可遍历的(键, 值) 元组数组
dict_items([('Google', 'www.google.com'), ('Runoob', 'www.runoob.com'), ('taobao', 'www.taobao.com')])
"""
# # dict.items()
# dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
#
# print ("字典值 : %s" %  dict.items())
#
# # 遍历字典列表
# for key, values in dict.items():
#     print(key, values)

"""
———————————————————————————while循环————————————————————————————————————————————————————————

"""
# # 默认
# while True:
#     pass
#
# # 参数
# number=0
# while number<=5:
#     print(number)
#     number+=1
# # 设置一个标志，
# activity=True
# while activity:
#     print(number)
#     number += 1
#     if number>5:
#         activity=False
#
# # 通常用于统计问卷  控制标准来结束循环
# citydict={}
# activity=True
# while activity:
# 	print("If you could visit one placein the world, where would you go?")
# 	names=input("names:")
# 	city=input("city:")
# 	# print(city)
# 	citydict[names]=city
# 	res=input("yes or no")
# 	if res=="no":
# 		activity=False
# print("----------------------------------------------------------------")
# for names ,city in citydict.items():
# 	print(names,city)

# 删除列表中重复的记录
# pets=["cat","dog","cat","cat","monkey"]
# while "cat" in pets:
#     pets.remove("cat")
#
# print(pets)

"""
———————————————————————————函数————————————————————————————————————————————————————————
funcname(【位置实参】,【关键字实参】)
"""

"""
形参 和实参
形参在定义函数时 创建的参数
实参 时在函数调用时传递给函数的值 ,形参用于结束实参
"""
# def canshu(xingcan):
#     print(xingcan)
# canshu(shican)

"""
可变参数
传递的是元组
关键字参数
字典
"""
# def func1(*op):
#     pass
#
# def func2(**user_info):
#     pass
#
# func1('a','b','c')
# func1('a')
#
# func2(a='a',b='b')
#
#
# def func2(a,b=1,*op,**user_info):
#     print(a)
#     print(b)
#     print(op)
#     print(user_info)
#     pass
# ops=('a','b','c')
#
# func1('1',ops)
#
#
#
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# f1(1, 2)
# # a = 1 b = 2 c = 0 args = () kw = {}
# f1(1, 2, c=3)
# # a = 1 b = 2 c = 3 args = () kw = {}
# f1(1, 2, 3, 'a', 'b')
# # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# f1(1, 2, 3, 'a', 'b', x=99)
# # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
# f2(1, 2, d=99, ext=None)
# # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
#
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
"""
________________________________ IF________________________
"""
# s="d"
# if s: #表达式 if s: == if s!="":
#     print("s")
# else:
#     print("sssss")

"""
—————————————————————————————————————————继承————————————————————————————————
"""
# 在类里面定义列表，在类外面赋值

"""
——————————————————————————————————————文件————————————————————————————————————————————
"""
# 文件的读取
# fliename = "learning_python.txt"
# with open(fliename) as obj:
#     # 读取全部文件
#     note = obj.read()
#     print(note.rstrip())
#     # 读取一行文件
#     note1 = obj.readline()
#     print(note1)
#
# with open(fliename) as obj:
#     # 读取一行文件
#     note1 = obj.readline()
#     print(note1)
#
# with open(fliename) as obj:
#     # 读取读取全部的文件已列表的形式返回
#     note2 = obj.readlines()
#     # print(note2)
#     for i in note2:
#         # i.rstrip() 删除每行末尾的空格字符
#         print(i.rstrip())

"""
r 只读模式 文件必须先存在
"""

# fliename="learning_python.txt"
# with open(fliename) as obj:
#       # 不写默认 R 只读模式
#       note=obj.read()
#       print(note.rstrip())

"""
r+
先读在写 文件必须先存在
打开文件后，既可以从头读取文件内容，也可以从开头向文件中写入新的内容，写入的新内容会覆盖文件中等长度的原有内容。
"""
# fliename="learning_python.txt"
# with open(fliename,'r+') as obj:
#       note=obj.read()
#       print(note.rstrip())
#       obj.write("In Python you can "+"\n")

"""
写入模式 w 不可读取文件	
打开一个文件只用于写入。如果该文件已存在则打开文件，
并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
"""
# fliename="learning_python1.txt"
# with open(fliename,'w') as obj:
#       #不可读
#       obj.write("c")

"""
W+ 可写 可读 先写在读 
先读在写文件会先被创建 文件为空
打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
obj.seek(0)
"""

# fliename="learning_python1.txt"
# with open(fliename,'w+') as obj:
#       obj.write("c++")
#       obj.seek(0)
#       r=obj.read()
#       print(r)

"""
a
写
不清空文件，在文件的末尾追加写 ，不可读
"""
# fliename="learning_python1.txt"
# with open(fliename,'a') as obj:
#       obj.write("java"+"\n")

"""
a+
追加写 读
不清空文件，在文件的末尾追加写 
obj.seek(0)
"""

# fliename="learning_python1.txt"
# with open(fliename,'a+') as obj:
#         obj.seek(0)
#         r = obj.read()
#         print(r)
#         obj.write("举办sx"+"\n")

"""
读取文件 ——绝对路径
开头要 r转义符开头 转义\
"""
# data=r"D:\path_file\file.txt"
# date=r"C:\Users\Administrator\PycharmProjects\pythonProject3\s\ss.txt"
# with open(date)as obj:
#     r=obj.read()
#     print(r)

"""
读取文件——相对路径
.py 文件和读取的文件在同一文件夹下
"""
# date="s\ss.txt"
# with open(date)as obj:
#     r=obj.read()
#     print(r)


"""
方法split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。为计算
Alicein Wonderland 包含多少个单词，

"""
# try:
#     with open(book) as book_obj:
#         books=book_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + book + " does not exist."
#     print(msg)
# else:
#     # 将文件已空格的为分隔符的形式隔开，并返回一个列表
#     world=books.split()
#     print(world)
#     # 打印列表的长度，读取出文件一含有多少的单词
#     num_worlds=len(world)
#
#     print(num_worlds)

"""
文件的存储

"""

"""
断言
"""

# 方法 用途
# 核实a == b
# assertEqual(a, b)
# # 核实a != b
# assertNotEqual(a, b)
# # 核实x 为True
# assertTrue(x)
# # 核实x 为False
# assertFalse(x)
# #  核实 item 在 list 中
# assertIn(item, list)
# # 核实 item 不在 list 中
# assertNotIn(item, list)

