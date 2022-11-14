"""
title   : iPAS-python-program
author  : Ming-Chang Lee
email   : alan9956@gmail.com
RWEPA   : http://rwepa.blogspot.tw/
Date    : 2020.11.18

Updated : 2022.01.01 -更新 08.繪圖中文字型
Updated : 2021.01.28 -新增 09.MySQL常用語法
Updated : 2021.01.28 -新增 10.Python連結MySQL
Updated : 2021.02.17 -新增 11.Python物件導向
Updated : 2021.04.11 -新增 12.iPAS 科目二：資料處理與分析概論
Updated : 2021.08.09 -新增 13.決策樹繪圖4種方法
Updated : 2021.09.30 -新增 14.深度學習CNN - MNIST範例
Updated : 2022.01.16 -新增 15.Dash視覺化簡介
Updated : 2022.02.12 -新增 16.Folium地理視覺化應用
Updated : 2022.07.02 -新增 17.Orange3簡介
Updated : 2022.08.02 -新增 18.conda虛擬環境
Updated : 2022.09.21 -新增 19.ipynb轉換為pdf檔案
"""

# 經濟部 iPAS 巨量資料分析師認證-Python學習參考資料
# https://www.ipas.org.tw/bda/AbilityIndex.aspx

##############################
# 大綱
##############################

# 00.conda,pip操作
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
# 12.iPAS - 科目二：資料處理與分析概論
# 13.決策樹繪圖4種方法
# 14.深度學習CNN - MNIST範例
# 15.Dash視覺化簡介
# 16.Folium地理視覺化應用
# 17.Orange3簡介
# 18.conda虛擬環境
# 19.ipynb轉換為pdf檔案

# anaconda
# https://www.anaconda.com/

##############################
# 00.conda,pip操作
##############################

# conda 資訊
conda info

# 顯示已安裝套件
conda list
pip list

# 查詢模組資訊
pip show 模組名稱

# 安裝模組
conda install 模組名稱
pip install 模組名稱

# 更新模組
conda update 模組名稱
pip install -U 模組名稱

# 範例: 更新 anaconda 模組
conda update anaconda

# 範例: 更新 Spyder 模組
conda update spyder

# 移除模組
conda remove 模組名稱
pip uninstall 模組名稱

##############################
# 切換工作目錄
##############################
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

# Get all keys
c.keys()

# Get an element
u = c["uid"]

# Add an element
c["shell"] = "/bin/sh"

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

# reshape 應用1
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
a # a物件已經更改, array([0, 1, 168, 3, 4, 5])

c = a.reshape((3,2)).copy()
c
c[0][0] = -999
c
a # a物件沒有更改

# reshape 應用2
a = np.array([[1, 2, 3], [4, 5, 6]])
a

b= a.reshape((3, 2))
b

b[1, 0] = 999
b
a

c = b.reshape(-1, 3)
c

# reshape 應用3
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

# pandas 設定顯示所有欄位
pd.set_option('display.expand_frame_repr', False)

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

# 取出一個儲存格 cell, 使用 at 或 iat

# at 使用變數名稱
df2.at[0,'A']

# iat 使用指標 index
df2.iat[1,4]

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

# 08.繪圖中文字型
# example 8 Windows 中文字型解決方案
import os
os.getcwd()
os.chdir("C:/pythondata")

import matplotlib.pyplot as plt
import numpy as np

##############################
# Windows 中文字型
##############################

##############################
# 方法1
##############################

# (1).關閉Spyder

# (2).將微軟正黑體 C:\Windows\fonts\msjh.ttc 複製到以下目錄
# 【C:\Users\user\anaconda3\Lib\site-packages\matplotlib\mpl-data\fonts\ttf】

# (3).將現有 DejaVuSans.ttf 更名為 DejaVuSans-old.ttf

# (4).將 msjh.ttc 更名為 DejaVuSans.ttf

# (5).重新啟動Spyder即可使用中文字型

##############################
# 方法2 使用  matplotlib.font_manager.FontProperties 方法
##############################

from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\mingliu.ttc", size=12)

# 匯入資料
# https://github.com/rwepa/DataDemo/blob/master/web_traffic.csv
myData = np.genfromtxt("web_traffic.csv", delimiter = '\t')

print(myData[:6])
myData.ndim # 2個維度
myData.shape # same as print(myData.shape) 743*2

x = myData[:,0] # 743*1
y = myData[:,1] # 743*1

# 檢查是否有Na
np.sum(np.isnan(y)) # 有8個值是nan
print("Number of invalid entries:", np.sum(np.isnan(y)))

# 取出非Na
x = x[~np.isnan(y)] # 743-8=735
y = y[~np.isnan(y)]

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
# 方法3 使用 matplotlib.rcParams 方法
##############################

import matplotlib

# 設定 matplotlib.rcParams 方法
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 設定負號錯誤顯示
matplotlib.rcParams['axes.unicode_minus'] = False

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

##############################
# 12.iPAS - 科目二：資料處理與分析概論
##############################

##############################
# 1-1資料組織與清理
##############################

# Label encoding
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 匯入資料
# https://github.com/rwepa/DataDemo/blob/master/german_credit.csv
df = pd.read_csv("C:/rdata/german_credit.csv")
df
df['Purpose'].describe()

# Purpose 進行 label encoding
labelencoder = LabelEncoder()
df['PurposeEncoding'] = labelencoder.fit_transform(df['Purpose'])

df['Purpose'].head()
df['PurposeEncoding'].head()

# One-hot encoding

# 匯入模組
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
  
# 匯入資料
df = pd.read_csv("C:/rdata/german_credit.csv")

df['Purpose'].describe()

# one-hot encoding   
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), ['Purpose'])],
                                      remainder='passthrough')
  
df1 = np.array(columnTransformer.fit_transform(df), dtype = np.str)
df1

##############################
# 1-2.資料摘要與彙總
##############################

# 盒鬚圖 boxplot - matplotlib 套件

import pandas as pd
import matplotlib.pyplot as plt

# 參考R匯出 Cars93.csv
df = pd.read_csv('C:/rdata/Cars93.csv')

fig1, ax1 = plt.subplots()
ax1.set_title('Python - boxplot')
ax1.boxplot(df['Price'])
ax1.set_xlabel('Cars93 dataset')
ax1.set_ylabel('Price')

# 群組盒鬚圖 - matplotlib 套件
data = [df[df.Origin == 'USA']['Price'], 
        df[df.Origin == 'non-USA']['Price']]

fig2, ax2 = plt.subplots()
ax2.set_title('Python - boxplot with group')
ax2.boxplot(data)
ax2.set_xticklabels(['USA', 'non-USA'])
ax2.set_xlabel('Origin')
ax2.set_ylabel('Price')

# 盒鬚圖 boxplot - pandas 套件
df.boxplot(column =['Price'], grid = False)

# 群組盒鬚圖 - pandas 套件
df.boxplot(by ='Origin', column =['Price'], grid = False)

# 盒鬚圖 boxplot - seaborn 套件
import seaborn as sns

ax = sns.boxplot(x = df["Price"])

ax = sns.boxplot(y = df["Price"])

# 群組盒鬚圖 - seaborn 套件
ax = sns.boxplot(x = "Origin", y = "Price", data=df)

# pandas排序
import pandas as pd
import numpy as np

np.random.seed(168)
df = pd.DataFrame(np.random.randn(3,3), columns=list(['x1', 'x2', 'x3']))
df

# 遞增
df.sort_values(by='x1')

# 遞減
df.sort_values(by='x1', ascending = False)

# 群組
import pandas as pd
df = pd.read_csv('C:/rdata/Cars93.csv')

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

# 摘要
import pandas as pd
df = pd.read_csv('C:/rdata/Cars93.csv')
df.describe()

# 1-3.屬性轉換與萃取

# 奇異值分解 (Singular Value Decomposition, SVD)
# 參考 Jason Brownlee, Basics of Linear Algebra for Machine Learning: Discover the Mathematical Language of Data in Python, 2018.

from numpy import array
from scipy.linalg import svd

# 定義矩陣 A:3*2
A = array([[1, 2], [3, 4], [5, 6]])
print(A)

# SVD計算
U, s, V = svd(A)
print(U)
print(s)
print(V)

##############################
# 2-1.統計分析基礎
##############################

# Python - 平均數 𝜇 之區間估計
from scipy.stats import norm
import math
alpha = 0.05
sampleSD = 5
sampleSize = 16
sampleMean = 60
zscore = norm.ppf(alpha/2)*(-1)
zscore

lowerBounr = sampleMean - zscore*sampleSD/math.sqrt(sampleSize)
upperBound = sampleMean + zscore*sampleSD/math.sqrt(sampleSize)
print([lowerBounr, upperBound])

# Python - t檢定
from scipy import stats
x = stats.norm.rvs(5, size=20)
x

# 回傳二個數值, 統計量與p值
stats.ttest_1samp(x, 5) # p-value 很大
stats.ttest_1samp(x, 1) # p-value 很小

print('t-statistic = %7.5f, pvalue = %7.5f' % stats.ttest_1samp(x, 5))

'''
%%	在字串中顯示%
%s  字串顯示
%d	以10 進位整數方式輸出
%f	將浮點 數以10進位方式輸出
%e  科學記號, 用小寫e表示
%E  科學記號, 用大寫E表示
'''

# .4f 表示數小數點後以四捨五入方式顯示4位小數值
print('22/7 = %.4f' % (22/7)) 

# 卡方檢定
from scipy.stats import chisquare
chisquare([230,220,450])

##############################
# 2-2.探索式資料分析與非監督式學習
##############################

# 階層式集群熱繪圖 Hierarchically Clustered Heatmap
import statsmodels.api as sm
import seaborn as sns

df = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
g = sns.clustermap(df, z_score=1)

##############################
# 2-3.線性模型與監督式學習
##############################

# 啟動函數 (Activation function)

# Sigmoid 函數
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+(np.e**(-x)))

x = np.arange(-6, 6, 0.1)

plt.plot(x, sigmoid(x))
plt.title("Sigmoid function (0~1)")
plt.show()

# ReLU 函數
import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-6, 6, 0.1)

plt.plot(x, relu(x))
plt.title("ReLU function, f(x)=max(0,x)")
plt.show()

# Tanh 函數
import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return np.tanh(x)

x = np.arange(-6, 6, 0.1)

plt.plot(x, tanh(x))
plt.title("Tanh function (-1 ~ 1)")
plt.show()

# Softmax 函數
import numpy as np

def softmax(x):
    return np.exp(x)/sum(np.exp(x))

x = np.array([1,2,3,4,1,2,3])

y = softmax(x)
print(y)

# 多層感知器 (MLP) –  iris範例

# conda install -c conda-forge tensorflow
# conda install -c conda-forge keras

# 步驟1 載入套件
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

# 步驟2 資料預處理
np.random.seed(7)  # 指定亂數種子

# 載入資料集
# https://github.com/rwepa/DataDemo/blob/master/iris.csv
df = pd.read_csv("iris.csv")

# one-hot 編碼
target_mapping = {"setosa": 0,
                  "versicolor": 1,
                  "virginica": 2}

df["Species"] = df["Species"].map(target_mapping)

dataset = df.values # 取出資料框的值
np.random.shuffle(dataset)  # 使用亂數打亂資料的列順序

# 分割成特徵資料(X)和標籤資料(Y)
X = dataset[:,0:4].astype(float)
Y = to_categorical(dataset[:,4])

# 特徵標準化
X -= X.mean(axis=0)
X /= X.std(axis=0)

# 分割成訓練和測試資料集
X_train, Y_train = X[:120], Y[:120]     # 訓練資料前120筆
X_test, Y_test = X[120:], Y[120:]       # 測試資料後30筆

# 步驟3 定義模型
# 建立Keras的Sequential模型
# input(4)-->hiden1(6)-->hiden2(6)-->output(3)
# 輸入層 4個特徵
# 第1隱藏層 6個神經元
# 第2隱藏層 6個神經元
# 輸出層 3個神經元

model = Sequential() # 建立 Sequential 物件
model.add(Dense(6, input_shape=(4,), activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(3, activation="softmax"))
model.summary()   # 顯示模型摘要

# dense (Dense)   : 4*6 + 6 = 30
# dense_1 (Dense) : 6*6 + 6 = 42
# dense_2 (Dense) : 6*3 + 3 = 21
# 合計 = 30 + 42 + 21 = 93

# 步驟4 編譯模型

# 編譯模型
# loss 損失函數, optimizer 優化器即梯度下降法, metrics 評估標準
# https://www.tensorflow.org/api_docs/python/tf/keras/optimizers

model.compile(loss="categorical_crossentropy", 
              optimizer="adam",
              metrics=["accuracy"])

# 步驟5 訓練模型

# 訓練模型
# epochs 訓練週期,  batch_size 批次樣本大小

print("Training ...")
model.fit(X_train, Y_train, epochs=100, batch_size=5)

# 步驟6 評估與儲存模型

# 評估模型
print("\nTesting ...")
loss, accuracy = model.evaluate(X_test, Y_test)
print("準確度 = {:.2f}".format(accuracy))

# 儲存 Keras 模型
print("Saving Model: iris.h5 ...")
model.save("iris.h5")

# 使用儲存模型進行預測
from tensorflow import keras

model = Sequential()
model = keras.models.load_model("iris.h5")
model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))

Y_pred = model.predict_classes(X_test)
print(Y_pred)

Y_target = dataset[:,4][120:].astype(int)
print(Y_target)

##############################
# 13.決策樹繪圖4種方法
##############################

# 執行環境: windows 10 (64-bit) anaconda with spyder 4.2.5
# 參考資料 https://scikit-learn.org/stable/modules/tree.html#tree

from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
X, y = iris.data, iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

##############################
# 繪圖方法1
# 繪圖於 Spyder \ Plots 視窗
##############################

tree.plot_tree(clf)

##############################
# 繪圖方法2
# 繪圖於 IPython 視窗
##############################

# 步驟1 安裝 pydotplus
# Anaconda 環境
# conda install pydotplus

# 步驟2 繪製決策樹
import io
import pydotplus
dot_data = io.StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

# 步驟3 匯出決策樹圖檔
graph.write_png('titanic-RWEPA.png')

# 步驟4 匯入決策樹
from IPython.core.display import Image
Image(filename='titanic-RWEPA.png')

##############################
# 繪圖方法3 graphviz 套件
# 輸出為 PDF檔案
##############################

# conda install python-graphviz

import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data) 
graph.render("iris") # 輸出為 iris.pdf

##############################
# 繪圖方法4 graphviz 套件
# 繪圖於 IPython 視窗, 填上顏色
##############################

dot_data = tree.export_graphviz(clf, 
                                out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True,
                                rounded=True,
                                special_characters=True)

graph = graphviz.Source(dot_data)
graph

##############################
# 14.深度學習CNN - MNIST範例
##############################

# 安裝 conda install tensorflow (或是 pip install tensorflow)
# 安裝 conda install keras (或是 pip install keras)

# 載入模組
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.utils import to_categorical

# 設定亂數種子
seed = 168
np.random.seed(seed)

# 載入 MNIST 資料集
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# 將圖片轉換成 4D 張量
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype("float32")
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype("float32")

# 因為是固定範圍, 所以執行正規化, 從 0-255 至 0-1
X_train = X_train / 255
X_test = X_test / 255

# One-hot編碼
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)

# 定義模型
model = Sequential()
model.add(Conv2D(16, kernel_size=(5, 5), padding="same", input_shape=(28, 28, 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, kernel_size=(5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))
model.summary()   # 顯示模型摘要資訊

# 編譯模型
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 訓練模型(需要一些時間...)
history = model.fit(X_train, Y_train, validation_split=0.2, epochs=10, batch_size=128, verbose=2)

# 評估模型
print("\nTesting ...")
loss, accuracy = model.evaluate(X_train, Y_train)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))

# 儲存Keras模型
print("Saving Model: mnist.h5 ...")
model.save("mnist.h5")

# 顯示圖表來分析模型的訓練過程
import matplotlib.pyplot as plt

# 顯示訓練和驗證損失
loss = history.history["loss"]
epochs = range(1, len(loss)+1)
val_loss = history.history["val_loss"]
plt.plot(epochs, loss, "bo-", label="Training Loss")
plt.plot(epochs, val_loss, "ro--", label="Validation Loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

# 顯示訓練和驗證準確度
# acc = history.history["acc"]
acc = history.history['accuracy']
epochs = range(1, len(acc)+1)
# val_acc = history.history["val_acc"]
val_acc = history.history["val_accuracy"]
plt.plot(epochs, acc, "bo-", label="Training Acc")
plt.plot(epochs, val_acc, "ro--", label="Validation Acc")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# 參考資料: 陳允傑, TensorFlow 與 Keras - Python 深度學習應用實務, 旗標.

##############################
# 15.Dash視覺化簡介
##############################
# 參考資料: https://dash.plotly.com/

# Dash 組成二大元件: layout, callback

# 執行 dash 三大方法
# (1).命令提示列 python app.py
# (2).Spyder 逐行執行
# (3).Jupyter notebook 逐行執行

# Part 1.安裝 plotly, dash等套件. 使用 Jupyter notebook時,須安裝 jupyter-dash 模組.
# conda install -c conda-forge plotly
# conda install -c conda-forge dash
# conda install -c conda-forge jupyter-dash
# conda install -c conda-forge dash-html-components
# conda install -c conda-forge dash-core-components
# conda install -c conda-forge dash-bootstrap-components

"""
# import dash_html_components as html (不再使用)
# import dash_core_components as dcc (不再使用)
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

# Spyder : http://127.0.0.1:8050/
# Jupyter : http://127.0.0.1:8051/
"""

# 範例1 plotly 長條圖
import plotly.graph_objects as go
import plotly.io as pio
#pio.renderers.default = 'svg'
pio.renderers.default = 'browser'

product = ['Product A', 'Product B', 'Product C']
sale = [20, 14, 23]
fig = go.Figure(data=[go.Bar(x=product, y=sale, text=sale, textposition='auto')])
fig.show()

# Part 2.Dash Layout

# 範例2 dash 長條圖

# 載入套件
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# 建立 app
app = dash.Dash(__name__)

# 使用字典物件建立資料框資料集 6列*3行
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["Taipei", "Taipei", "Taipei", "Taichung", "Taichung", "Taichung"]
})

# 使用 plotly.express 建立長條圖
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# 建立 dash layout
# children 是第一個屬性, 一般此屬性可以省略.
# html.H1(children='Hello Dash') 與 html.H1('Hello Dash') 相同.
# children 可以是字串, 數字, list.
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data (網頁應用框架)
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server(debug=True, use_reloader=False)
# 使用瀏覽器開啟 http://127.0.0.1:8050/
# 如果設定本例中的 debug=True, 則當程式碼更新時, 瀏覽器會自動更新,執行"hot-reloading"功能.

# 範例3 左右並排長條圖
import dash_html_components as html
import dash_core_components as dcc
import dash
import dash_core_components
print(dash_core_components.__version__)

# 加入 CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div('Dash: A web application framework for Python. 2022.1.16'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': '男'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': '女'},
            ],
            'layout': {
                'title': 'Dash 資料視覺化'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)

# 範例4 下拉式選單長條圖
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("2022.01.16-選取顏色 Color:"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['Gold', 'MediumTurquoise', 'LightGreen']
        ],
        value='Gold',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], marker_color=color))
    return fig

app.run_server(debug=False)

##############################
# 16.Folium地理視覺化應用
##############################

# folium官網 https://python-visualization.github.io/folium/

# folium 特性:
# Folium 是 Python 地理視覺化模組
# Folium 提供互動式的操作介面
# Folium 採用 leaflet JavaScript 函式庫, 操作與R類似
# Folium 地圖服務結合 OpenStreetMap, Mapbox, and Stamen 等客製化功能

# 安裝 folium
# conda install -c conda-forge folium 

# 使用 Spyder 可以配合 webbrwoser 開啟瀏覽器, Anaconda 已安裝 webbrwoser 模組
# Jupyter-notebook 不用使用 webbrwoser 模組, 可以直接顯示.

# webbrowser 可以直接開啟網頁
webbrowser.open_new_tab('http://rwepa.blogspot.com/')

##############################
# folium - 範例1 台北101大樓地圖
##############################

import folium

import webbrowser

# [緯度 lat, 經度 long]
# 街道圖, 此為預設值 tiles='OpenStreetMap' 
m = folium.Map(location=[25.033493, 121.564101], zoom_start=18)

m.save("mymap.html")

webbrowser.open_new_tab("mymap.html")

# stamenterrain 地形圖
m = folium.Map(location=[25.033493, 121.564101], tiles='stamenterrain', zoom_start=13)
m.save("mymap.html")
webbrowser.open_new_tab("mymap.html")

# tiles='stamentoner' 黑白線條圖
m = folium.Map(location=[25.033493, 121.564101], tiles='stamentoner', zoom_start=13)
m.save("mymap.html")
webbrowser.open_new_tab("mymap.html")

# tiles='stamenwatercolor' 水波圖
m = folium.Map(location=[25.033493, 121.564101], tiles='stamenwatercolor', zoom_start=13)
m.save("mymap.html")
webbrowser.open_new_tab("mymap.html")

# tiles='cartodbpositron'  
m = folium.Map(location=[25.033493, 121.564101], tiles='cartodbpositron', zoom_start=13)
m.save("mymap.html")
webbrowser.open_new_tab("mymap.html")

##############################
# folium - 範例2 動態放置標記(marker)
##############################
m = folium.Map(location=[23.97555, 120.97361], tiles="Stamen Terrain", zoom_start=8)

tooltip = "Click me!"

folium.Marker(
    location=[23.97555, 120.97361], 
    popup="<i>臺灣地理中心碑</i>", 
    tooltip=tooltip,
    icon=folium.Icon(icon="cloud"),
).add_to(m)

folium.Marker(
    location=[25.033493, 121.564101], 
    popup="<b>台北101大樓</b>", 
    tooltip=tooltip,
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(m)

# Jupyter-notebook 輸入 m 即可顯示地圖
m.save("mymap.html")

webbrowser.open_new_tab("mymap.html")

##############################
# folium - 範例3 加入圓形標記
##############################

m = folium.Map(location=[25.042276, 121.533394], zoom_start=14)

folium.Circle(
    radius=200,
    location=[25.033493, 121.564101],
    popup="台北101大樓",
    color="crimson",
    fill=False,
).add_to(m)

folium.CircleMarker(
    radius=100,
    location=[25.04777, 121.51722],    
    popup="台北車站",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

m.save("mymap.html")

webbrowser.open_new_tab("mymap.html")

##############################
# folium - 範例4 滑鼠點選加入標記
##############################

m = folium.Map(location=[25.033493, 121.564101], zoom_start=14)

folium.Marker([25.04777, 121.51722], popup="台北車站").add_to(m)

m.add_child(folium.ClickForMarker(popup="Waypoint"))

m.save("mymap.html")

webbrowser.open_new_tab("mymap.html")
##############################
# folium - 範例5 新北市公共自行車租賃系統(YouBike)應用
##############################

# 新北市公共自行車租賃系統(YouBike)
# https://data.gov.tw/dataset/123026

import folium
import webbrowser
import pandas as pd

df = pd.read_csv('C:/Users/user/Downloads/新北市公共自行車租賃系統(YouBike).csv') # 664*14
df
df.columns
# ['sno', 'sna', 'tot', 'sbi', 'sarea', 'mday', 'lat', 'lng', 'ar', 'sareaen', 'snaen', 'aren', 'bemp', 'act']
# sno(站點代號)、sna(中文場站名稱)、tot(場站總停車格)、sbi(可借車位數)、sarea(中文場站區域)
# mday(資料更新時間)、lat(緯度)、lng(經度)、ar(中文地址)、sareaen(英文場站區域)
# snaen(英文場站名稱)、aren(英文地址)、bemp(可還空位數)、act(場站是否暫停營運)

# 缺車: 可借車比例較小者,可借車比例=可借車位數 /場站總停車格 = sbi/tot
# 缺車比例 = 1- (sbi/tot)
# 缺車熱點: 可借車比例 < 自訂 或 可借車位數 < 自訂個數

df['lackcar'] = 1 - df['sbi']/df['tot']
df['lackcar'].describe()
# count    664.000000
# mean       0.366837
# std        0.216291
# min        0.000000
# 25%        0.198611
# 50%        0.367544
# 75%        0.533333
# max        0.937500

# 取出缺車比例較大的前10筆資料
df_lackcar = df.sort_values(by=['lackcar'], ascending=False)[0:10]

m = folium.Map(location=[25.012839, 121.456308], tiles='cartodbpositron', zoom_start=13)

for index, row in df.iterrows():
    # 將資料點加到地圖上
    folium.Circle(
        radius=100,
        location=[row["lat"], row["lng"]],
        popup="{} \n {}".format(row["sna"], row["tot"]),
        color="#555",
        weight=1,
        fill_color="#FFE082",
        fill_opacity=1,

    ).add_to(m)
    
    # 加入缺車標記
    if row["lackcar"] == 1:
        folium.Marker(
            location=[row["lat"], row["lng"]],
            tooltip=row['sna'],
            icon=folium.Icon(color='lightred', icon='fa-regular fa-bicycle', prefix='fa')
    ).add_to(m)
# icon list: https://fontawesome.com/icons

# 加入標題
loc = '新北市Youbike系統-2022.2.11-@RWPEA'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)   

m.get_root().html.add_child(folium.Element(title_html))

m.save("mymap.html")

webbrowser.open_new_tab("mymap.html")

# 17.Orange3簡介

# (1).Orange 3 特性
# 1.University of Ljubljana, Slovenia, 10 October 1996
# 2.視覺化程式設計工具(Visual Programming Tools)
# 3.執行更加快速(C++)與視覺化操作
# 4.提供多種機器學習模組
# 5.開放原始碼與跨平台
# 6.適用於Python模組
# 7.資料預處理
# 8.模型訓練
# 9.部署

# (2).參考資源
# 官網     : https://orangedatamining.com/
# 元件     : https://orangedatamining.com/widget-catalog/
# Tutorial : https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/  

# (3).Orange 3 安裝

# 方法1 使用 Anaconda
# 選取 程式集 \ Anaconda3 \ Anaconda Navigator (anaconda3)
# 選取 Orange 3 並按下 [Install] 下載並安裝
# 安裝完成後按下 [Launch] 啟動 Orange3
# 或是在命令提示字元輸入以下字元: python -m Orange.canvas
# 注意:本安裝方法須一些時間

# 方法2 下載 windows 免安裝檔. 解壓縮後,即可使用, 不用進行安裝程序.
# https://orangedatamining.com/download/#windows 
# Orange3-3.32.0.zip (550MB)
# 下載並解壓縮zip
# 開啟 Orange 執行檔

# 方法3 使用 orange3 虛擬環境
cd C:\Users\user\anaconda3\envs\orange3
python -m Orange.canvas

# (4).Orange3 add-ons (外掛元件)
# 1.Orange3-Associate          關聯規則
# 2.Orange3-Bioinformatics     生物資訊
# 3.Orange3-Educational        機器學習教育示範
# 4.Orange3-Explain            重要特徵解釋
# 5.Orange3-Geo                地理資料視覺化
# 6.Orange3-ImageAnalytics     影像分析
# 7.Orange3-Network            網路分析
# 8.Orange3-Prototypes         原型
# 9.Orange3-SingleCell         單細胞分析
# 10.Orange-Spectroscopy       光譜分析
# 11.Orange3-Text              文字探勘
# 12.Orange3-Textable          文字探勘, 編碼
# 13.Orange3-Timeseries        時間序列
# 14.Orange3-Survival-Analysis 存活分析
# 15.Orange3-WorldHappiness    世界社會經濟指標 (GDP...)

# (5).安裝 Add-ons Associate
# Options \ Add-ons
# Associate 打勾 進行安裝
# 按 OK 重新啟動 Orange

# (6).Associate 二大元件:
# Frequent Itemsets 頻繁項目集 
# Association Rules 關聯規則
# 輸入Associate的資料須為 0-1 encoding或是類別型資料(yes/no)
# milk egg sugar 
# 1    0    1
# 0    1    1
# 0    0    0

##############################
# 18.conda虛擬環境
##############################

"""
# 檢視所有虛擬環境清單
conda env list

# 啟用 myenv 虛擬環境
conda activate myenv

# 關閉虛擬環境
conda deactivate

# 建立 myenv 虛擬環境
# --name 也可以使用 -n
# --file 也可以使用 -f
conda create --name myenv

# 建立特定 python 版本的虛擬環境
conda create -n myenv python=3.9

# 建立特定 scipy 模組版本的虛擬環境
conda create -n myenv scipy=1.9.0

# 建立特定 python 版本與特定 scipy 模組版本的虛擬環境
conda create -n myenv python=3.9 scipy=1.9.0 astroid babel

# 檢視 myenv 虛擬環境的模組資訊
conda list -n myenv scipy

# 安裝 myenv 虛擬環境的 spyder 模組
conda install -n myenv spyder

# 安裝 myenv 虛擬環境的 rdkit 模組
# rdkit: Open source toolkit for cheminformatics
# https://www.rdkit.org/docs/GettingStartedInPython.html
conda install -c conda-forge -n myenv rdkit

####################
# 複製(clone)虛擬環境
####################

# 方法1.使用conda指令複製(clone)虛擬環境的三大步驟.
# 此方法將新增程式集 Jupyter Notebook (newenv1), Reset Spyder Settings (newenv1), Spyder (newenv1)

# 步驟1.顯示環境清單
conda env list

# 步驟2.如果有登入, 先執行登出環境
conda deactivate

# 步驟3.複製環境
# conda create --name new_env --clone original_env
# new_env      : 新的環境, 本例使用 newenv1
# original_env : 原始被複製的環境, 本例使用 base
conda create --name newenv1 --clone base

# 方法2.使用YML複製(clone)新環境的二大步驟.
# 此方法將新增程式集 Anaconda Navigator (opencv), Anaconda Prompt (opencv), Anaconda Powershell Prompt (opencv)

# 步驟1.匯出原始環境YML組態檔
conda activate base
conda env export > environment.yml
conda deactivate

# 步驟2.修改 environment.yml
# 將 environment.yml 第1行name: 更名為新環境名稱, 本例將 base 更改為 opencv

# 步驟3.使用YML並建立新環境
conda env create -f environment.yml

# 步驟4.登入opencv環境
conda activate opencv

# 步驟5.安裝opencv模組
pip install opencv-python
pip install opencv-contrib-python

# 同理, 亦可以新建 orange3 環境並安裝 orange3 模組
pip install orange3

# 登入 orange3 環境
conda activate orange3

# 啟動 Orange3
orange-canvas

reference: https://docs.conda.io/projects/conda/en/4.6.0/user-guide/tasks/manage-environments.html#managing-environments
"""

##############################
# 19.ipynb轉換為pdf檔案
##############################

# 使用 Jupyter-notebook, 如果須將檔案轉換為 PDF, 即 File \ Download as \ PDF via HTML (.html)
# 顯示以下錯誤
# nbconvert failed: Pyppeteer is not installed to support Web PDF conversion. Please install `nbconvert[webpdf]` to enable

# 執行以下3個指令後, 即可轉換為PDF檔案
pip install nbconvert
pip install pyppeteer
pyppeteer-install
# end
