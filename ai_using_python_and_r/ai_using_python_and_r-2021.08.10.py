"""
file     : AI使用Python與R語言.py
author   : Ming-Chang Lee
date     : 2021.8.10
email    : alan9956@gmail.com
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Encoding : UTF-8
"""

# Python: https://github.com/rwepa/DataDemo/blob/master/ai_using_python_and_r/ai_using_python_and_r-2021.08.10.py
# R: https://github.com/rwepa/DataDemo/blob/master/ai_using_python_and_r/ai_using_python_and_r-2021.08.10.R

# 大綱
# 8/10(二) 01.Python與Anaconda簡介,資料型別與運算子
# 8/11(三) 02.Python資料物件,使用NumPy模組與reshape應用
# 8/12(四) 03.字串與正規表示式,判斷式與函數應用
# 8/13(五) 04.日期時間資料,檔案匯入pandas
# 8/27(五) 05.MySQL與SQL語法,Python連結MySQL應用

# R 入門資料分析與視覺化應用(7小時28分鐘)
# https://mastertalks.tw/products/r?ref=MCLEE

# R 商業預測應用(8小時53分鐘)
# https://mastertalks.tw/products/r-2?ref=MCLEE

##############################
# 8/10(二) 01.Python與Anaconda簡介,資料型別與運算子
##############################

##############################
# 資料分析架構APC方法
##############################
# 1.群組
# 2.時間
# 3.建立評估變數

##############################
# CRISP-DM 跨產業資料探勘標準作業流程
##############################
# https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining

# 數值模型績效指標
# 均方誤差 (Mean Squared Error, MSE)
# 均方根誤差 (Root Mean Squared Error, RMSE)
# 平均絕對誤差 (Mean Absolute Error, MAE)

# 類別模型績效指標
# http://rwepa.blogspot.com/2013/01/rocr-roc-curve.html

##############################
# Python 簡介與安裝
##############################
# https://www.python.org/ 

# Anaconda 簡介與安裝
# https://www.anaconda.com/

# 實作練習1
# 在 jupyter notebook 輸入以下程式碼練習
from numpy import *
random.rand(5,5)

# jupyter notebook – 更改預設目錄
# cd C:\
# jupyter-notebook

# 實作練習2
# 開啟下列 ipynb 檔案
# Python 程式設計-李明昌 <免費電子書>
# http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html

# 使用命令提示列 開啟 Orange
# python -m Orange.canvas

# 顯示已安裝模組
# conda list

# 尋找官網套件
# conda search matplotlib

# 安裝模組
# conda install 模組名稱

# 更新模組
# conda update 模組名稱

# Spyder 更新
# 步驟1.Anaconda 整體更新
# conda update anaconda

# 步驟2.Spyder 更新
# conda update spyder

# 實作練習3
# 熟悉自動換列等設定
# Tools \ Preferences \ Editor \ Display \ Wrap lines

# 恭喜您, 開啟人生的 Python 學習之旅 ^_^

# Python 執行-命令提示列
# 建立 C:\mydata\helloworld.py

# cd C:\mydata
# python --version
# dir
# python helloworld.py

# 合法變數
大數據 = 1 # 中文亦可,建議不要使用
CustomerSaleReport = 1
_CustomerSaleReport = 1
Customer_Sale_Report = 1
customer_sale_report = 1

# 不合法變數
$CustomerSaleReport = 1 # SyntaxError: invalid syntax
2020_sale = 100 # SyntaxError: invalid decimal literal
break = 123 # SyntaxError: invalid syntax

# 內建保留字
dir(__builtins__)
len(dir(__builtins__)) # 159

# 指派多個變數
x, y, z = "台北", "台中", "高雄"
print(x,y,z)
type(x) # str

address = ["台北", "台中", "高雄"]
x, y, z = address
print(x)
print(y)
print(z)

# Python Style Rules
# https://google.github.io/styleguide/pyguide.html

# Python 註解
# 使用一個 #	   用於1行註解
# 使用二個 """  用於超過1行註解或函數之說明文件

# 內縮4個空白鍵之語法

# 資料型別
# https://docs.python.org/3/library/stdtypes.html
# 參考: https://www.w3schools.com/python/  

# 資料型態 – 範例

# 整數 int
x1 = 1
type(x1)

# 浮點數 float
x2 = 1.234
type(x2)

# 複數  complex
x3 = 1+2j
type(x3)

# 布林值 (Boolean)
x4 = True
type(x4)
x4 + 10

# None值
import numpy as np
None == False
None == 0
False == 0
True == 1
None == np.nan
None == None

# 整數亂數
import random
random.seed(168)
myrandom = random.randrange(1, 100)
myrandom

# 運算子
3 + 5
3 + (5 * 4)
3 ** 2
"Hello" + "World"
1 + 1.234
7 / 2
7 // 2
7 % 2
2 ** 10
1.234e3 - 1000

x5 = 1 == 2
x5
x5 + 10

# 位移運算子: << 向左位移
# 位移運算子: >> 向右位移
a = 4 << 3 # 0100 --> 0100000, 32 16 8 4 2 1
print(a)

b = a * 4.5
print(b)

c = (a+b)/2.5

# 指派運算子
x = 9
x+=2
print(x)

##############################
# 8/11(三) 02.Python資料物件,使用NumPy模組與reshape應用
##############################

# 資料物件
# Tuple 序列 (元組) - (value,...) 不可變更
# List 串列(清單)   - [value,...]
# Set 集合          - {value,...}
# Dict 字典         - {key:value,...}

##############################
# Tuple 序列 (元組)
##############################

# 建立序列
f = (2,3,4,5) # A tuple of integers
g = () # An emptmy tuple
h = (2, [3,4], (10,11,12)) 	# A tuple containing mixed objects

# Tuples操作
x = f[1] # Element access. x = 3
x

y = f[1:3] # Slices. y = (3,4)
y

z = h[1][1] 	# Nesting. z = 4
z

xy = (2, 3)
xy

personal = ('Hannah',14,5*12+6)
personal

singleton = ("hello",)
singleton
type(singleton) # tuple

singleton1 = ("hello")
singleton1
type(singleton1) # str

# single format: tuple[index]
# index : 0  ~  len(tuple)-1
# index: -len(tuple)  ~  -1
f= (2,3,4,5)
f[0]
f[-1] # 索引 -1 表示倒數第1個元素
f[-2]
f[len(f)-1]

# slice format: tuple [start:end ]. Items from start to (end -1)
t=((1,2), (2,"Hi"), (3,"RWEPA"), 2+3j, 6E23)
t[2]
t[:3]
t[3:]
t[-1]
t[-3:]

# tuple 長度
len(t) # 5

# tuple 建構子
# 使用 tuple(( ... )) 或 tuple([ ... ]) 
employeeGender = tuple(("男", "女", "女"))
employeeGender

# tuple unpacking - 將元素指派至變數
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# TRY: green, yellow, red = fruits

# tuple unpacking - 使用萬用字元*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# tuple - loop 處理
fruits = ("apple", "banana", "cherry")

# 方法1. tuple - 取出元素, 使用for
for x in fruits:
  print(x)

# 方法2. tuple - 取出元素, 使用while
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1
  
# 方法3. tuple - 取出元素, 使用指標 range, len
for i in range(len(fruits)):
  print(fruits[i])

# tuple - join 結合
tuple1 = ("台北", "台中", "高雄")
tuple2 = ("男", "女", "女")
tuple3 = tuple1 + tuple2
print(tuple3)

# tuple - 重複
tuple1*3
3*tuple1

# count 次數統計
tuple = ("男", "女", "女", "男", "女")
tuple.count("男") # 2
tuple.count("女") # 3

##############################
# List 串列(清單)
##############################

# 建立串列
a = [2, 3, 4]            # 整數串列
b = [2, 7, 3.5, "Hello"] # 混合資料串列
c = []	                 # 空串列
d = [2, [a, b]]	         # 巢狀串列

# 串列的操作
a
a[1] 	   # 取得第2個元素
a[-1]      # 取得最後一個元素
b[1:3] 	   # 串列篩選
d[1][0][2] # 巢狀串列操作
b[0]       # 2
b[0] = 42  # 修改元素值
b[0]       # 42

# 串列 slice format
t=[1, 2, (3,"Hi"), [4,"RWEPA"], 2+3j, 6E7]
t

t[2]
t[:3]
t[3:]
t[-1]
t[-3:]

# 串列長度
len(t)

# list 建構子
# 使用 list(( ... )) 或 list([ ... ])
mylist1 = list(("男", "女", "女"))
mylist1

mylist2 = list(["男", "女", "女"])
mylist2

mylist1 == mylist2

# 串列 unpacking - 將元素指派至變數
fruits = ["apple", "banana", "cherry"]
green, yellow, red = fruits
print(green)
print(yellow)
print(red)
type(green) # str

# 串列 unpacking - 使用萬用字元*
fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]
green, yellow, *red = fruits
print(green)
print(yellow)
print(red)
type(green) # str

# 串列 - loop 處理
mylist = [1, 2, 3, [4, 5], ["A", "B", "C"]]
# 練習 loop 方法

# 方法1. list - 取出元素, 使用for
for x in mylist:
  print(x)

# 方法2. list - 取出元素, 使用while
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

# 方法3. list - 取出元素, 使用指標 range, len
for i in range(len(mylist)):
  print(mylist[i])

# 方法4. list - 取出元素, 使用串列包含法 (List Comprehension)
[print(x) for x in mylist]

# 串列包含法應用

# for 資料篩選-包括字母 a
codes = ["Python", "R", "SQL", "Julia", ".NET", "Java", "JavaScript"]
newlist = []
for x in codes:
  if "a" in x:
    newlist.append(x)
print(newlist)

# 串列包含法應用1
# 亦可用於序列, 集合, 字典等可反覆運算物件(可迭代物件, iterable object)
codes = ["Python", "R", "SQL", "Julia", ".NET", "Java", "JavaScript"]
newlist = [x for x in codes if "a" in x]
print(newlist)

# 串列包含法應用2
newlist = [x.upper() for x in codes]
print(newlist)

codes.upper() # AttributeError: 'list' object has no attribute 'upper'

# 串列包含法應用3
newlist = ['RWEPA' for x in codes]
print(newlist)

# 串列 join 結合
e = a + b  # Join two lists
e

# 串列 repeat 重複
f1 = a*3    # repeat lists
f1

f2 = 3*a
f2

# 串列排序-預設為遞增排序,英文字母先大寫,再小寫
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.sort()
print(codes)

# 串列排序-先全部小寫,再排序
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.sort(key = str.lower)
print(codes)

# 串列排序-遞減排序
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.sort(reverse =True)
print(codes)

# 串列反序
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.reverse()
print(codes)

# 串列複製,等號會建立參考物件
a = [1, 2, 3]
a
b = a
b[0] = 999 # 修改b,亦會修改a
b
a # a已經更新

# 串列複製-使用 copy
a = [1, 2, 3]
b = a.copy()
b
b[0] = 999
b
a # a保持不變

# 串列複製-使用 list
a = [1, 2, 3]
c = list(a)
c
c[0] = 123
c
a # a保持不變

# 附加元素 append
a = [1, 2, 3]
a.append(['BigData', 'SQL']) # 新增1個元素
a

# 延伸元素 extend
a.extend(['Python', 'R', "Julia"]) # 新增一個串列
a

# 延伸元素 extend - 加入tuple,list,set,dict
a = [1, 2, 3]
a.extend(('4', '5', 'RWEPA')) # 延伸一個序列
a

a.extend({'8', '8', '10'}) # 延伸一個集合
a

a.extend({'a':'R', 'b':'Python'}) # 延伸一個字典-ONLY KEY, NO VALUE
a

# 串列 – insert

# 插入元素
a = list(range(5))
a
a.insert(2, 999) # 在指標為2的位置,插入新元素
a

# 串列 – remove, pop, del

# 刪除指定元素
a.remove(999)
a

# 刪除指定指標元素
a.pop(1)
a

# 刪除指定指標元素
del a[1]
a

# 刪除第一個元素
a.pop(0)
a

# 刪除最後一個元素
a.pop()
a

# 清空物件元素,物件仍存在記憶體
a.clear()
a

# 刪除物件,物件不存在記憶體
del a
print(a) # NameError: name 'a' is not defined

# 串列 - zip 應用
a = ("x1", "x2", "x3")
b = ("y1", "y2", "y3")
c = (1, 2, 3)

x = zip(a, b, c)
x
list(x)

# 顯示方法
print(dir(list))

# 實作練習4
# 如何顯示不以 __ 開始串列方法的總個數 11

##############################
# Set 集合
##############################

# 集合與字典相似, 但字典沒有key,只有值
# 集合內容不可以修改
# 集合是  unordered
# 集合是  unindexed
# 集合會忽略重複的值

a = set() # 空集合
type(a)

b = {"台北市", "新北市", "桃園市", "台中市", "台北市", "新北市", "高雄市"}
b # {'台中市', '台北市', '新北市', '桃園市', '高雄市'}

# b[0] = 1 # TypeError: 'set' object does not support item assignment
# b[0]     # TypeError: 'set' object is not subscriptable

len(b)

# 使用 myset 練習集合 - loop 方法
myset = {"台北市", "新北市", "桃園市", "台中市", "高雄市"}
myset

# 集合新增元素 add, 因為集合是unordered, 不一定新增在最後一個
myset = {"台北市", "新北市", "桃園市", "台中市", "高雄市"}
myset.add("台南市")
myset

# 集合新增集合
myset.update({"澎湖", "金門"})
myset

# 刪除指定元素
myset.remove("澎湖")
myset

# 清空物件兀素,物件仍存在記憶體
myset.clear()
myset

# 刪除物件,物件不存在記憶體
del myset
myset # NameError: name 'myset' is not defined

# 集合運算
x = {1,2,3,4,5}
y = {1,3,5,7}

x & y # {1, 3, 5} # 交集

x.intersection(y) # 交集

x | y # {1, 2, 3, 4, 5, 7} # 聯集

x.union(y) # 聯集

x ^ y # {2, 4, 7} # XOR 互斥

x - y # 差集

x.difference(y) # 差集

##############################
# Dict 字典
##############################

# 字典宣告
mydict = {
    "language": "Python",
    "designer": "Guido van Rossum",
    "year": 1991
    }

print(mydict)

type(mydict) # dict

# 重複 key, 只保留1個
mydict1 = {
    "language": "Python",
    "designer": "Guido van Rossum",
    "year": 1991,
    "year": 2021
    }

print(mydict1)

# 字典存取元素
b = {
     "uid": 168, 
     "login": "marvelous", 
     "name" : 'Alan Lee'
     }
b

# dict 取得所有 keys
mykeys = b.keys()
print(mykeys)

# dict 取得所有 values
myvalues = b.values()
print(myvalues)

# dict 取得key的值
u = b["uid"] # 168
print(u)

# dict 更新值
b.update({"uid": 123})
print(b)

# dict 新增元素
b["shell"] = "/bin/sh"
print(b)

# dict 刪除元素 - pop
b.pop("shell")
print(b)

# dict 刪除元素 - del
del b["login"]
print(b)

# dict 清空整個物件 - clear
b.clear()
b

# dict 刪除整個物件 -del
del b
b

# dict - items 物件, 回傳 [(key1,value1), (key2,value2,...)]
# 回傳 list[(序列1), (序列2), ...]
b = {
     "uid": 168, 
     "login": "marvelous", 
     "name" : 'Alan Lee',
     "shell": "/bin/sh"
     }
b
x = b.items()
print(x)

# 檢查 key 是否存在
# AttributeError: 'dict' object has no attribute 'has_key'
# 早期版本使用 has_key
if b.has_key("uid"):
	d = b["uid"]
else:
	d = None

# 使用 in
if "uid" in b:   # v3.x 直接使用 in
    d = b["uid"]
else:
    d = None
print(d)

# 使用 get
d = b.get("uid", None) # 較簡潔
print(d)

# dict - loop 處理
mydict = {
    "uid": 168, 
    "login": "marvelous", 
    "name" : 'Alan Lee'
    }
mydict

# for - 回傳 keys
for x in mydict:
    print(x)
    
# for - 使用 keys
for x in mydict.keys():
    print(x)

# for - 回傳 values
for x in mydict:
    print(mydict[x])

# for - 使用 values()
for x in mydict.values():
    print(x)

# for - 回傳 (key, value) 使用 items()
for x,y  in mydict.items():
    print(x, y)

# 字典複製-使用 copy
mydict = {
    "uid": 168, 
    "login": "marvelous", 
    "name" : 'Alan Lee'
    }
mydict

mydict2 = mydict.copy()
print(mydict2)

# 字典複製-使用 dict
mydict3 = dict(mydict)
print(mydict3)

mydict2 == mydict3 # True

# 巢狀字典 (Nested Dictionaries)

# 方法1 一次建立一個巢狀字典
mycodes = {
    "code1" : {
         "name" : "Fortran77",
         "year" : 1977
         },
    "code2" : {
        "name" : "Python",
        "year" : 1991
        },
    "code3" : {
        "name" : "R",
        "year" : 2000
        }
    }

mycodes

# 方法2 建立三個字典,再合併為一項字典
mycode1 = {
    "name" : "Fortran77",
    "year" : 1977
    }

mycode2 = {
    "name" : "Python",
    "year" : 1991
    }

mycode3 = {
    "name" : "R",
    "year" : 2000
    }

mycodes2 = {
  "程式1" : mycode1,
  "程式2" : mycode2,
  "程式3" : mycode3
}

mycodes2

# 實作練習5
# 將 list 轉換為 dictionary
# 輸入: lst = ['a', 1, 'b', 2, 'c', 3]
# 結果: {'a': 1, 'b': 2, 'c': 3}

##############################
# 模組 Modules
##############################

# 使用模組
import math
math.sqrt(9)

from math import sqrt
sqrt(9)

# 切換工作目錄
import os
os.getcwd() # 讀取工作目錄
os.chdir("C:/") # 變更工作目錄
os.getcwd()
os.listdir(os.getcwd()) # 顯示檔案清單

# 模組的搜尋路徑
import sys
sys.path
# '' 表示現行目錄

# 實作練習6
# 自訂模組, 計算商數與餘數
# 自訂模組檔案名稱為 numberscompute.py
# 練習檔案名稱為 mycompute.py

##############################
# 物件導向 - 類別
##############################

# 範例1
# 建立類別 class
class MyClass:
  x = 5

# 使用 () 實作實例
p1 = MyClass()
print(p1.x)

# 範例2
# __init__() 函數表示類別初使化時,該函數會自動執行, 左右為二個底線
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p1

print(p1.name)
print(p1.age)  

# 範例3
# Inheritance 繼承
# 父類別(Parent class)是給其他繼承的類別, 稱為基本類別.
# 子類別(Child class )是從另一個父類別繼承的, 也稱為衍生類別(derived class).
# https://www.w3schools.com/python/python_inheritance.asp

# 父類別
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("ALAN", "LEE")
x.printname()

# class 子類別(父類別)
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

# 新增 __init__ 函數
# 子類別的__init __()函數將覆蓋父類別的__init __()函數
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# super - 表示使用父類別的方法
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Big", "Data")
x.printname()

##############################
# Numpy 模組
##############################

import numpy as np

####################
# 一維陣列
##############################

# 使用 tuple 或 list 建立一維陣列
a = np.array([1, 2, 3, 4, 5])
b = np.array((1, 2, 3, 4, 5), dtype=float) 

print(a)
print(b)

print(type(a))
print(type(b))

print(a[0], a[1], a[2], a[3])

b[0] = 5    
print(b) 

b[4] = 0
print(b)

##############################
# 二維陣列
##############################

# 使用巢狀清單建立二維陣列
# axis 0:列, axis 1:行
a = np.array([[1,2,3],[4,5,6]])
a 

print(type(a))

print(a[0, 0], a[0, 1], a[0, 2])

print(a[1, 0], a[1, 1], a[1, 2])

a[0, 0] = 6
a[1, 2] = 1
print(a)

# np.arrange
a = np.arange(5) # [0 1 2 3 4]
print(a) 

b = np.arange(1, 11, 2) # 1<= x < 11
print(b) # [1 3 5 7 9]

# np.zeros
np.zeros(5) # array([0., 0., 0., 0., 0.])

np.zeros(5, dtype=int) # array([0, 0, 0, 0, 0])

np.zeros((3, 2)) # 建立3列,2行皆為零的陣列
# array([[0., 0.],
#        [0., 0.],
#        [0., 0.]])

# np.ones 
np.ones(3) # array([1., 1., 1.])

# np.full
np.full(shape = (3, 4), fill_value = 99)
# array([[99, 99, 99, 99],
#        [99, 99, 99, 99],
#        [99, 99, 99, 99]])

# zeros_like
a = np.array([[1,2,3], [4,5,6]])
a
# array([[1, 2, 3],
#        [4, 5, 6]])

np.zeros_like(a)
# [[0 0 0]
#  [0 0 0]]

# ones_like
np.ones_like(a)
# [[1 1 1]
#  [1 1 1]]

##############################
# 陣列儲存與載入
##############################

# 實作練習7
# 使用 save 將 Numpy 陣列 a 儲存成外部檔案
outputfile = 'myarray.npy'
with open(outputfile, 'wb') as fp:
    np.save(fp, a)

# 使用 load 將外部檔案匯入至Numpy陣列
outputfile = "myarray.npy"
with open(outputfile, 'rb') as fp:
    mydata = np.load(fp)
print(mydata)

##############################
# 常數 Constants
##############################

import numpy as np

np.Inf # 無限大 inf

np.NAN # nan

# 新版本使用 nan
np.nan

np.pi # 3.141592653589793

# Euler’s constant, base of natural logarithms
# Napier’s constant(蘇格蘭數學家約翰·納皮爾)
np.e # 2.718281828459045

# 三角函數
# sin(30度) = sin(pi/6) = 0.5
# sin(45度) = sqrt(2)/2 = 0.707
# sin(60度) = sqrt(3)/2 = 0.866
# sin(90度) = 1
a = np.array([30, 45, 60, 90])
np.sin(a*np.pi/180)

##############################
# 亂數
##############################

import numpy as np

np.random.seed(123) # 設定亂數種子, 須輸入 >= 1 的整數

# random 產生0.0~1.0之間的1個亂數
x1 = np.random.random()
print(x1)

# random 產生0.0~1.0之間的3個亂數
x2 = np.random.random(3)
print(x2)

# rand 產生0.0~1.0之間的1個亂數
x3 = np.random.rand()
print(x3)

# rand 產生0.0~1.0之間的3個亂數
x4 = np.random.rand(3)
print(x4)

# rand(row, column) 產生亂數值陣列
x5 = np.random.rand(3, 2) # 3列,2行
print(x5)

# randint 產生 min 與 max 之間的整數亂數,不包括max
# randint(max, size)

# 建立 5~10之間的1個整數亂數
x6 = np.random.randint(5, 10)
print(x6)

# randint(min, max, size), min <= x < max

# 建立 1~11之間的10個整數亂數
x7 = np.random.randint(1, 11, size=10)
print(x7)

# 建立 1~11之間的4列5行陣列的整數亂數
x8 = np.random.randint(1, 11, size=(4, 5))
print(x8)

# 標準常態分配隨機樣本
# https://numpy.org/doc/stable/reference/random/generator.html

from numpy import random

# 舊版用法
vals = random.standard_normal(3)
print(vals)

more_vals = random.standard_normal(3)
print(more_vals)

# 新版用法
from numpy.random import default_rng

rng = default_rng()
vals = rng.standard_normal(3)
print(vals)

more_vals = rng.standard_normal(3)
print(more_vals)

##############################
# 陣列的屬性
##############################
import numpy as np

a = np.array([0,1,2,3,4,5])
a
a.dtype    # dtype('int32')
a.size     # 6
a.ndim     # 1
a.shape    # (6,)
a.itemsize # 4 bytes
a.nbytes   # 24

b = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10.]])
b
b.dtype    # float64
b.size     # 12
b.ndim     # 2
b.shape    # (3, 4)
b.itemsize # 8
b.nbytes   # 12*8=96

# 資料型別轉換
b.astype('int32')
b = b.astype('int32')
b.dtype    # int32

# 實作練習8
# 建立3維陣列 myzero, 5個元素, 每個元素為3列,4行的零矩陣
# myzero.shape 結果為 (5, 3, 4)

##############################
# array 一維陣列 - loop 處理
##############################

a = np.array([1,2,3,4])
a

# 方法1. array - 取出元素, 使用for
for x in a:
  print(x)

# 方法2. array - 取出元素, 使用while
i = 0
while i < len(a):
  print(a[i])
  i = i + 1

# 方法3. array - 取出元素, 使用指標 range, len
for i in range(len(a)):
  print(a[i])

# 方法4. array - 取出元素, 使用陣列包含法
[print(x) for x in a]

##############################
# array 二維陣列 - loop 處理
##############################

a = np.array([[1,2,3,4], [5,6,7,8]])
a

for x in a:
  print(x)

for x in a:
    for item in x:
        print(str(item) + " ", end = " ")

##############################
# array 運算
##############################

a = np.array([1,2,3])
b = np.array([4,5,6])
a+b # 加
a-b # 減
a*b # 乘
a/b # 除

# 矩陣相乘(dot)
a = np.array([[1,2],[3,4],[5,6]])
a
b = np.array([[1,2],[3,4]])
b
a.shape
b.shape
c = a.dot(b) # 矩陣相乘(dot)
c

np.transpose(c) # 矩陣轉置
c.T             # 矩陣轉置

# inv()：反矩陣,逆矩陣 (inverse matrix)
from numpy.linalg import inv

x = np.array([[1, 2], [3, 4]])

inv(x)
# array([[-2. ,  1. ],
#        [ 1.5, -0.5]])

# 單位矩陣 (Identity matrix)
x.dot(inv(x))
# array([[1.00000000e+00, 1.11022302e-16],
#        [0.00000000e+00, 1.00000000e+00]])

x.dot(inv(x)).round(1)
# array([[1., 0.],
#        [0., 1.]])

# 計算矩陣行列式值 (determinant)
np.linalg.det(x)
# -2.0000000000000004

# 計算方形矩陣的特徵值 (eigenvalue) 與特徵向量 (eigenvector)
np.linalg.eig(x)
# (array([-0.37228132,  5.37228132]),
#  array([[-0.82456484, -0.41597356],
#         [ 0.56576746, -0.90937671]]))

##############################
# 陣列應用 -高維度影像
# MNIST 手寫數字辨識資料集
##############################
# http://yann.lecun.com/exdb/mnist/

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 方法1 回傳 Bunch 資料物件
# 原圖為28*28, 2維展開為1維 28*28=784

mnist_data = fetch_openml("mnist_784")
xdata = mnist_data["data"] # 70000*784
ydata = mnist_data["target"] # 70000

xdata.ndim # 2
xdata.shape # (60000, 784)
xdata.dtype

# 方法2 直接回傳 X, y

# Load data from https://www.openml.org/d/554
X, y = fetch_openml('mnist_784', return_X_y=True)
# X : 70000*84
# y : 70000

X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    random_state=123, 
                                                    test_size=10000)
type(X_train) # DataFrame (早期版本為 numpy.ndarray)

# 將 DataFrame 轉換成 array 物件
X_train = X_train.to_numpy()
y_train = y_train.to_numpy()

type(X_train) # numpy.ndarray
X_train.ndim # 2
X_train.shape # (60000, 784)
X_train.dtype # dtype('float64')

type(y_train) # numpy.ndarray
y_train.ndim # 1
y_train.shape # (60000,)
y_train.dtype # dtype('O'), 表示字串

# 繪製數字影像
plt.imshow(X_train[0].reshape(28,28), cmap='binary')

# 實際值
y_train[0] # '5'

# 繪製多個數字影像, 最多一次顯示25個
def plot_images_labels(images, labels, idx, num=10):
    fig = plt.gcf() # 取得目前的 figure
    fig.set_size_inches(12, 14) # 設定圖形大小
    if num > 25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5, 5, 1+i)
        ax.imshow(images[idx].reshape(28,28), cmap='binary')
        title= "Label=" + str(labels[idx])
        ax.set_title(title, fontsize=20)
        ax.set_xticks([])
        ax.set_yticks([])        
        idx+=1 
    plt.show()

plot_images_labels(X_train, y_train, 0, 10)

##############################
# reshape 應用
##############################
import numpy as np

z = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
z
z.reshape(-1) # -1: unknown dimension
# array([ 1,  2,  3, ..., 10, 11, 12])

z.reshape(-1,1) # row -1: unknown , column 1

z.reshape(-1, 2) # row -1: unknown , column 2

z.reshape(1,-1) # row 1 , column: unknown

z.reshape(2, -1) # row 2 , column: unknown

z.reshape(3, -1) # row 3 , column: unknown

z.reshape(-1, -1) # ERROR

##############################
# 建立副本
##############################

# 建立副本-使用等號
a = np.array([0,1,1,2,3,5])
b = a.reshape((3,2)) # b之修改會影響a
b

b.ndim   # 2
b.shape  # (3,2)

b[1][0] = 168
b
a # a物件已經更改, array([  0,   1, 168,   3,   4,   5])

# 建立副本-使用 copy
c = a.reshape((3,2)).copy()
c
c[0][0] = -999
c
a # a物件沒有更改

##############################
# 向量化處理
##############################

a = np.array([0,1,1,2,3,5])

a*2

a**3 # 次方運算

# indexing

a[np.array([1,3,5])]

##############################
# 離群值調整
##############################

a = a**3
a > 10
a[a > 10]
a[a > 10] = 10
a

a.clip(0, 3)

##############################
# nan 處理
##############################

# isnan 判斷是否為 nan
x = np.array([1, 2, 3, np.nan, 4])
x
np.isnan(x)

# 刪除 nan 值
x[~np.isnan(x)]

np.mean(x[~np.isnan(x)])

np.mean(x) # nan

##############################
# 計算時間
##############################

import timeit
import numpy as np

normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000)
naive_np_sec = timeit.timeit('sum(na*na)', setup="import numpy as np; na=np.arange(1000)", number=10000)
good_np_sec = timeit.timeit('na.dot(na)', setup="import numpy as np; na=np.arange(1000)", number=10000)

print("Normal Python: %f sec"%normal_py_sec)
print("Naive NumPy: %f sec"%naive_np_sec)
print("Good NumPy: %f sec"%good_np_sec)

print "Hello World"    # python 2
print("Hello World")   # python 3

##############################
# 8/12(四) 03.字串與正規表示式,判斷式與函數應用
##############################

##############################
# 字串處理
##############################

# 字串輸入 input
# input-範例1
name = input("keyin your name? ")
print(name)
type(name) # str

# input-範例2
mynumbers = input("輸入2個數值, 中間使用逗號區隔, 計算2個數值相加結果?")
print(mynumbers)

# 字串(String)由一個(以上)字元所組成
# 字串左右二側須使用單引號或是雙引號

# 字串物件 https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 字串方法 https://docs.python.org/3/library/string.html

city = '台北市'
district = '信義區'
road = '信義路五段7號'

# 使用 + 字串串接
city + district

address = city + district + road
print(address)

# 數值轉換為字串
myinteger = 123
mystr = str(myinteger)
mystr
type(mystr)

# 字串轉換為數值
mystr = "123.456"
myvalue = float(mystr)
myvalue
type(myvalue)

# 8進位,16進位,Unicode字串表示
'\156' # 8進位          \aaa
'\x6E' # 16進位-英文大寫 \xFFFF
'\x6e' # 16進位-英文小寫 \xffff

mystr1 = '\N{GREEK SMALL LETTER ALPHA}' # \N Unicode名稱: 'α'
mystr1

mystr2 = '\N{LATIN SMALL LETTER U WITH DIAERESIS}' # 'ü'
mystr2

mystr3 = '\u00FC' # \u 4碼16進位表示Unicode字元, 'ü'
mystr3

# 字串指標存取
address       # '台北市,信義區,信義路五段7號'
address[0]    # '台'
address[-1]   # '號'
address[8:13] # '信義路五段'

# 使用 * 建立重複字串
city   # '台北市'
5*city
city*5

# len 長度
len(address) # 15

# 字串分割 – split
# str.split(sep=None, maxsplit=-1)
# 預設分割 sep 為空白字元, maxsplit=-1 表示沒分割次數限制

address = city + ',' + district + ',' + road
address
address.split(',') # 預設分割字元為空白字元
address.split(',',  maxsplit = 1) # 預設分割字元為空白字元

# 字串結合 - join

city = "台北市"
district = "信義區"
road = "信義路五段7號"
str1 = city + district + road
str1

''.join([city, district, road])

'-'.join([city, district, road])

mytuple = ("台北市", "信義區", "信義路五段7號")
"".join(mytuple)
           
# 字串 if in (if not in)
txt = "One of the world's strictest lockdowns is lifting, but many are scared to go back to normal life."

if "scared" in txt:
    print("Find 'scared'") # 完全比對
    
if "scare" in txt:
    print("Find 'scare'") # 部分字串相同
    
if "Scare" in txt:
    print("Find 'Scare'") # 區分大小寫

# 刪除左側或右側空白字元 strip (中間的字元不會刪除) 
# 刪除左側空白字元 lstrip 
# 刪除右側空白字元 rstrip
x = " RWEPA - Python 大數據分析\n "

x.strip()  # \n 視為空白字元而加以刪除
x.lstrip()
x.rstrip()

import string
string.whitespace # ' \t\n\r\x0b\x0c' \x0b:印表機垂直定位符號, \x0c:換頁符號

x.strip("Python") # 中間字元會保留
"Python大數據分析Python".strip("python") # 有區分大小寫
"Python大數據分析Python".strip("Python") # 有區分大小寫
"Python大數據分析Python".lstrip("python")
"Python大數據分析Python".rstrip("python")

# 字串判斷 str.isxxx
"123".isdigit()                # 數字digits包括 '0123456789'
"123".isalpha()                # 數字不是英文字母
"alan9956".isalpha()           # 英文加數字不是英文字母
"alan9956".isdigit()           # 英文加數字不是數字
"!@#$%^&*()[]{}\|".isascii()   # 半型符號是ASCII
"おはようございます".isascii()   # 日本字不是ASCII
"大數據分析".isascii()          # 中文字不是ASCII
"RWEPA".isupper()              # 大寫英文字母
"alan9956@gmail.com".islower() # 小寫英文字母

# 實作練習9
# 計算 mystr 字串中, 不區分大小寫, 英文字母出前次數最多的前6名為何?
mystr = 'Scikit-learn is an Open source Machine Learning learning library that supports supervised and unsupervised learning.'
# 技巧: 使用 collections.Counter 方法
# 答案為 n, e, i, r, s, a

# 字串的搜尋
# find 回傳字串的索引, 找不到回傳-1
mystr.find('learning') # 39
mystr.find('bigdata') # -1

mystr.index('learning') # 39
mystr.index('bigdata') # ValueError: substring not found

for x in mystr:
    print(x)

# rfind 從最後面查詢
mystr.rfind('learning') # 98

# 字串取代 - replace
address = '台北市,信義區,信義路五段7號'
address.replace(',', '*') # '台北市*信義區*信義路五段7號'

##############################
# 字串格式化 - 4種方式
##############################

# 字串格式化 方法1. 早期使用 %, 與 C語言 的 printf 相似
text = 'world'
print('Hello %s' % text) # Hello world

# 字串格式化 方法2. str.format 函數

# 1個參數
year = 2021
txt = "我的名字是 Alan, 現在是 {} 年"
print(txt.format(year)) # 我的名字是 Alan, 現在是 2021 年

# 多個參數
quantity = 1
item = "美國Blue Yeti 雪怪 USB麥克風"
price = 5590

myorder = "感謝您訂購-->產品名稱: {}, 數量: {}, 價格: {} 元"
print(myorder.format(item, quantity, price))
# 感謝您訂購-->產品名稱: 美國Blue Yeti 雪怪 USB麥克風, 數量: 1, 價格: 5590 元

# 多個參數-使用指標
quantity = 1
item = "美國Blue Yeti 雪怪 USB麥克風"
price = 5590

myorder = "感謝您訂購-->數量: {1}, 產品名稱: {0}, 價格: {2} 元"
print(myorder.format(item, quantity, price))
# 感謝您訂購-->數量: 1, 產品名稱: 美國Blue Yeti 雪怪 USB麥克風, 價格: 5590 元

# 字串格式化 方法3. Formatted String Literal - 將運算式置於字串之中

text = 'world'
print(f'Hello, {text}') # Hello, world

x = 10
y = 27
print(f'x + y = {x + y}') # x + y = 37

# 字串格式化 方法4. Template String 樣板字串 - 使用 string.Template

from string import Template

mytext = 'world'
t = Template('Hello $text') # 使用1個變數 $text
type(t) # string.Template
t.substitute(text=mytext) # 將 text置換為 mytext, 'Hello world'
# 參考: https://stackabuse.com/formatting-strings-with-the-python-template-class

##############################
# 正規表示式
##############################

# https://docs.python.org/3/library/re.html

# re.complile  建立正規表示式
# re.match     從開始位置檢查是否匹配. 如果有, 則回傳匹配結果. 如果沒有, 則回傳 None.
# re.fullmatch 從開始或結束位置檢查是否匹配
# re.search    從任何位置開始模式匹配，回傳第１筆
# re.findall   回傳與模式匹配的所有字串
# re.split     分割
# re.sub       取代

# re範例-電話號碼
# 參考 Automate the Boring Stuff with Python, 第2版.
# Python 自動化的樂趣｜搞定重複瑣碎&單調無聊的工作, 碁峰資訊, 2020.

# 02-8101-8800，(區域碼)2碼數字–4碼數字–4碼數字

# 方法1-使用 if, for
def isPhoneNumber(text):
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False  # not an area code
    if text[2] != '-':
        return False  # does not have first hyphen
    for i in range(3, 7):
        if not text[i].isdecimal():
            return False  # does not have first 3 digits
    if text[7] != '-':
        return False  # does not have second hyphen
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # does not have last 4 digits
    return True  # "text" is a phone number!

print('02-8101-8800is a phone number:')
print(isPhoneNumber('02-8101-8800'))

print('02-1234-ALAN is a phone number:')
print(isPhoneNumber('02-1234-ALAN'))

# 方法2-使用正規表示式
import re

phoneRegex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d') # 建立正規表示式物件

mystr = '02-8101-8800'
myresult1 = phoneRegex.match(mystr)
myresult1

mystr = '02-8101-ALAN'
myresult2 = phoneRegex.match(mystr)
myresult2

# re範例-字串
mystr = 'Please call ALAN at 02-2822-5252. 02-1234-5678 is his office number. Try 02-87654321'

# match 方法
phoneRegex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d') # 建立正規表示式物件

# 方法1
myresult = phoneRegex.match(mystr) # 使用match, 從最左側搜尋.
print(myresult) # None 表示沒有找到符合字串

# 方法2
myresult1 = re.match(phoneRegex, mystr)
print(myresult1) # None,與方法1結果相同.

# fullmatch 方法, 與 match類似,除了最左側另包括最右側搜尋
print(re.fullmatch(phoneRegex, mystr)) # None

# search 方法
phoneRegex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
phoneRegex.search(mystr) 
# 有找到1筆資料
# <re.Match object; span=(20, 32), match='02-2822-5252'>

phoneRegex = re.compile(r'\d{2}-\d{4}-\d{4}')
phoneRegex.search(mystr) # 結果與前面相同

# findall 方法
phoneRegex.findall(mystr)
# ['02-2822-5252', '02-1234-5678']

# 實作練習10
# 字串練習-match, fullmatch, search, findall
# 以 mystr 字串練習 learning 或 Learning
mystr = 'Learning is the obtaining of new knowledge. Scikit-learn is an Open source Machine learning library that supports supervised and unsupervised learning'
# 使用 match, fullmatch, search, findall

# 實作練習11
# 以 mystr 字串練習, 使用 findall 找出所有股票代碼
# 結果為 ['2481-TW', '4952-TW', '3264-TW', '6531-TW']
mystr = '隨著歐美多國解封，燃油車、電動車市況明顯回溫，帶動車用電子強勁需求，相關零組件廠出貨也陸續報捷，車電族群今 (13) 日再度發動猛攻，包括強茂 (2481-TW)、凌通 (4952-TW)、欣銓 (3264-TW)、愛普 (6531-TW) 等多檔，盤中均亮燈漲停。'

# group 方法,使用左右括號 ()
mystr = '101大樓客服電話是 02-8101-8800'

phoneRegex = re.compile(r'(\d{2})-(\d{4}-\d{4})')
myresult = re.search(phoneRegex, mystr)
print(myresult) # match='02-8101-8800'

myresult.group(0) # 取得全部號碼 '02-8101-8800'
myresult.group(1) # 取得區域號碼 '02'
myresult.group(2) # 取得電話號碼 '8101-8800'

# groups 方法
areaCode, mainCode = myresult.groups()
areaCode # '02'
mainCode # '8101-8800'

# group 方法+跳脫字元
mystr = '101大樓客服電話是 (02)-8101-8800'
phoneRegex = re.compile(r'(\d{2})-(\d{4}-\d{4})')
myresult = re.search(phoneRegex, mystr)
print(myresult) # None-->找不到???

phoneRegex = re.compile(r'(\(\d{2}\))-(\d{4}-\d{4})')
myresult = re.search(phoneRegex, mystr)
print(myresult)

myresult.group(0) # 取得全部號碼 '02-8101-8800'
myresult.group(1) # 取得區域號碼 '(02)'
myresult.group(2) # 取得電話號碼 '8101-8800'

# re範例-保留日與時期：

import re
mystr = '現在的日期時間是：2021-08-01 14:02:48'

datetime = re.search('\d+-\d+-\d+ \d+:\d+:\d+', text1).group(0)
print(datetime)

# re範例-保留中間字串

mystr = '作者 - 李明昌 老師'

author = re.search('編輯 - (.*) ', mystr).group(1)
print(author)

author = re.search('編輯 - (.*?) ', mystr).group(1)
print(author)

author = re.search('編輯 - (\w+)', mystr).group(1)
print(author)

##############################
# 判斷式 if elif else
##############################

"""
# case 1
if 布林值:
 	若布林值為 True，執行命令

# case 2
if 布林值:
 	若布林值為 True，執行命令
else:
    若布林值為 False，執行命令

# case 3
if 布林值一:
 	若布林值一為 True，執行命令
elif 布林值二:
 	若布林值二為 True，執行命令
...
else:
 	若布林值一和二...都是 False，執行命令
"""

# elif敘述
a = '+'

if a == '+':
	op = 'PLUS'
elif a == '-':
	op = 'MINUS'
else:
	op = 'UNKNOWN'

op

# 沒有像C語言一樣，有switch的語法
# 布林表示式 – and, or, not
a = 1
b = 6
c = 9

if b >= a and b <= c:
	print('b is between a and c')
    
if not (b < a or c > c):
	print('b is still between a and c')

# if 範例 - 測試所有輸入情形
mynameage = input('輸入姓名與年齡: ')

name = mynameage.split(',')[0]
age = mynameage.split(',')[1]

if name == 'Alan':
    print('Hi, Alan.')
elif age < 20:
    print('You are not Alan.')

# 邏輯錯誤 (Logical Errors)
# if 範例 - age > 200 不會執行
name = 'RWEPA'
age = 300
if name == 'Alan':
    print('Hi, Alan.')
elif age < 20:
    print('You are not Alan.')
elif age > 100:
    print('You are not Alan. 大大')
elif age > 200:
    print('年齡異常')
# You are not Alan. 大大

##############################
# 迴圈 (Loops)
##############################

# while 迴圈
name = ''
while name != 'Alan Lee':
    print('Please type your name.')
    name = input()
print('Thank you!')

# while + break
while True:
    print('Please type your name.')
    name = input()
    if name == 'Alan Lee':
        break
print('Thank you!')

# while + break + continue
while True:
    print('Who are you?')
    name = input()
    if name != 'Alan':
        continue
    print('Hello, Alan. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

# for + range

# 顯示list元素
for i in [3, 4, 10, 25]:
	print(i)

# 顯示一個字元
for c in "Hello":
	print(c)

# 顯示 range 元素
for i in range(1, 4):
	print(i)

for i in range(4, -2, -1):
	print(i)


# 零數值判斷, 以下結果皆為 True
0 == False
0.0 == False
0.000 == False
'' == False

# 非零數值判斷
1 == True     # True
1.23 == True  # False
1.23 == False # False

# 實作練習12
# for + continue 迴圈練習, 篩選出 list 的字串資料
# 提示: 使用 if, for, append, continue 順序非固定
# 結果 ['python', '123.45', 'RWEPA', 'R']
mylist = [1, 3, "python", '123.45', "RWEPA", 100, "R"]

##############################
# def 函數應用
##############################

# 回傳 a/b 之餘數
def remainder(a,b):
	q = a/b
	r = a - q*b
	return r

# 如何修改回傳餘數2
a = remainder(42,5) # a = 2
print(a)

# 回傳 a/b 之商數與餘數
# 參考上例練習
def divide(a,b):
	q = a/b
	r = a - q*b
	return q,r

x,y = divide(42,5) 	# x = 8, y = 2
print(x)
print(y)

# None值
answer = print("Hello")
type(answer) # NoneType
answer == None

# 實作練習13
# 使用 def 建立計算2點之間的直線距離函數
# 函數名稱 distance
# 引數名稱 x1, y1, x2, y2
# 不可使用 math.sqrt 函數
# 輸入第1個點的座標值為 (a, b)
# 輸入第2個點的座標值為 (c, d)

# Python: lambda 函數
# refer to materials

# 函數撰寫範例研究
# Master Machine Learning: K Nearest Neighbors From Scratch With Python
# https://python-bloggers.com/2021/03/master-machine-learning-k-nearest-neighbors-from-scratch-with-python/

##############################
# 檔案處理
##############################

# os模組-建立與切換工作目錄
import os
os.getcwd()             # 讀取工作目錄

dir = os.path.join("C:/","mydata")
if not os.path.exists(dir):
    os.mkdir(dir)       # 建立目錄

os.chdir(dir)           # 變更工作目錄
os.listdir(os.getcwd()) # 顯示檔案名稱

# 方法1.檔案的開啟/寫入/關閉
f = open("coding.dat", "w") # Open a file for writing
f.write("Hello World\n")
f.write("Python\n")
f.write("R\n")
f.write("SQL\n")
f.write("Excel VBA\n")
f.close()

g = open("coding.dat","a") 	# Open a file for appending
g.write(".NET")
g.close()

# 方法2.使用 with區塊

# with open("coding.dat", "r") as infile:

# with區塊特性
# 檔案會自動關閉, 可以不用撰寫 .close()
# 即使出現以下狀況, 檔案仍會自動關閉:
#  (1)發生例外 (Exception)
#  (2)執行 return, continue, break 等而跳出 with 區塊

# read 讀取全部資料
with open("coding.dat", "r") as infile:
    mydata = infile.read()
    print(type(mydata)) # str
    print(mydata)

# readline 一次讀一列資料, while 迴圈-預設加入分隔列
with open("coding.dat", "r") as infile:
    while True:
        line = infile.readline()  # 一次讀一列資料
        if not line:              # 所有資料讀取完畢
            break
        print(line)               # 預設加入分隔列

# readline 一次讀一列資料, while 迴圈自訂分隔列符號
with open("coding.dat", "r") as infile:
    while True:
        line = infile.readline()     # 一次讀一列資料
        if not line:                 # 所有資料讀取完畢
            break
        print(line, end='*')          # end='*' 自訂分隔列符號

# readlines 一次讀取所有資料
with open("coding.dat", "r") as infile:
    for line in infile.readlines():  # 一次讀取所有資料，再逐列處理
        print(line, end='')
        
# readlines 簡化版本
with open("coding.dat", "r") as infile:
    for line in infile:
        print(line, end='')

# 檔案處理範例
# 讀入 coding.dat, 加上額外一列, 寫入另一檔案 output.txt
with open("coding.dat", "r") as infile:
    data = infile.read()
data

with open("output.txt", "w") as outfile:
    outfile.write('New data: C++ language\n')
    outfile.write(data)

# 例外處理機制
# https://docs.python.org/3/tutorial/errors.html

def exceptTest():
    try:
        x, y = eval(input("輸入2個數字,中間以,區隔: "))
        answer = x/y
        myanswer = " {}/{} = {} "
        print(myanswer.format(x, y, answer))
    except ZeroDivisionError:
        print('被除數不可為零 Division by zero!')
    except SyntaxError:
        print("二個數值中間要加上 , ")
    except:
        print("輸入有錯誤")
    else:
        print("<<<運算沒錯誤>>>")
    finally:
        print("程式已執行完成")

exceptTest()

# 8. Errors and Exceptions
# https://docs.python.org/3/tutorial/errors.html

# Built-in Exceptions and Exception hierarchy
# https://docs.python.org/3/library/exceptions.html

# 內建例外Error
dir(__builtins__)

##############################
# 8/13(五) 04.日期時間資料,檔案匯入pandas
##############################

##############################
# 日期時間
##############################

# 使用 datetime 模組
from datetime import date, time, datetime

date(year=2021, month=8, day=10) # datetime.date(2021, 8, 10)

time(hour=13, minute=30, second=31) # datetime.time(13, 30, 31)

datetime(year=2021, month=8, day=10, hour=13, minute=30, second=31)
# datetime.datetime(2021, 8, 10, 13, 30, 31)

# 現在日期,時間
today = date.today()
today

now = datetime.now()
now

current_time = time(now.hour, now.minute, now.second)
current_time

datetime.combine(today, current_time)

# 字串轉換為日期-fromisoformat
mystr = "2021-07-21"
mydate = date.fromisoformat(mystr)
mydate
print(mydate)

# 字串轉換為日期-strptime
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

# Year    %Y (4位數值年)
# Month   %m (2位數值月)
# Date    %d (2位數字日)
# Hour    %H (2位數字24小時的時)
# Minute  %M (2位數字分)
# Second  %S (2位數字秒)

date_string = "06-30-2021 12:34:56"
format_string = "%m-%d-%Y %H:%M:%S"
datetime.strptime(date_string, format_string)
# datetime.datetime(2021, 6, 30, 12, 34, 56)

# 範例-日期計算
PYCON_DATE = datetime(year=2022, month=4, day=27, hour=8)
countdown = PYCON_DATE - datetime.now()
type(countdown) # datetime.timedelta
countdown
countdownDay = countdown.days

txt = "距離 2022年4月27日 USA PyCon 還有 {} 天"
print(txt.format(countdownDay))

# Time Zones 時區 - 使用 dateutil 模組
# https://dateutil.readthedocs.io/en/stable/

from dateutil import tz
from datetime import datetime

now = datetime.now(tz=tz.tzlocal())
now
now.tzname() # '台北標準時間'

my_tz = tz.gettz('Asia/Taipei')
my_tz # tzfile('ROC')

London_tz = tz.gettz("Europe/London")
now = datetime.now(tz=London_tz)
now
now.tzname()

# 範例-時區轉換至美國紐約時區
NYC_tz = tz.gettz('America/New_York')
NYC_tz
now_utc = datetime.now(tz.tzutc())
now_utc

now_utc.astimezone(NYC_tz)

# 範例-計算程式執行時間
from datetime import datetime
from numpy.random import default_rng

# 開始計算時間
starttime = datetime.now()
starttime

# 程式執行
rng = default_rng()
vals = []
x = abs(rng.standard_normal(100000000))
x[0:3]
vals = x**0.5
vals[0:3]

# 結束時間
endtime = datetime.now()
endtime

# 程式執行時間
print(endtime - starttime)

# 範例-時間運算
from datetime import datetime, timedelta
now = datetime.now()
now

tomorrow = timedelta(days=+1) # 本地時間加1天
now + tomorrow

delta = timedelta(days=+3, hours=-4) # # 本地時間加3天,減4小時
now + delta

# 實作練習14
# 檔案日期時間處理
# https://www.kaggle.com/shawon10/web-log-dataset
# 檔案名稱: weblog.csv
# 欄位個數:4
# 資料筆數:16007
# IP	Time	URL	Staus
# 10.128.2.1	[29/Nov/2017:06:58:55	GET /login.php HTTP/1.1	200
# 10.128.2.1	[29/Nov/2017:06:59:02	POST /process.php HTTP/1.1	302
# 10.128.2.1	[29/Nov/2017:06:59:03	GET /home.php HTTP/1.1	200
# 下載 https://github.com/rwepa/DataDemo/blob/master/weblog.csv

# 練習使用 open, read, datetime, re 等處理技術(不可使用 pandas),計算下列3個時段的資料筆數
# 06:00-14:00, 14:00-22:00, 22:00-06:00

##############################
# pandas 資料物件
##############################

# 10 minutes to pandas
# https://pandas.pydata.org/docs/user_guide/10min.html

# 載入2大套件 numpy, pandas
import numpy as np  # Python Scientific Computing Library
import pandas as pd # Python Data Analysis Library

##############################
# pandas 序列(Series)物件
##############################

# s = pd.Series(data, index=index)
# data 包括使用 array, Iterable, dict, scalar value
# 序列包括指標(Index) 與值(Value), 指標採用預設整數型態指標 0,1,2,...

# (1).Series - 使用 ndarray
s = pd.Series(data = np.random.randn(5), index=["a", "b", "c", "d", "e"])
s
# a   -0.492604
# b   -0.073386
# c   -0.063632
# d    0.197128
# e    0.178333
# dtype: float64
type(s) # pandas.core.series.Series

# (2).Series -使用 Iterable - 序列(tuple)
s1 = pd.Series((1,3,5,np.nan,6,8))
s1

# (3).Series - 使用 Iterable - 串列(List)
s2 = pd.Series([1,3,5,np.nan,6,8])
s2

s1 == s2 # equality 相等, 比較每個元素是否相同, 大部分使用此功能.
s1 is s2 # identity 相同, 比較二物件是否指向同一個記憶體

id(s1)
id(s2) # 與id(s1) 不相等

# "==" 與 "is" ("is not") 應用

# identity - 使用 id 函數, 查看說明 help(id). 相同程式 id 結果,每次不一定相同.
# https://realpython.com/python-is-identity-vs-equality/

a = 'Hello world'
b = 'Hello world'
a == b
a is b
id(a)
id(b)

# 整數 [-5 ~ 256] 會使用相同記憶體位址功能
a = 256
b = 256
a == b   # True
a is b   # True
id(a)
id(b)

a = 1000
b = 1000
a == b   # True
a is b   # False
id(a)
id(b)

x1 = np.nan
x2 = np.nan
id(x1)
id(x2) # 與上面結果相同
x1 == x2 # False
x1 is x2 # True

# (4).Series - 使用 Iterable - 字典(Dict)
# 在 pandas 模組之中, NaN 表示為 "not a number"
x = {"x1": 1, "x2": 2, "a": np.nan, "b": 3, "c": 4}
c = pd.Series(x)
c

# (5).Series - 使用 scalar value
pd.Series(999.0, index=["a", "b", "c", "d", "e"])

##############################
# Series 使用 ndarray-like 操作
##############################
c
# x1    1.0
# x2    2.0
# a     NaN
# b     3.0
# c     4.0
# dtype: float64

c[0]              # 1.0
c[1]              # 2.0
c[-1]             # 4.0
c[:3]
# x1    1.0
# x2    2.0
# a     NaN
# dtype: float64

c[c > c.median()]
c[[1, 3, 2]]
np.exp(c)
c.dtype

# Series.array 是 pandasExtensionArray.
# ExtensionArray 是包括一個或多個 numpy.ndarray 的 thin wrapper類別
c.array      # 將 series 轉換為 PandasArray

c1 = c.to_numpy() # 將 series 轉換為 NumPy ndarray
c1

c2 = c.to_numpy
c2

c1 == c2
c1 is c2

##############################
# Series 使用 dict-like 操作
##############################
c

c['x1']
c['a'] = np.pi

'x1' in c

c.get("a")
c.get("e") # None

##############################
# pandas 資料框(DataFrame)物件
##############################

# 方法1.建立指標與值,再合併為資料框

# 步驟1-建立 DatetimeIndex 物件
dates = pd.date_range('20210801', periods=6) # 日期指標
dates
type(dates)

# 步驟2-建立 DataFrame
# 欄位名稱: A, B, C, D
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df1
type(df1)

# 方法2.使用字典建立資料框
df2 = pd.DataFrame({ 'A' : 1.,
    'B' : pd.Timestamp('20210801'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })
df2

# dtypes: 顯示各欄位的資料型態
df2.dtypes

# 方法3.使用 list of dicts 建立資料框

# 預設指標
mydata = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
df3 = pd.DataFrame(mydata)
df3

# 客製化指標
df4 = pd.DataFrame(mydata, index=["first", "second"])
df4

# 方法4.使用 dict of tuples 建立資料框
# 使用 tuples dictionary, 可建立 MultiIndexed dataframe(階層式指標資料框)
df5 = pd.DataFrame(
    {
        ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},
        ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},
        ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
        ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
        ("b", "b"): {("A", "D"): 10, ("A", "B"): 11},
    }
)
df5
type(df5)

# 方法5.使用 list of dataclasses 建立資料框
# pandas 1.1.0 新增功能, 參考 PEP 557 -- Data Classes
# list of dataclasses 類似於 list of dictionaries
# https://www.python.org/dev/peps/pep-0557/

from dataclasses import make_dataclass
Mydata = make_dataclass("Stations", [("x", int), ("y", int)])
Mydata
df6 = pd.DataFrame([Mydata(0, 0), Mydata(0, 3), Mydata(2, 3), Mydata(1, 2)])
df6

##############################
# 資料檢視
##############################
np.random.seed(123)
dates = pd.date_range('20210801', periods=6) # 日期指標
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df1

# head 顯示前 5 筆資料, 此功能與 R 顯示 6 筆不相同.
df1.head()

df1.head(3) # 顯示前 3 筆資料

df1.tail()  # 顯示後 5 筆資料

# 顯示指標(index)
df1.index

# 欄名稱(columns)
df1.columns

# 資料值(values)
df1.values

# T 資料轉置, 類似將原本長資料 (Long data), 轉換為寬資料 (Wide data)
df1.T

##############################
# describe 統計摘要(statistic summary)
##############################

# count 個數
# mean 平均值
# std  標準差 standard deviation, 一般希望愈小愈好
# min  最小值
# 25%  25百分位數
# 50%  50百分位數, 中位數 median
# 75%  75百分位數 (quantile)
# max  最大值

df1.describe()

##############################
# 排序
##############################

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

# (1).排序 sort_index

# axis為排序的軸，0表示 rows index(列指標)，1表示 columns index(行指標)
# 當對資料"列" 進行排序時，axis必須設置為0.
# df.sort(["A"]) 新版不支援 sort 函數, 改用 sort_values 或 sort_index

# ascending =FALSE, 即遞增是FALSE, 表示遞減是TRUE, 結果為D,C,B,A
df1.sort_index(axis=1, ascending=False)

# (2).排序 sort_values

# 依照 B 欄大小, 由小至大排序 (預設值是遞增)
df1.sort_values(by='B')

# 依照 B 欄大小, 改為由大至小排序 (遞減)
df1.sort_values(by='B', ascending = False)

# 依照 B 欄大小, 將 nan 排在最前面或最後面
df1.iloc[2, 0] = np.nan
df1
df1.sort_values(by='A')
df1.sort_values(by='A', na_position = 'first')

# 實作練習15
# 使用 mydf 進行A欄位遞增, B欄位遞減排序
#    A   B   C
# 0  1  10  aa
# 1  2  24  bb
# 2  2  26  cc
# 3  4   9  dd
# 4  2  29  aa

##############################
# 資料列,行選取
##############################
import numpy as np
import pandas as pd
np.random.seed(123)
dates = pd.date_range('20210801', periods=6) # 日期指標
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df1

# 選取行
df1['A']
df1.A
df1[['A', 'B']]

# 選取列, df[1:4]選取第1至第3列(4-1=3), 此功能與 R 不同.
df1
df1[1:4]

# 使用 loc
df1.loc[:, ['A','B']]

# 使用 iloc
df1.iloc[2] # 指標為第2列

df1.iloc[2:4,]
df1.iloc[2:4, :]

df1.iloc[, 2]    # ERROR
df1.iloc[:, 2]   # OK
df1.iloc[:, 2:4] # OK

# Boolean Indexing 邏輯值(條件式)資料選取
df1.loc[dates[2]]
df1.loc['20210803']

df1.loc['20210803', ['A', 'B']]
df1.loc['20210802':'20210804', ['A', 'B']]

df1.iloc[[1,2,4],[0,2]] # 選取不連續範圍

df1.iloc[2,2]
df1.iat[2,2]

df1[df1 > 1.5]
df1[df1.A > 1.5]

# 使用 .isin - 範例1
df1[df1.index.isin(['2021-08-02', '2021-08-04'])]

# 使用 .isin - 範例2

df2 = df1.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2
df2[df2['E'].isin(['two','four'])]

# Missing Data 遺漏值 np.NaN (np.nan), R: 使用NA
df3 = df1.reindex(index=dates[0:4], columns=list(df1.columns) + ['E'])
df3.loc[dates[0]:dates[1],'E'] = 1
df3

# 判斷何者為NaN
pd.isnull(df3)

# 刪除列中包括 NaN
df3.dropna(how='any')

# 將遺漏值填入值
df3.fillna(value=999)

##############################
# 列,行的匯總計算
##############################
"""
A B C
1 5 
2 NaN 10
3 7 11
4 8 12
"""
df = pd.read_clipboard()
df
df.dtypes
df.isnull()

# 計算每行平均
df.mean()

# 計算每列平均
df.mean(1)

# apply 將資料套用至函數
df.apply(np.cumsum) # 各資料行累計加總

##############################
# 列合併 append, concat 
##############################

np.random.seed(123)
df = pd.DataFrame(np.random.randn(3, 4))
df

pieces = pd.DataFrame(np.random.randn(2, 4))
pieces

# append 列合併
df.append(pieces, ignore_index=True)

# concat 列合併, 類似 R的 rbind
pieces1 = pd.DataFrame(np.random.randn(2, 4))
pieces1

pd.concat([df, pieces, pieces1], ignore_index=True)

##############################
# Grouping 群組計算
##############################
# https://github.com/rwepa/DataDemo/blob/master/Cars93.csv

import pandas as pd
df = pd.read_csv('C:/mydata/Cars93.csv')
df

df = df[['Manufacturer', 'Price', 'AirBags', 'Horsepower', 'Origin']]

df.head()

df_AirBags = df.groupby('AirBags')
type(df_AirBags)

print(df_AirBags.groups)

# 群組 - 2個維度
df_AirBagsOrigin = df.groupby(['AirBags', 'Origin'])

# 群組大小
df_AirBagsOrigin.size()

# 篩選群組
df_AirBags.get_group('Driver & Passenger')

# 群組總和
df_AirBags.sum()

# 群組平均
df_AirBags.mean()

# agg - 每行計算min
df_AirBags.agg('min')

# agg - 每行計算max
df_AirBags.agg('max')

# 資料摘要
import pandas as pd
df = pd.read_csv('C:/mydata/Cars93.csv')
df

df.dtypes # object: 字串, float64: 含小數點數值

df.describe() # 無法顯示所有欄位
df.describe(include='all') # 顯示所有欄位

# 顯示所有資料
pd.set_option('display.max_rows', None, 'display.max_columns', None) # None 沒有限制
df.describe()
df

##############################
# 檔案匯入 pandas
##############################

# pandas IO 模組
# https://pandas.pydata.org/docs/user_guide/io.html

##############################
# 匯入 CSV 檔案
##############################

import pandas as pd
print(pd.__version__) # 1.2.4

# 下載 marketing.csv 至 C:\pythondata\data 資料夾
# https://github.com/rwepa/DataDemo/blob/master/marketing.csv

# 匯入資料
marketing = pd.read_csv('C:/mydata/marketing.csv')
marketing # 200*4

# 資料摘要
marketing.describe()

# 有NaN
marketing.isnull().sum()

marketing['facebook']

# 將 facebook 變數的 NaN資料, 以中位數填滿
marketing['facebook'].fillna(marketing['facebook'].median, inplace = True)

# 沒有NaN
marketing.isnull().sum()

print(marketing)
# RecursionError: maximum recursion depth exceeded

##############################
# 匯入 Excel 檔案
##############################

# 匯入 Excel 檔案, 全國訂單明細.xlsx
# https://github.com/rwepa/DataDemo/blob/master/全國訂單明細.xlsx

sales = pd.read_excel(io = 'C:/mydata/全國訂單明細.xlsx', sheet_name = '全國訂單明細')
sales # 8568*19
sales.head()

##############################
# 匯入 SAS 檔案
##############################

# 匯入 SAS 檔案, h_nhi_ipdte103.sas7bdat
# 資料說明: 103年模擬全民健保處方及治療明細檔_西醫住院檔
# 資料筆數: 14297
# 欄位個數: 80
# 檔案大小: 7.25MB
# https://github.com/rwepa/DataDemo/blob/master/h_nhi_ipdte103.sas7bdat

ipdate = pd.read_sas(filepath_or_buffer = 'C:/mydata/h_nhi_ipdte103.sas7bdat')
ipdate # 14297*80
ipdate.head()

##############################
# # 資料匯出
##############################
df = pd.DataFrame({'姓名': ['ALAN', 'LEE'],
                   '地址': ['台北市', '新北市'],
                   '年資': [10, 20]})
df
#      姓名   地址  年資
# 0  ALAN  台北市  10
# 1   LEE  新北市  20

df.to_csv('data/df.csv', index = False) # 中文亂碼

df.to_csv('data/df.csv', index = False, encoding = 'utf-8') # 中文亂碼

df.to_csv('data/df.csv', index = False, encoding = 'utf_8_sig') # OK



##############################
# 8/27(五) 05.MySQL與SQL語法,Python連結MySQL應用
##############################

##############################
# SQL語法
##############################

"""
SELECT VERSION(), CURRENT_DATE;

SELECT NOW();

SELECT power(2, 3)

-- 顯示資料庫
SHOW databases;

-- 使用資料庫
USE sakila;

-- 目前使用資料庫
SELECT DATABASE();

-- 顯示資料表
SHOW TABLES;

-- 資料表綱要
DESCRIBE rental;

-- 查詢資料
SELECT * FROM rental;

-- 筆數總計 16044
SELECt count(*) FROM rental;

-- GROUP BY
SELECT customer_id, count(customer_id) AS rental_count
FROM rental
GROUP BY customer_id;

SELECT date(rental_date) FROM rental;
-- end
"""

##############################
# Python連結MySQL應用
##############################

# 執行環境
# Anaconda3-2020.11-Windows-x86_64.exe
# mysql-installer-community-8.0.22.0.exe

# 下載 mysql-python 模組
# 方法1 (執行時會有ERROR)
# pip install mysql-connector-python

# 方法2 (採用此方法較佳)
# conda install -c conda-forge mysql-connector-python

# example 1 - 資料庫連結
import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password='123456',
                              host='127.0.0.1',
                              database='sakila')
cnx.close()

# example 2 - SELECT 範例
import mysql.connector

cnx = mysql.connector.connect(user='root', password='123456', database='sakila')
cursor = cnx.cursor()

query = "SELECT rental_id, rental_date, customer_id FROM rental"
cursor.execute(query)

# 取出第1筆, tuple
result1 = cursor.fetchone()
print(result1)

# 取出前6筆, list
result2 = cursor.fetchmany(6)
print(result2)

# 取得所有資料, list
result3 = cursor.fetchall()
print(result3)

# 關閉游標 True
cursor.close()

# 關閉資料庫連結
cnx.close()

##############################
# 實作練習參考說明
##############################
# 實作練習1
# 在 jupyter notebook 輸入以下程式碼練習
from numpy import *
random.rand(5,5)
# analysis: refer to materials

# 實作練習2
# 開啟下列 ipynb 檔案
# Python 程式設計-李明昌 <免費電子書>
# http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html
# analysis: refer to materials

# 實作練習3
# 熟悉自動換列等設定
# Tools \ Preferences \ Editor \ Display \ Wrap lines
# analysis: refer to materials

# 實作練習4
# 如何顯示list不以 __ 開始方法的總個數 11?
# analysis:
listmethod = dir(list)
newlist = [x for x in listmethod if "__" not in x]
newlist
len(newlist)

# 實作練習5
# 將 list 轉換為 dictionary
# 輸入: lst = ['a', 1, 'b', 2, 'c', 3]
# 結果: {'a': 1, 'b': 2, 'c': 3}
# analysis:    
# 方法1
def ListConvertDict(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

lst = ['a', 1, 'b', 2, 'c', 3]
print(ListConvertDict(lst))

# 方法2
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))

# 實作練習6
# 自訂模組, 計算商數與餘數
# 自訂模組檔案名稱為 numberscompute.py
# 練習檔案名稱為 mycompute.py
# analysis: refer to materials

# 實作練習7
# 使用 save 將 Numpy 陣列 a 儲存成外部檔案
# analysis:
# 步驟1
outputfile = 'myarray.npy'
with open(outputfile, 'wb') as fp:
    np.save(fp, a)

# 步驟2
# 使用 load 將外部檔案匯入至Numpy陣列
outputfile = "myarray.npy"
with open(outputfile, 'rb') as fp:
    mydata = np.load(fp)
print(mydata)

# 實作練習8
# 建立3維陣列 myzero, 5個元素, 每個元素為3列,4行的零矩陣
# myzero.shape 結果為 (5, 3, 4)
# analysis:
import numpy as np
myzero = np.zeros((5, 3, 4))
myzero
myzero.ndim
myzero.shape

# 實作練習9
# 計算 mystr 字串中, 不區分大小寫, 英文字母出前次數最多的前6名為何?
# analysis:
mystr = 'Scikit-learn is an Open source Machine Learning learning library that supports supervised and unsupervised learning.'
# 技巧: 使用 collections.Counter 方法

# 步驟1.轉換為 list
mylist_tmp = list(mystr)

# 步驟2.判斷是否為字母, 如果是字母, 轉換成小寫
mylist = []
for x in mylist_tmp:
    if x.isalpha():
        mylist.append(x.lower())
mylist

# 步驟3.使用 counter 計算字母發生次數並轉換為 dict
import collections
mycounter = collections.Counter(mylist)
mycounter
mycounter.keys()
mycounter.values()

# 步驟4.排序發生次數

# 最大值
max(mycounter, key=mycounter.get)

# 由小至大排序
sorted(mycounter, key=mycounter.get)

# 由大至小排序
sorted(mycounter, key=mycounter.get, reverse=True)

# 由大至小排序,並列出(key,value)結果, 最多為 n,e,i,r,s,a
mystrsort = sorted(mycounter.items(), key=lambda x: x[1], reverse=True)
mystrsort

# 答案為 n, e, i, r, s, a
mystrsort[0:6]

# 實作練習10
# 字串練習-match, fullmatch, search, findall
# 以 mystr 字串練習 learning 或 Learning
# analysis:
import re

mystr = 'Learning is the obtaining of new knowledge. Scikit-learn is an Open source Machine learning library that supports supervised and unsupervised learning'

wordRegex = '[lL]earning'

re.match(wordRegex, mystr)     # match='Learning'

re.fullmatch(wordRegex, mystr)

re.search(wordRegex, mystr)    # match='Learning'

re.findall(wordRegex, mystr)   # ['Learning', 'learning', 'learning']

# 實作練習11
# 以 mystr 字串練習, 使用 findall 找出所有股票代碼
# 結果為 ['2481-TW', '4952-TW', '3264-TW', '6531-TW']
mystr = '隨著歐美多國解封，燃油車、電動車市況明顯回溫，帶動車用電子強勁需求，相關零組件廠出貨也陸續報捷，車電族群今 (13) 日再度發動猛攻，包括強茂 (2481-TW)、凌通 (4952-TW)、欣銓 (3264-TW)、愛普 (6531-TW) 等多檔，盤中均亮燈漲停。'
# analysis:
stockRegex = re.compile(r'\d{4}-TW')
re.findall(stockRegex, mystr)

# 實作練習12
# for + continue 迴圈練習, 篩選出 list 的字串資料
# 提示: 使用 if, for, append, continue 順序非固定
# 結果 ['python', '123.45', 'RWEPA', 'R']
mylist = [1, 3, "python", '123.45', "RWEPA", 100, "R"]
# analysis:
result = []
for element in mylist:
        if type(element) != str:
            continue
        result.append(element)
result

# 實作練習13
# 使用 def 建立計算2點之間的直線距離函數
# 函數名稱 distance
# 引數名稱 x1, y1, x2, y2
# 不可使用 math.sqrt 函數
# 輸入第1個點的座標值為 (a, b)
# 輸入第2個點的座標值為 (c, d)
# analysis:
def distance(x1, y1, x2, y2):
    dist = ((c-a)**2 + (d-b)**2)**0.5
    return dist

a, b, c, d = eval(input())
distance(a, b, c, d)

# 實作練習14
# 檔案日期時間處理
# https://www.kaggle.com/shawon10/web-log-dataset
# 檔案名稱: weblog.csv
# 欄位個數:4
# 資料筆數:16007
# IP	Time	URL	Staus
# 10.128.2.1	[29/Nov/2017:06:58:55	GET /login.php HTTP/1.1	200
# 10.128.2.1	[29/Nov/2017:06:59:02	POST /process.php HTTP/1.1	302
# 10.128.2.1	[29/Nov/2017:06:59:03	GET /home.php HTTP/1.1	200
# 下載 https://github.com/rwepa/DataDemo/blob/master/weblog.csv
# 練習使用 open, read, datetime, re 等處理技術(不可使用 pandas),計算下列3個時段的資料筆數
# 06:00-14:00, 14:00-22:00, 22:00-06:00
# analysis: refer to materials and try it

# 實作練習15
# 使用 mydf 進行A欄位遞增, B欄位遞減排序
import pandas as pd
#    A   B   C
# 0  1  10  aa
# 1  2  24  bb
# 2  2  26  cc
# 3  4   9  dd
# 4  2  29  aa
# analysis:
mydf = pd.DataFrame(
    {'A': [1,2,2,4,2],
     'B': [10,24,26,9,29],
     'C': ['aa', 'bb', 'cc', 'dd', 'aa']})
mydf

mydf.sort_values(by=['A', 'B'], ascending = [True, False])

mydf.sort_values(by=['A', 'B'], ascending = [True, False],  inplace=True) # 更改 mydf 內容
# end

##############################
# 補充篇-行銷案例應用
##############################

# 線上交易銷售資料
# 下載網址：https://www.kaggle.com/vijayuv/onlineretail
# 下載檔名：OnlineRetail.csv.zip
# 檔案筆數：541909列
# 欄位數：8欄
# 解壓縮後檔名: OnlineRetail.csv
# 解壓縮後大小：43.4MB
# 參考資料：https://towardsdatascience.com/data-driven-growth-with-python-part-1-know-your-metrics-812781e66a5b

# 直接 github 下載
# https://github.com/rwepa/DataDemo/blob/master/OnlineRetail.csv.zip

##############################
# 安裝與載入套件
##############################
# conda install plotly

# 載入套件
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from plotly.offline import plot # method 1: plot(fig)
import plotly.express as px # method 2: fig.show()
import plotly.graph_objs as go

# 設定 plotly繪圖預設顯示於瀏覽器
import plotly.io as pio
pio.renderers.default='browser'

# 匯入CSV檔案
df = pd.read_csv('C:/mydata/OnlineRetail.csv')

# 前5筆資料
df.head(5)

# 後5筆資料
df.tail()

# 欄位名稱
df.columns

# 資料摘要-數值
df.describe()

# 資料摘要-類別
# Country 唯一值為38個
df.describe(include = 'object')

# 資料摘要-數值＋類別
df.describe(include = 'all')

# 找出有用的特徵(有意義的屬性)
# Customer ID
# Unit Price
# Quantity
# Invoice Date

# 將 InvoiceDate 欄位轉換為日期
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceDate']

# 新增評估欄位 InvoiceYearMonth 發票年月
df['InvoiceYearMonth'] = df['InvoiceDate'].map(lambda date: 100*date.year + date.month)
df['InvoiceYearMonth']

##############################
# 新增評估欄位 Revenue 收入
##############################

df['Revenue'] = df['UnitPrice'] * df['Quantity']
df['Revenue']

# 建立年月為群組,收入小計資料
df_revenue = df.groupby(['InvoiceYearMonth'])['Revenue'].sum().reset_index()
df_revenue

# 每月收入統計圖
plot_data = [
    go.Scatter(
        x=df_revenue['InvoiceYearMonth'],
        y=df_revenue['Revenue'],
    )
]

plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='圖1.每月收入統計圖')
fig = go.Figure(data=plot_data, layout=plot_layout)

# method 1
plot(fig)

# method 2
fig.show()

# 每月收入向上增加趨勢.
# 2011年2,4月達到最低點.

##############################
# 每月收入變化百分比
##############################

# 使用 pct_change() 函數計算"每月收入百分比變化"

df_revenue['MonthlyGrowth'] = df_revenue['Revenue'].pct_change()
df_revenue
# (560000.260-748957.020)/748957.020 = -0.252293

# 每月收入百分比變化統計圖
plot_data = [
    go.Scatter(
        x=df_revenue.query("InvoiceYearMonth < 201112")['InvoiceYearMonth'],
        y=df_revenue.query("InvoiceYearMonth < 201112")['MonthlyGrowth'],
    )
]

plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='圖2.每月收入百分比變化統計圖'
    )

fig = go.Figure(data=plot_data, layout=plot_layout)

fig.show()

##############################
# pandas 資料處理技巧
##############################

# 1.groupby 群組小計
# 2.rename 欄位重新命名
# 3.sort_values 排序

# 38個國家, 先考慮國家資料筆數最多者 - United Kingdom
df_country = df.groupby(['Country']).size().reset_index()
df_country

# 欄位重新命名
df_country.rename(columns={0:'Count'}, inplace=True)

# 排序
df_country.sort_values(by=['Count'], ascending=False)

# 建立篩選 United Kingdom 資料集
df_uk = df.query("Country=='United Kingdom'").reset_index(drop=True)
df_uk # 495478 rows × 10 columns

##############################
# 建立每月活動客戶數統計表
##############################

# nunique: Count distinct observations over requested axis.
df_monthly_active = df_uk.groupby('InvoiceYearMonth')['CustomerID'].nunique().reset_index()
df_monthly_active

# 每月活動客戶數長條圖
plot_data = [
    go.Bar(
        x=df_monthly_active['InvoiceYearMonth'],
        y=df_monthly_active['CustomerID'],
    )
]

plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='圖3.每月活動客戶數長條圖'
    )

fig = go.Figure(data=plot_data, layout=plot_layout)

fig.show()
# 2011年4月客戶數從3月的 923降低至 817, 減少 (817-923)/923 = -11.5%

##############################
# 每月每筆訂單平均收入
##############################

df_monthly_order_avg = df_uk.groupby('InvoiceYearMonth')['Revenue'].mean().reset_index()
df_monthly_order_avg

# 每月每筆訂單平均收入長條圖
plot_data = [
    go.Bar(
        x=df_monthly_order_avg['InvoiceYearMonth'],
        y=df_monthly_order_avg['Revenue'],
    )
]

plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='圖4.每月每筆訂單平均收入長條圖'
    )
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()

##############################
# 建立評估欄位: 新客戶, 舊客戶
##############################

# 建立第1次消費之客戶
# 以客戶編號為群組, 計算 Min{發票日期}
df_min_purchase = df_uk.groupby('CustomerID').InvoiceDate.min().reset_index()

# 修改欄位名稱
df_min_purchase.columns = ['CustomerID','MinPurchaseDate']
df_min_purchase

# 新增欄位 - 轉換日期格式: 西元年月
df_min_purchase['MinPurchaseYearMonth'] = df_min_purchase['MinPurchaseDate'].map(lambda date: 100*date.year + date.month)

df_min_purchase # 3950 rows × 3 columns

df_uk # 495478 rows × 10 columns

# 合併 {MinPurchaseDate, MinPurchaseYearMonth} 至 df_uk 之最右側

df_uk = pd.merge(df_uk, df_min_purchase, on='CustomerID')

df_uk # 361878 rows × 12 columns

# 建立評估欄位: 客戶型態 UserType, 預設值為 New
# 如果 InvoiceYearMonth 大於 MinPurchaseYearMonth,表示之前為現有客戶, 將 UserType 改為 Existing

df_uk['UserType'] = 'New'

df_uk.loc[df_uk['InvoiceYearMonth'] > df_uk['MinPurchaseYearMonth'], 'UserType'] = 'Existing'

# 新,舊客戶的每月收入小計

# 計算每月新舊客戶收入小計
df_user_type_revenue = df_uk.groupby(['InvoiceYearMonth','UserType'])['Revenue'].sum().reset_index()

# 篩選資料並刪除前,後資料
df_user_type_revenue = df_user_type_revenue.query("InvoiceYearMonth != 201012 and InvoiceYearMonth != 201112")
df_user_type_revenue

# 繪圖
plot_data = [
    go.Scatter(
        x=df_user_type_revenue.query("UserType == 'Existing'")['InvoiceYearMonth'],
        y=df_user_type_revenue.query("UserType == 'Existing'")['Revenue'],
        name = 'Existing'
    ),
    go.Scatter(
        x=df_user_type_revenue.query("UserType == 'New'")['InvoiceYearMonth'],
        y=df_user_type_revenue.query("UserType == 'New'")['Revenue'],
        name = 'New'
    )
]

plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='圖5.新,舊客戶的每月收入統計圖'
    )
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()

##############################
# 新客戶比率 (New Customer Ratio)
##############################

# 建立每月新客戶資料並刪除 NA
# 本例使用 unique 函數

df_user_ratio = df_uk.query("UserType == 'New'").groupby(['InvoiceYearMonth'])['CustomerID'].nunique()/df_uk.query("UserType == 'Existing'").groupby(['InvoiceYearMonth'])['CustomerID'].nunique()

# 設定 index
df_user_ratio = df_user_ratio.reset_index()

# 刪除 NA
df_user_ratio = df_user_ratio.dropna()

df_user_ratio

# 繪圖
# 考慮2月為新客戶,因此比例較高.

plot_data = [
    go.Bar(
        x=df_user_ratio.query("InvoiceYearMonth>201101 and InvoiceYearMonth<201112")['InvoiceYearMonth'],
        y=df_user_ratio.query("InvoiceYearMonth>201101 and InvoiceYearMonth<201112")['CustomerID'],
    )
]

plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='圖6.新客戶比率統計圖'
    )
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()

##############################
# 每月客戶保留率 (Monthly Retention Rate)
##############################

# 每月客戶保留率=上個月以前保留的客戶/總活躍客戶數

# 計算活躍客戶數, 依據 {CustomerID, InvoiceYearMonth}為群組, 計算收入總計.

df_user_purchase = df_uk.groupby(['CustomerID','InvoiceYearMonth'])['Revenue'].sum().reset_index()
df_user_purchase

# 使用 crosstab (交叉表) 建立客戶保留矩陣, crosstab 預設使用"發生次數"

df_retention = pd.crosstab(df_user_purchase['CustomerID'], df_user_purchase['InvoiceYearMonth']).reset_index()

df_retention

# 建立字典物件, 記錄月份, 總活躍客戶數, 保留客戶數
months = df_retention.columns[2:]
retention_array = []

for i in range(len(months)-1):
    retention_data = {}
    selected_month = months[i+1]
    prev_month = months[i]
    retention_data['InvoiceYearMonth'] = int(selected_month)
    retention_data['TotalUserCount'] = df_retention[selected_month].sum()
    retention_data['RetainedUserCount'] = df_retention[(df_retention[selected_month]>0) & (df_retention[prev_month]>0)][selected_month].sum()
    retention_array.append(retention_data)
retention_array

# 轉換為資料框
df_retention = pd.DataFrame(retention_array)
df_retention

# 計算保留率
df_retention['RetentionRate'] = df_retention['RetainedUserCount']/df_retention['TotalUserCount']
df_retention

# 繪圖
plot_data = [
    go.Scatter(
        x=df_retention.query("InvoiceYearMonth<201112")['InvoiceYearMonth'],
        y=df_retention.query("InvoiceYearMonth<201112")['RetentionRate'],
        name="organic"
    )
    
]

plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='圖7.每月客戶保留率統計圖'
    )
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()

# 參考資料 -----

# RWEPA
# http://rwepa.blogspot.com/

# Python 程式設計-李明昌 <免費電子書>
# http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html

# R入門資料分析與視覺化應用教學(付費)
# https://mastertalks.tw/products/r?ref=MCLEE

# R商業預測與應用(付費)
# https://mastertalks.tw/products/r-2?ref=MCLEE
# end
# 辛苦啦,Python程式之旅完成 ~~
