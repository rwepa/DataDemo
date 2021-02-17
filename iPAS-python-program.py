"""
title   : iPAS-python-program
author  : Ming-Chang Lee
email   : alan9956@gmail.com
RWEPA   : http://rwepa.blogspot.tw/
Date    : 2020.11.18
Updated : 2021.1.28 -新增 10.Python連結MySQL
Updated : 2021.2.17 -新增 11.Python物件導向
"""

# 經濟部 iPAS 巨量資料分析師認證-Python學習參考資料
# https://www.ipas.org.tw/bda/AbilityIndex.aspx

##############################
# 大綱
##############################

# 01.資料型態與基本運算
# 02.字串處理
# 03.Numpy資料結構
# 04.Pandas資料結構
# 05.流程控制與物件導向觀念
# 06.資料載入及匯出
# 07.資料變形、排序與清理
# 08.探索式資料分析(含繪圖中文字型)
# 09.MySQL常用語法
# 10.Python連結MySQL
# 11.Python物件導向

# anaconda
# https://www.anaconda.com/

# 切換工作目錄
import os # 載入 os 套件
os.getcwd() # 讀取工作目錄
os.chdir("C:/pythondata") # 變更工作目錄
os.getcwd()
os.listdir(os.getcwd()) # 顯示檔案清單

# 顯示模組提供之函數
dir(os)

# jupyter notebook – 更改預設目錄
"""
cd C:\
jupyter-notebook
"""

# Jupyter Notebook 行號重新計算
# Kernel / Restart & Run All

# Python程式設計-李明昌.ipynb
# http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html

# Tools \ Preferences \ Keyboard shortcuts
# editor: run slection: F9        --> Ctrl + Return
# editor: run cell: Ctrl + Return --> F9

##############################
# 01.資料型態與基本運算.py
##############################

# 變數

# 合法
大數據 = 1 # 中文亦可,建議不要使用
CustomerSaleReport = 1
_CustomerSaleReport = 1
Customer_Sale_Report = 1
customer_sale_report = 1

# 不合法
$CustomerSaleReport = 1 # SyntaxError: invalid syntax
2020_sale = 100 # SyntaxError: invalid decimal literal
break = 123 # SyntaxError: invalid syntax

# 內建保留字
dir(__builtins__)
len(dir(__builtins__)) # 159

# 資料型態
# https://docs.python.org/3/library/stdtypes.html

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
a = 4 << 3 # 0100 --> 0100000, 64 32 16 8 4 2 0
b = a * 4.5
c = (a+b)/2.5
a = "Hello World"

# Tuples 序列 (元組)

f = (2,3,4,5) # A tuple of integers
# g = (,) 	 # error code
g = ()
h = (2, [3,4], (10,11,12)) 	# A tuple containing mixed objects

# Tuples的操作
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

# Tuple Operations
("chapter",8) + ("strings","tuples","lists")

2*(3,"blind","mice")

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

# Tuple Comparison Operations
# standard comparisons ‘<’, ‘<=’, ‘>’, ‘>=’, ‘==’, ‘!=’, in, not in

# Lists 串列
# 任意物件的串列
a = [2, 3, 4]            # A list of integer
b = [2, 7, 3.5, "Hello"] # A mixed list
c = []	                 # An empty list
d = [2, [a, b]]	         # A list containing a list

len(d)
d[0]
d[1]

# 串列的操作
x = a[1] 	   # Get 2nd element (0 is first)
y = b[1:3] 	   # Return a sub-list
z = d[1][0][2] # Nested lists
b[0] = 42 	   # Change an element

# 串列的結合與重複
e = a + b			     # Join two lists
e

f = e*3                  # repeat lists
f

# 附加元素
# append 
a.append('BigData')
a

# extend
a.extend(['Python', 'R', "Julia"])
a

# 插入元素
a.insert(2, 999)
a

# 刪除元素
del a[4]
a

del a
print(a)

# 顯示方法
print(dir(list))

# Set 集合
# https://docs.python.org/3/tutorial/datastructures.html#sets
# 集合與字典相似, 但字典沒有key,只有值
a = set() 			# An empty set
type(a)

b = {"台北市", "新北市", "桃園市", "台中市", "台北市", "新北市", "高雄市"}
b # {'台中市', '台北市', '新北市', '桃園市', '高雄市'}

# 集合運算
x = {1,2,3,4,5}
y = {1,3,5,7}
x & y # {1, 3, 5}
x | y # {1, 2, 3, 4, 5, 7}
x ^ y # {2, 4, 7}

# Dictionaries 字典
a = {}  # An empty dictionary
type(a) # dict
b = { 'x': 3, "y": 4 }
c = { "uid": 168,
	   "login": "marvelous",
	   "name" : 'Alan Lee'
	 }

u = c["uid"] 		        # Get an element
c["shell"] = "/bin/sh" 	    # Add an element

if c.has_key("directory"): 	# 'dict' object has no attribute 'has_key'
	d = c["directory"]
else:
	d = None
 
if "directory" in c:   # v3.x 直接使用 in
    d = c["directory"]
else:
    d = None
    
if "uid" in c:         # v3.x 直接使用 in
    d = c["uid"]
else:
    d = None

d = c.get("directory", None) # 較簡潔

d = c.get("uid", None) # 較簡潔

##############################
# 02.字串處理
##############################

# 字串 (String)由一許多字元所組成
# 字串左右二側須使用單引號或是雙引號

# 字串物件 https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# 字串方法 https://docs.python.org/3/library/string.html

city = '苗栗縣'
district = '造橋鄉'
road = '學府路168號'

# 使用 + 字串串接
city + district

address = city + district + road
address

# 數值轉換為字串
myinteger = 123
mystr = str(myinteger)
mystr

# len 長度
len(address)

# split 分割字串
address = city + ',' + district + ',' + road
address
address.split(',')

# replace 取代字串
address.replace(',', '')

# find 搜尋
mystr = 'Scikit-learn is an open source machine learning library that supports supervised and unsupervised learning.'

# find 回傳字串的索引, 找不到回傳-1
mystr.find('learning') # 39
mystr.find('bigdata') # -1

mystr.index('learning') # 39
mystr.index('bigdata') # ValueError: substring not found

# rfind 從最後面查詢
mystr.rfind('learning') # 98

##############################
# 03.Numpy資料結構
##############################

# NumPy 模組
import numpy as np

# 使用串列與元組建立一維陣列
a = np.array([1, 2, 3, 4, 5])
b = np.array((1, 2, 3, 4, 5))

print(type(a))
print(type(b))

print(a[0], a[1], a[2], a[3])

b[0] = 5    
print(b) 

b[4] = 0
print(b)

# 使用巢狀清單建立二維陣列
a = np.array([[1,2,3],[4,5,6]])
print(type(a))

print(a[0, 0], a[0, 1], a[0, 2])

print(a[1, 0], a[1, 1], a[1, 2])

a[0, 0] = 6
a[1, 2] = 1
print(a)

# 使用 save 將Numpy陣列儲存成外部檔案
outputfile = 'myarray.npy'
with open(outputfile, 'wb') as fp:
    np.save(fp, a)

# 使用 load 將外部檔案匯入至Numpy陣列
outputfile = "myarray.npy"
with open(outputfile, 'rb') as fp:
    mydata = np.load(fp)
print(mydata)

# 亂數函數

# 設定亂數函數的種子, 須輸入 >= 1 的整數
np.random.seed(123)

# random() 產生0.0~1.0之間的亂數
x1 = np.random.random()
x2 = np.random.random()
print(x1,x2)

# randint(min, max, size) 產生min~max之間的整數亂數, 不含max
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html

x3 = np.random.randint(5, 10)
x4 = np.random.randint(1, 101)
print(x3, x4)

x5 = np.random.randint(5, 21, size=3)
print(x5)

x6 = np.random.randint(1, 11, size=(4, 5))
print(x6)

# rand() 產生亂數值的陣列
a = np.random.rand(5)
print(a)

b = np.random.rand(5, 4)  
print(b)

# 常數 Constants
np.NAN

# NaN and NAN are equivalent definitions of nan. 
# Please use nan instead of NAN.
# 新版本使用 nan
np.nan

np.pi

np.e

a = np.array([30, 45, 60, 90])
np.sin(a*np.pi/180)

# 陣列的屬性

a = np.array([0,1,2,3,4,5])
a
a.ndim   # 1
a.shape  # (6,)

# 建立副本, b之修改會影響a
b = a.reshape((3,2))
b
b.ndim   # 2
b.shape  # (3,2)

b[1][0] = 168
b
a # a物件已經更改, array([  0,   1, 168,   3,   4,   5])

c = a.reshape((3,2)).copy()
c
c[0][0] = -999
c
a # a物件沒有更改

# reshape 應用
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

# 向量化處理
a = np.array([0,1,1,2,3,5])

a*2

a**3 # 次方運算

# indexing

a[np.array([1,3,5])]

# 離群值調整
a = a**3
a > 10
a[a > 10]
a[a > 10] = 10
a

a.clip(0, 3)

# nan 處理
x = np.array([1, 2, 3, np.NAN, 4])
x
np.isnan(x)

x[~np.isnan(x)]

np.mean(x[~np.isnan(x)])

np.mean(x) # nan

# 計算時間
import timeit
import numpy as np

normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000)
naive_np_sec = timeit.timeit('sum(na*na)', setup="import numpy as np; na=np.arange(1000)", number=10000)
good_np_sec = timeit.timeit('na.dot(na)', setup="import numpy as np; na=np.arange(1000)", number=10000)

print("Normal Python: %f sec"%normal_py_sec)
print("Naive NumPy: %f sec"%naive_np_sec)
print("Good NumPy: %f sec"%good_np_sec)

print "Hello World"    # python 2, Python 3 with ERROR
print("Hello World")   # python 3

##############################
# 04.Pandas資料結構
##############################

# 載入2大套件 pandas, numpy
# https://pandas.pydata.org/docs/user_guide/10min.html

import pandas as pd # Python Data Analysis Library
import numpy as np # Python Scientific Computing Library 

# 序列(Series)物件
# 使用串列(List)建立序列物件
# 序列包括指標(Index) 與值(Value), 指標採用預設整數型態指標
s = pd.Series([1,3,5,np.nan,6,8])
s
type(s)

# 使用陣列建立資料框(DataFrame)
dates = pd.date_range('20200801', periods=6) # 日期指標
dates
type(dates)

# 資料框(DataFrame)物件
# 欄位名稱: A, B, C, D
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df1
type(df1)

# 使用字典建立資料框 DataFrame
df2 = pd.DataFrame({ 'A' : 1.,
    'B' : pd.Timestamp('20190101'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })
df2

# dtypes: 表示資料型態
df2.dtypes # df2. 按 [Tab] 按鈕

# Viewing Data 資料檢視
df1

# head 顯示前 5 筆資料, 此功能與 R 顯示 6 筆不相同.
df1.head()

df1.head(3)

df1.tail()

# 顯示指標(index)
df1.index

# 欄名稱(columns)
df1.columns

# 資料值(values)
df1.values

# describe 統計摘要(statistic summary)
# count 個數
# mean 平均值
# std  標準差 standard deviation, 一般希望愈小愈好
# min  最小值
# 25%  25百分位數
# 50%  50百分位數, 中位數 median
# 75%  75百分位數 (quantile)
# max  最大值

df1.describe()

# 排序 sort_values()
# axis為排序的軸，0表示 rows index(列指標)，1表示columns index(行指標)
# 當對數據 "列" 進行排序時，axis必須設置為0.
# df.sort(["A"]) 新版不支援 sort, 改用 sort_values 或 sort_index

# ascending =FALSE, 即遞增是FALSE, 表示遞減是TRUE, 結果為D,C,B,A
df1.sort_index(axis=1, ascending=False)

# 依照 B 欄大小, 由小至大排序
df1.sort_values(by='B')

# 選取行
df1['A']
df1.A

# 選取列, 此功能與 R 不同, R: df[1:4] 表示選取第1至第4行
df1
df1[1:4]

# 使用 loc
df1.loc[:, ['A','B']]

# 使用 iloc
df1.iloc[2] # 指標為第2列

df1.iloc[2:4,]
df1.iloc[2:4, :]

df1.iloc[, 2] # ERROR
df1.iloc[:, 2] # OK
df1.iloc[:, 2:4] 

# Boolean Indexing 邏輯值(條件式)資料選取
df1[df1 > 0]
df1[df1.A > 0]

# 使用 .isin
df1[df1.index.isin(['2020-08-02', '2020-08-04'])]

# 建立資料框
df2 = df1.reindex(index=dates[0:4], columns=list(df1.columns) + ['E'])
df2

# Missing Data 遺漏值 NaN, R: 使用NA
df2.loc[dates[0]:dates[1],'E'] = 1
df2

# 刪除列中包括 NaN
df2.dropna(how='any')

# 將遺漏值填入值
df2.fillna(value=999)

# 判斷何者為NaN
pd.isnull(df2)

# 計算每行平均
df2.mean()

# 計算每列平均
df2.mean(1)

# Apply 將資料套用至函數
df2.apply(np.cumsum)

# Merge 合併
df = pd.DataFrame(np.random.randn(10, 4))
df

pieces = [df[:3], df[4:7], df[8:]]
pieces

# 列合併, 類似 R的 rbind
pd.concat(pieces)

# Grouping 群組計算
df = pd.DataFrame({
    'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C' : np.random.randn(8),
    'D' : np.random.randn(8)})
df

df.groupby('A').sum() # 類似 R- aggregate

df.groupby(['A','B']).sum()

# 繪圖
ts = pd.Series(np.random.randn(1000), 
               index=pd.date_range('1/1/2000', periods=1000))
ts

ts = ts.cumsum()

ts.plot()

##############################
# 05.流程控制與物件導向觀念
##############################

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

#================
# Functions 函數
#================
# Return the remainder of a/b
def remainder(a,b):
	q = a/b
	r = a - q*b
	return r

# Now use it
a = remainder(42,5) 	# a = 2

# Return two values
def divide(a,b):
	q = a/b
	r = a - q*b
	return q,r

x,y = divide(42,5) 		# x = 8, y = 2

# 檔案處理

# 1.檔案的讀取/寫入
f = open("foo","w") 	# Open a file for writing
f.write("Hello World")
f.close()

g = open("foo","r") 	# Open a file for reading
data = g.read() 		# Read all data
data

g = open("foo","r")
line = g.readline() 	# Read a single line
line

g = open("foo","r")
lines = g.readlines() # Read data as a list of lines
lines

# 2.使用%來格式化字串
for i in range(0,10):
	f.write("2 times %d = %d\n" % (i, 2*i))

for i in range(0,10):
	print("2 times %d = %d\n" % (i, 2*i))

# 物件導向
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
# 06.資料載入及匯出
##############################

# pandas IO 模組
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

# 匯入 CSV 檔案
import pandas as pd

# 使用 [CTRL] + 左鍵 --> Raw --> 下載 marketing.csv 至 C:\pythondata\data 資料夾
# https://github.com/rwepa/DataDemo/blob/master/marketing.csv

# 匯入資料
# 加上角選取 C:\pythondata 資料夾
marketing = pd.read_csv('data/marketing.csv')
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

marketing

# 匯入 Excel 檔案, 全國訂單明細.xlsx
# https://github.com/rwepa/DataDemo/blob/master/全國訂單明細.xlsx

sales = pd.read_excel(io = 'data/全國訂單明細.xlsx', sheet_name = '全國訂單明細')
sales # 8568*19
sales.head()

# 匯入 SAS 檔案, h_nhi_ipdte103.sas7bdat
# 資料說明: 103年模擬全民健保處方及治療明細檔_西醫住院檔
# 資料筆數: 14297
# 欄位個數: 80
# 檔案大小: 7.25MB
# https://github.com/rwepa/DataDemo/blob/master/h_nhi_ipdte103.sas7bdat

ipdate = pd.read_sas(filepath_or_buffer = 'data/h_nhi_ipdte103.sas7bdat')
ipdate # 14297*80
ipdate.head()

# 資料匯出
df = pd.DataFrame({'姓名': ['ALAN', 'LEE'],
                   '地址': ['台北市', '新北市'],
                   '年資': [10, 20]})
df
#      姓名   地址  年資
# 0  ALAN  台北市  10
# 1   LEE  新北市  20

df.to_csv('data/df.csv', index = False) # Windows 中文亂碼

df.to_csv('data/df.csv', index = False, encoding = 'utf-8') # 中文亂碼

df.to_csv('data/df.csv', index = False, encoding = 'utf_8_sig') # OK

##############################
# 07.資料變形,排序與清理
##############################

import pandas as pd
import numpy as np

# pandas.DataFrame.pivot
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html

df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
df
#    foo bar  baz zoo
# 0  one   A    1   x
# 1  one   B    2   y
# 2  one   C    3   z
# 3  two   A    4   q
# 4  two   B    5   w
# 5  two   C    6   t

# DataFrame.pivot(index=None, columns=None, values=None)
df.pivot(index='foo', columns='bar', values='baz')
# bar  A  B  C
# foo         
# one  1  2  3
# two  4  5  6

df.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
#     baz       zoo      
# bar   A  B  C   A  B  C
# foo                    
# one   1  2  3   x  y  z
# two   4  5  6   q  w  t

# pandas.DataFrame.pivot_table
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html

df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two", "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small", "small", "large", "small", "small", "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
df
#      A    B      C  D  E
# 0  foo  one  small  1  2
# 1  foo  one  large  2  4
# 2  foo  one  large  2  5
# 3  foo  two  small  3  5
# 4  foo  two  small  3  6
# 5  bar  one  large  4  6
# 6  bar  one  small  5  8
# 7  bar  two  small  6  9
# 8  bar  two  large  7  9

table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum)
table
# C        large  small
# A   B                
# bar one    4.0    5.0
#     two    7.0    6.0
# foo one    4.0    1.0
#     two    NaN    6.0

# 資料變形-寬資料轉換為長資料

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})
df
#    A  B  C
# 0  a  1  2
# 1  b  3  4
# 2  c  5  6

# 識別變數為A,轉換值變數為B
df.melt(id_vars=['A'], value_vars=['B'])
#    A variable  value
# 0  a        B      1
# 1  b        B      3
# 2  c        B      5

# 識別變數為A,自訂轉換後變數名稱
df.melt(id_vars=['A'], value_vars=['B'],
        var_name='myVarname', value_name='myValname')
#    A myVarname  myValname
# 0  a         B          1
# 1  b         B          3
# 2  c         B          5

# 識別變數為A,轉換值變數為B, C
longdf = df.melt(id_vars=['A'], value_vars=['B', 'C'])
longdf
#    A variable  value
# 0  a        B      1
# 1  b        B      3
# 2  c        B      5
# 3  a        C      2
# 4  b        C      4
# 5  c        C      6

# 資料變形-長資料轉換為寬資料
longdf.pivot(index='A', columns='variable', values='value')
# variable  B  C
# A             
# a         1  2
# b         3  4
# c         5  6

# 排序-預設值遞增
longdf.sort_values('value')
#    A variable  value
# 0  a        B      1
# 3  a        C      2
# 1  b        B      3
# 4  b        C      4
# 2  c        B      5
# 5  c        C      6

# 排序-遞減
longdf.sort_values('value', ascending=False)
#    A variable  value
# 5  c        C      6
# 2  c        B      5
# 4  b        C      4
# 1  b        B      3
# 3  a        C      2
# 0  a        B      1

# 排序-2個以上欄位
longdf.sort_values(['A','variable','value'])
#    A variable  value
# 0  a        B      1
# 3  a        C      2
# 1  b        B      3
# 4  b        C      4
# 2  c        B      5
# 5  c        C      6

# 內插法 interpolate
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html

# 範例1
s = pd.Series([0, 1, np.nan, 2])
s
# 0    0.0
# 1    1.0
# 2    NaN
# 3    2.0
# dtype: float64

s.interpolate()
# 0    0.0
# 1    1.0
# 2    1.5
# 3    2.0
# dtype: float64

# 範例2 - 設定最多填補二個連續 NaN
s = pd.Series([np.nan, "single_one", np.nan,
               "fill_two_more", np.nan, np.nan, np.nan,
               4.71, np.nan])
s
# 0              NaN
# 1       single_one
# 2              NaN
# 3    fill_two_more
# 4              NaN
# 5              NaN
# 6              NaN
# 7             4.71
# 8              NaN
# dtype: object

s.interpolate()

s.interpolate(method='pad', limit=2) # pad為最近值
# 0              NaN
# 1       single_one
# 2       single_one
# 3    fill_two_more
# 4    fill_two_more
# 5    fill_two_more
# 6              NaN
# 7             4.71
# 8             4.71
# dtype: object

# 範例3 - 使用多項式法, 參考 scipy模組
s = pd.Series([0, 2, np.nan, 8])
s
# 0    0.0
# 1    2.0
# 2    NaN
# 3    8.0

s.interpolate(method='polynomial', order=2)
# 0    0.000000
# 1    2.000000
# 2    4.666667
# 3    8.000000
# dtype: float64

##############################
# 08.探索式資料分析
##############################

# matplotlib
import matplotlib.pyplot as plt
import numpy as np

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 半徑 0~15

# 散佈圖 plt.scatter
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.savefig('random.plot.png')
plt.savefig('random.plot.pdf')
plt.show()

plt.scatter(x, y, s=500, c=colors, alpha=0.5)
plt.show()

# 線圖 plt.plot
plt.plot(x,y)

plt.plot(sorted(x), y)

# example 1 - 線圖
plt.plot([1,2,3,4])   # x 軸: 0,1,2,3
plt.ylabel("Quality")
plt.show()

# example 2 - 點圖
plt.plot([1,2,3,4], [1,4,9,16], 'ro')  # r:red, o:circle marker
plt.axis([0, 6, 0, 20]) # set xlim and ylim
plt.show()

# example 3 - 3組資料
t = np.arange(0., 5., 0.2) # 等差級數, 區間包括啟始, 不包括結束
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# example 4
plt.figure(1)                # the first figure

# 211: (nrow, ncol, plot_number) 
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])

plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title

# example 5
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# example 6 直方圖 (histogram)
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(123)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(50, 0.025, r'$\mu=100,\ \sigma=15$', size = 50)
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()

# example 7 多列多行繪圖
fig = plt.figure()

# subplot:設定圖形位置(列,行,編號)
# fig.add_subplot(221)   #top left
# fig.add_subplot(222)   #top right
# fig.add_subplot(223)   #bottom left
# fig.add_subplot(224)   #bottom right 
# plt.show()

# plt.subplot()
# subplot(232) # 2列, 3行, 圖2位置
# 圖1 , 圖2 , 圖3
# 圖4 , 圖5 , 圖6

# example 8 Windows 中文字型解決方案
import os
os.getcwd()
os.chdir("C:/pythondata")

import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

##############################
# Windows 中文字型
##############################

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\mingliu.ttc", size=12)

# 匯入資料
# https://github.com/rwepa/DataDemo/blob/master/web_traffic.csv

myData = sp.genfromtxt("web_traffic.csv", delimiter = '\t')
myData = np.genfromtxt("web_traffic.csv", delimiter = '\t')

print(myData[:6])
myData.ndim # 2個維度
myData.shape # same as print(myData.shape) 743*2

x = myData[:,0] # 743*1
y = myData[:,1] # 743*1

# 檢查是否有Na
sp.sum(sp.isnan(y)) # 有8個值是nan
print("Number of invalid entries:", sp.sum(sp.isnan(y)))

# 取出非Na
x = x[~sp.isnan(y)] # 743-8=735
y = y[~sp.isnan(y)]

# 繪圖
plt.scatter(x, y, s=10)
plt.title(u"2017年10月每小時網路流量", fontproperties=font) # 中文顯示
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)

# 加上網格線
plt.grid(True, linestyle='-', color='0.75')

# 輸出 png
plt.savefig(u"2017年10月每小時網路流量.png", dpi=300, format="png")
plt.show()

##############################
# Mac 中文字型
##############################

# import matplotlib
# print(matplotlib.matplotlib_fname())
# /Users/rwepa/opt/anaconda3/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc

# 編輯 matplotlibrc, 最底下新增3行指令
# font.family: sans-serif
# font.sans-serif: Arial Unicode MS, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
# axes.unicode_minus: False

# 刪除暫存檔
# rm -rf ~/.matplotlib/*
# 重新啟動 Spyder

# Mac 標題修正如下即可正常顯示中文
# plt.title("2017年10月每小時網路流量")

#plt.xticks() :設定x軸刻度, e.g. plt.xticks([10,20,30,40,50])
#plt.yticks() :設定y軸刻度

# color
"""
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
"""
#https://matplotlib.org/users/colors.html

# line style or marker
"""
'-'	  solid line style
'--'	  dashed line style
'-.'	  dash-dot line style
':'	  dotted line style
'.'	  point marker
','	  pixel marker
'o'	  circle marker
'v'	  triangle_down marker
'^'	  triangle_up marker
'<'	  triangle_left marker
'>'	  triangle_right marker
'1'	  tri_down marker
'2'	  tri_up marker
'3'	  tri_left marker
'4'	  tri_right marker
's'	  square marker
'p'	  pentagon marker
'*'	  star marker
'h'	  hexagon1 marker
'H'	  hexagon2 marker
'+'	  plus marker
'x'	  x marker
'D'	  diamond marker
'd'	  thin_diamond marker
'|'	  vline marker
'_'	  hline marker
"""
# http://matplotlib.org/users/pyplot_tutorial.html

# 水雷 vs. 岩石 視覺化分析

import pandas as pd
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# 資料有 208列, 61行
# X: V0-V59
# Y: V60
# 第61行: R: rock  岩石
# 第61行: M: mine 水雷
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")
rocksVMines
#          V0      V1      V2      V3      V4  ...     V56     V57     V58     V59  V60
# 0    0.0200  0.0371  0.0428  0.0207  0.0954  ...  0.0180  0.0084  0.0090  0.0032    R
# 1    0.0453  0.0523  0.0843  0.0689  0.1183  ...  0.0140  0.0049  0.0052  0.0044    R
# 2    0.0262  0.0582  0.1099  0.1083  0.0974  ...  0.0316  0.0164  0.0095  0.0078    R
# 3    0.0100  0.0171  0.0623  0.0205  0.0205  ...  0.0050  0.0044  0.0040  0.0117    R
# 4    0.0762  0.0666  0.0481  0.0394  0.0590  ...  0.0072  0.0048  0.0107  0.0094    R
# ..      ...     ...     ...     ...     ...  ...     ...     ...     ...     ...  ...
# 203  0.0187  0.0346  0.0168  0.0177  0.0393  ...  0.0065  0.0115  0.0193  0.0157    M
# 204  0.0323  0.0101  0.0298  0.0564  0.0760  ...  0.0034  0.0032  0.0062  0.0067    M
# 205  0.0522  0.0437  0.0180  0.0292  0.0351  ...  0.0140  0.0138  0.0077  0.0031    M
# 206  0.0303  0.0353  0.0490  0.0608  0.0167  ...  0.0034  0.0079  0.0036  0.0048    M
# 207  0.0260  0.0363  0.0136  0.0272  0.0214  ...  0.0040  0.0036  0.0061  0.0115    M

# print head and tail of data frame
print(rocksVMines.head())
rocksVMines.tail()

# print summary of data frame
summary = rocksVMines.describe()
print(summary)
#                V0          V1          V2  ...         V57         V58         V59
# count  208.000000  208.000000  208.000000  ...  208.000000  208.000000  208.000000
# mean     0.029164    0.038437    0.043832  ...    0.007949    0.007941    0.006507
# std      0.022991    0.032960    0.038428  ...    0.006470    0.006181    0.005031
# min      0.001500    0.000600    0.001500  ...    0.000300    0.000100    0.000600
# 25%      0.013350    0.016450    0.018950  ...    0.003600    0.003675    0.003100
# 50%      0.022800    0.030800    0.034300  ...    0.005800    0.006400    0.005300
# 75%      0.035550    0.047950    0.057950  ...    0.010350    0.010325    0.008525
# max      0.137100    0.233900    0.305900  ...    0.044000    0.036400    0.043900

#平行座標軸 Parallel coordinates graph
for i in range(208):
    # assign color based on color based on "M" or "R" labels
    if rocksVMines.iat[i,60] == "M":
        pcolor = "red"
    else:
        pcolor = "blue"

    # plot rows of data as if they were series data
    dataRow = rocksVMines.iloc[i, 0:60]
    plot.rcParams["figure.figsize"] = (20, 15) #(寬, 高)
    dataRow.plot(color=pcolor, alpha=0.5)
    # plot.figure(figsize=(16, 16))

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()

# 散佈圖矩陣 scatter_matrix{pandas}
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np

df = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])

# diagonal matrix with histogram
scatter_matrix(df)

scatter_matrix(df, alpha=0.2, figsize=(6, 6))

# diagonal matrix with kernel density estimation
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')

# 散佈圖矩陣 pairplot {seaborn}
# https://seaborn.pydata.org/
# seaborn-data: https://github.com/mwaskom/seaborn-data

# 安裝 seaborn 模組
import seaborn as sns

sns.set(style="ticks")

df = sns.load_dataset("iris")
df
#      sepal_length  sepal_width  petal_length  petal_width    species
# 0             5.1          3.5           1.4          0.2     setosa
# 1             4.9          3.0           1.4          0.2     setosa
# 2             4.7          3.2           1.3          0.2     setosa
# 3             4.6          3.1           1.5          0.2     setosa
# 4             5.0          3.6           1.4          0.2     setosa
# ..            ...          ...           ...          ...        ...
# 145           6.7          3.0           5.2          2.3  virginica
# 146           6.3          2.5           5.0          1.9  virginica
# 147           6.5          3.0           5.2          2.0  virginica
# 148           6.2          3.4           5.4          2.3  virginica
# 149           5.9          3.0           5.1          1.8  virginica
# [150 rows x 5 columns]

sns.pairplot(df, hue="species")

###
# Question:
# import seaborn as sns 
# --> ImportError: DLL load failed: 找不到指定的程序。

# Solution: 可能是 scipy 或是 numpy 的版本問題, 移除後重新安裝
# conda remove numpy
# conda install numpy
# conda install seaborn
# 加油!!!

##############################
# 09.MySQL常用語法
##############################

# MySQL 下載
# https://dev.mysql.com/downloads/
# 選取 [MySQL Installer for Windows]
# 選取 [MySQL Installer 8.0.23] --> Windows (x86, 32-bit), MSI Installer [mysql-installer-community-8.0.23.0.msi] 422.4MB
# mysql-installer-community-8.0.23.0.msi
# 安裝完成會啟動 (1).MySQL Shell (2).MySQL Workbench

# 開啟 MySQL Workbench, 練習以下 MySQL語法

-- 顯示版本，日期
SELECT VERSION(), CURRENT_DATE;

-- 現在時間
SELECT NOW();

-- 顯示資料庫
SHOW databases;

-- 使用內建範例資料庫
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

-- date 函數
SELECT date(rental_date) FROM rental;

##############################
# 10.Python連結MySQL
##############################

# example 1 - 資料庫連結
import mysql.connector

# https://dev.mysql.com/doc/sakila/en/
cnx = mysql.connector.connect(user='rwepa', 
                              password='123456',
                              host='127.0.0.1',
                              database='sakila')
cnx.close()

# example 2 - SELECT 範例
import mysql.connector

cnx = mysql.connector.connect(user='rwepa', password='123456', database='sakila')
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
# 11.Python物件導向
##############################

# 範例1
# 建立類別 class
class MyClass:
  x = 5

# 使用 ClassName() 實作實例
p1 = MyClass()
print(p1.x)

# 範例2
# __init__() 函數表示類別初使化時,該函數會自動執行, 左右為二個底線
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Alan", 20)

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
# end
