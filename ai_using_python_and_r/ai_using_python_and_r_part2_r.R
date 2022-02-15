# File     : ai_using_python_and_r_part2_r.R
# Author   : Ming-Chang Lee (2022)
# Email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

# 大綱 -----
# 06.R與RStudio簡介,資料匯入與匯出
# 07.R資料物件,判斷式與函數,群組分析與繪圖graphics
# 08.資料操作dplyr,視覺化ggplot2,互動式表格視覺化
# 09.地理資料視覺化leaflet,機器學習與深度學習應用
# 10.基礎互動式shiny,進階互動式shiny Server 佈署

# R 入門資料分析與視覺化應用(7小時28分鐘)
# https://mastertalks.tw/products/r?ref=MCLEE

# R 商業預測應用(8小時53分鐘)
# https://mastertalks.tw/products/r-2?ref=MCLEE

# 06.R與RStudio簡介,資料匯入與匯出 -----

# R 安裝與簡介 -----

# 認識R-統計分析,繪圖與資料視覺化

# http://www.r-project.org/

# 安裝參考說明, 2006
# https://github.com/rwepa/DataDemo/blob/master/windows_intall_R.pdf

# 下載並安裝 Rtools

# 實作練習16 -----
# R 執行畫面
plot(runif(100), type="l", main= "R大數據分析")
demo(graphics)
demo(persp)

# 實作練習17 -----
# 新增R檔案練習
# 使用R原生環境,輸入以下程式碼, 另儲存成 myfirst.R
plot(runif(10), type="b", main= "R大數據分析")
x <- rnorm(10)
x
pairs(iris[-5], pch=16, col=iris$Species, main="RWEPA-iris資料集散佈圖矩陣")

# R for Mac -----
# https://youtu.be/72MYRBNo5Bk

# R for Ubuntu -----
# http://rwepa.blogspot.tw/2013/05/ubuntu-r.html

# RStudio 安裝與簡介 -----
# http://www.rstudio.com/

# R Markdown -----
# https://www.rstudio.com/resources/cheatsheets/

# Google’s R Style Guide -----
# https://google.github.io/styleguide/Rguide.html

# 套件 package -----

# e1071 package
install.packages("e1071")

library(e1071)

example(svm, package="e1071")

# 已載入的套件
search()

# R套件-41類別
# https://cran.csie.ntu.edu.tw/web/packages/index.html

# https://cloud.r-project.org/web/packages/index.html 

# 41類別-說明
# http://rwepa.blogspot.tw/2013/10/packages-list-32.html

# R對話資訊 -----
sessionInfo()

# 套件安裝目錄 -----

# 預設套件安裝目錄
.Library

# 套件安裝目錄
.libPaths()

# 已安裝套件
x <- installed.packages()
class(x)  # "matrix" "array"
dim(x)    # 626*16
mypackage = x[, 1] # matrix[列, 行]
mypackage[1:5]

library() # same as installed.packages()

# 輔助說明 help -----
help.start()

?plot

help(plot)

help.search("regression")

??regression

# 數學運算 -----

# R即是計算機
# log, exp

# e，作為數學常數，是自然對數函數的底數，亦稱自然常數、自然底數，或是尤拉數（Euler's number），以瑞士數學家尤拉命名。它是一個無限不循環小數
exp(1) # 2.718282
log(exp(1))
log(exp(2))
log10(1000)

# 算數操作 (arithmetic operator)

# +, -, *, /, ^, %%, %/%, %*%
2^3 # 次方
7 %% 2 # 餘數
7 %/% 2 # 商數

# 關係比較操作 (relation/comparison operator) 
# ==, !=, <, <=, >, >=

# 邏輯操作(logical operator)
# ! NOT
# & AND
# | OR

# 特殊數值 -----
x <- 5/0

x # Inf

exp(x)

exp(-x)

x - x

0/0 # NaN

# NA
x.NA <- c(1, 2, 3)

x.NA

length(x.NA) <- 4

x.NA

pi

letters

LETTERS

month.abb

month.name

# 資料型別 -----
# 整數
# 數值
# 字串: 須使用 ‘台北市‘ 或 “台北市“ 符號
# 邏輯值: 包括 TRUE, FALSE

# 資料匯入與匯出 -----

# read.table  輸入文字檔
# read.csv    輸入CSV檔
# write.table 輸出文字檔
# write.csv   輸出CSV檔

# 步驟 1. 設定工作目錄
# 步驟 2. 建立資料檔
# 步驟 3. 匯入資料  read.table
# 步驟 4. 資料處理
# 步驟 5. 匯出資料

#********************
# 步驟 1. 設定工作目錄
#********************

# 預設工作目錄
getwd() # get working directory
workpath <- "C:/rdata"
setwd(workpath)

# 已更改為 C:\rdata 工作目錄
getwd()

#********************
# 步驟 2. 準備資料檔 – 範例
#********************

# 日空氣品質指標(AQI)
# https://data.gov.tw/dataset/40507

#********************
# 步驟 3. 匯入資料  read.table
#********************

# ?read.table
# header: 標題名稱, sep: 區隔符號

myfile <- "aqx_p_434_20210725123120.csv"

aq <- read.table(myfile, header=TRUE, sep=",") # error!

aq <- read.table(myfile, header=TRUE, sep=",", fill=TRUE) # 亂碼!
head(aq, n=3) # 檢視前6筆, 標題,第2行有亂碼

aq <- read.table(myfile, header=TRUE, sep=",", fill=TRUE, encoding="UTF-8")
head(aq, n=3) # 第1個欄位名稱異常!

# 將檔案另儲存為 ANSI 編碼格式
myfileNew <- "aqx_p_434_20210725123120-ansi.csv"

aq <- read.table(myfileNew, header=TRUE, sep=",",) # OK

head(aq) # 第1個欄位名稱正常!

# 資料檢視
head(aq, n=5)

names(aq) # 欄位名稱

#********************
# 步驟 4. 資料處理
#********************

# 日期: 字串(chr)修正為日期(Date)
str(aq)

aq$MonitorDate <- as.Date(aq$MonitorDate)

str(aq)

head(aq)
dim(aq) # 1000列9行

AQI # 錯誤: 找不到物件 'AQI'
aq$AQI
attach(aq)
AQI
detach(aq)

# 篩選資資料
aq.Banqiao<- aq[aq$SiteName == "板橋", ]
aq.Banqiao <- aq.Banqiao[order(aq.Banqiao$MonitorDate), ]

aq.Xizhi <- aq[aq$SiteName == "汐止", ]
aq.Xizhi <- aq.Xizhi[order(aq.Xizhi$MonitorDate), ]

# 繪製直線圖
plot(aq.Banqiao$AQI, type="b")
lines(aq.Xizhi$AQI, col="red")
points(aq.Xizhi$AQI, col="red")

ymin <- min(aq.Banqiao$AQI, aq.Xizhi$AQI) - 1
ymax <- max(aq.Banqiao$AQI, aq.Xizhi$AQI) + 3

plot(aq.Banqiao$AQI, type="b", ylim=c(ymin, ymax), main="2018年8月AQI-板橋vs.汐止")
lines(aq.Xizhi$AQI, col="red")
points(aq.Xizhi$AQI, col="red")
legend("topleft", legend=c("板橋", "汐止"), col=c(1,2), lty=1)

#********************
# 步驟 5. 匯出資料
#********************

aq.Banqiao.Xizhi <- rbind(aq.Banqiao, aq.Xizhi)

write.table(aq.Banqiao.Xizhi, 
            "aq.Banqiao.Xizhi.csv", 
            sep=",", 
            row.names=FALSE)

# RData 資料物件儲存/匯入 -----
# save(資料物件1, 資料物件2, file=“myData.RData”)
# load(“myData.RData”)

# 實作練習18 -----
# 練習儲存 aq.Banqiao.Xizhi 為 aq.Banqiao.Xizhi.RData
# 練習載入 aq.Banqiao.Xizhi.RData

# 讀取 SAS 檔案 -----
# https://cran.r-project.org/web/packages/sas7bdat/index.html

library(sas7bdat)

# h_nhi_ipdte103.sas7bdat 103年模擬全民健保處方及治療明細檔_西醫住院檔
# 下載 https://github.com/rwepa/DataDemo/blob/master/h_nhi_ipdte103.sas7bdat

dd2014 <- read.sas7bdat("h_nhi_ipdte103.sas7bdat") # 14297*80, 7.25MB

system.time(dd2014 <- read.sas7bdat("h_nhi_ipdte103.sas7bdat")) # 23.09秒

head(dd2014)

# 匯入 SPSS -----

# foreign 套件
# https://cran.r-project.org/web/packages/foreign/index.html

# foreign 套件可讀取以下檔案格式:
# Minitab, S, SAS, SPSS, Stata, Systat, Weka, dBase

library(foreign)

# 下載 https://github.com/rwepa/DataDemo/blob/master/school.sav

db <- read.spss("school.sav", to.data.frame = TRUE)
head(db)
str(db)

# RMySQL套件編譯與建立 -----
# http://rwepa.blogspot.tw/2013/01/windows-rmysql.html

# RODBC 與 SQL Server 資料匯入與寫入 -----
# http://rwepa.blogspot.tw/2013/08/rodbc-sql-server.html

# 07.R資料物件,判斷式與函數,群組分析與繪圖graphics -----

# 資料物件 -----
# 向量   vector
# 矩陣   matrix
# 陣列   array
# 資料框 data.frame
# 串列   list

# 建立向量函數 c (concatenate) -----
x <- c(1, 3, 5, 7, 9)
x

# 因子 factor - levels, labels -----
f1 <- factor(1:3)
f2 <- factor(1:3, levels=1:5)

f1
f2

f2[4] <- 5
f2[5] <- 10
f2

# factor 範例1 -----
eye.colors <- factor(c("brown", "blue", "blue", "green", "brown", "brown", "brown"))
eye.colors
levels(eye.colors)

# factor 範例2 ------
gender <- factor(c("男", "女", "男", "男", "女"))

gender

levels(gender)

str(gender)

# 有序因子 (ordered factor) -----

ClothSize <- ordered(c("L", "H", "L", "M", "H"), 
                     levels = c("L", "M", "H"))

ClothSize

levels(ClothSize)

str(ClothSize)

# 因子轉換 -----
# as.factor 		    轉換為因子
# as.numeric()     	轉換為數值
# as.character()   	轉換為字串

# cut 函數示範
?cut

# 向量 vector -----

# 整數
v0 <- c(1:10)
v0
class(v0)
typeof(v0)

# 實數
v1 <- c(.29, .30, .15, .89, .12)
v1
class(v1)
typeof(v1)

v1[1]
v1[2:4]
v1[1,3,5] # error
v1[c(1,3,5)]

# 字元
x2 <- c("Taiwan", "China", "USA")
x2
is.vector(x2)

# Expand the length of a vector
length(x2) <- 5
x2

# 數值+字元
# 強制(coercion)轉換成單一相同型態
v2 <- c(.29, .30, .15, .89, .12, "wepa")
v2
class(v2)
typeof(v2)
mean(v2)

# 如何取得數值資料之平均值
as.numeric(v2)
mean(as.numeric(v2))
mean(as.numeric(v2), na.rm=TRUE)

# 向量具有 mode, length 屬性 
x1 <- vector(mode="numeric", length=1000000)

# 檢視前6筆資料
head(x1)

# 是否為向量
is.vector(x1)

taiwan1 <- c("正月初一", "正月初二", "正月初四", "正月初五", "正月初九", "正月十五")
names(taiwan1) <- c("春節", "回娘家", "接神日", "迎財神", "天公生", "元宵節")
taiwan1

# 矩陣 matrix

# 預設採用直行填入資料
x <- matrix(c(1:4), ncol = 2)
x
# [,1] [,2]
# [1,]    1    3
# [2,]    2    4

# 使用 byrow = TRUE 改為橫列填入
x <- matrix(c(1:4), ncol = 2, byrow = TRUE)
x
# [,1] [,2]
# [1,]    1    2
# [2,]    3    4
t(x)
diag(x)

# 矩陣運算
y <- matrix(c(4:1), ncol = 2)
y

x %*% y

?solve # 解a*x=b

# 資料框 data.frame -----

?cars
help(cars)

data(cars) # 好像不輸入data(cars),亦可以直接輸入cars???

cars

class(cars) # data.frame

head(cars)

head(cars, n=3)

cars[2]

cars["dist"]

cars[,2]

# 認識 iris, 150*5 -----
iris

head(iris)

tail(iris)

# 資料結構 str
str(iris)

# 資料摘要 summary
summary(iris)

# 實作練習19 -----

# 資料框的操作
# 練習1.iris {datasets} 操作
# 找出 Sepal.Length變數大於中位數的資料集

# 練習2.Cars93 {MASS}操作,資料篩選
data(Cars93, package = "MASS")
Cars93
str(Cars93)
summary(Cars93)
# 練習列,行,條件式資料篩選

# 練習3.計算 Luggage.room 的平均值為何?
# 將 Luggage.room 的遺漏值以平均值填補
mean(Cars93$Luggage.room) # NA ???

# 日期與時間資料 -----
mydates <- as.Date(c("2013-01-01", "2016-04-07"))

mydates

class(mydates)

# 日期相差
day <- mydates[2] - mydates[1]

day

# 日期/時間格式 -----
today <- Sys.Date()

today

format(today, format = "%B %d %Y")

# 日期與字串轉換 -----
# as.Date
# as.character

mydatetime <- strptime("2016-04-15 08-01-09", 
                       format="%Y-%m-%d %H-%M-%S")

mydatetime

class(mydatetime)
# "POSIXlt" "POSIXt" 
# POSIXt 包括二大類物件: POSIXct, POSIXlt

# ?strftime
# ?as.Date

# 時間序列 ts -----

# ts預設為年
x <- ts(c(123,39,78,52,110), start = 2015)
x

# ts季
data.ts <- ts(c(2,5,4,6,3,7,9:8),start=c(2009,2),frequency=4)

data.ts

is.ts(data.ts)

start(data.ts)

end(data.ts)

frequency(data.ts)

deltat(data.ts) # 0.25(=1/4)

plot(data.ts, type="b")

# ARIMA (AutoRegressive Integrated Moving Average)model -----
fit <- arima(AirPassengers, order=c(1,0,0), list(order=c(2,1,0), period=12))
fore <- predict(fit, n.ahead=24)
# error bounds at 95% confidence level
U <- fore$pred + 2*fore$se
L <- fore$pred - 2*fore$se
ts.plot(AirPassengers, fore$pred, U, L, col=c(1,2,4,4), lty = c(1,1,2,2), ylab="Passengers(1000)")
legend("topleft", col=c(1,2,4), lty=c(1,1,2), c("Actual", "Forecast", "Error Bounds (95% Confidence)"))

# zoo 套件 – 日期/時間物件 -----

# 支援 Regular / Irregular time series data
# S3物件:包括 index and date/time

# xts 套件 -----
# https://cran.r-project.org/web/packages/xts/index.html

# tidyquant 財金套件 -----
library(tidyquant) # tq_get

library(tidyverse) # 自動載入ggplot2

TWII <- tq_get("^TWII", get = "stock.prices", from = "2000-01-01")

# 台灣加權股價指數收盤價視覺化 -----
TWII %>%
  ggplot(aes(x = date, y = close)) +
  geom_line(size = 1) +
  labs(title = "2000年~2021年台灣加權股價指數收盤價",
       x = "日期", y = "收盤價")

# 判斷式 -----

# if 流程控制

?if # ERROR, 出現+

# unexpected token '?', expected 'LPAREN', LPAREN: Left PARENthesis 左括號

?"if" # OK

?`if` # OK

# if 用法1 -----

# if (條件式) {
#   表示式
# }

# if 範例1 -----
x <- 6

if (x > 0) {
  print("正數")
}

# if 用法2 -----

# if (條件式) {
#   表示式1 
# } else {
#   表示式2
# }

# 範例 if ... else 用法
x <- -1

if (x >= 0) {
  print("非負數")
} else {
  print("負數")
}

# if 範例2
# refer to materials
# 練習輸入

# ifelse 用法 -----
x <- c(1, 3, NA, 5, NA)
ifelse(is.na(x), 999, x)

# switch 函數 -----
centre <- function(x, type) {
  switch(type,
         mean = mean(x),
         median = median(x),
         trimmed = mean(x, trim = 0.1))
}

(x <- rt(n=10, df=1)) # 隨機抽樣10個樣本,其自由度為1的t分配
centre(x, "mean")
centre(x, "median")
centre(x, "trimmed") # 結果與沒有 trimmed 有明顯差異

# for迴圈 -----
(mydata <- c("R", "ggplot2", "shiny", "zoo", "leaflet"))

for (i in mydata) {
  print(nchar(i))
}

# while迴圈 -----
i <- 1
while (i <= length(mydata)) {
  print(paste0("字串 ", mydata[i], " 的長度為: ", nchar(mydata[i])))
  i <- i + 1
}

# 函數-範例 -----
# refer to materials

# 實作練習20 -----
# 自訂函數:輸入iris 資料集計算每列第2大數值的向量結果
# 使用 function 自訂函數

# 資料轉換 -----
# 判斷 is
# 轉換 as

# 數學轉換 -----
x <- 100
log(x)

log10(x)

log2(x)

log(x, base = 5)

1/x

x^0.5

1/x^0.5

# 標準化 scale -----
x <- matrix(1:30, ncol = 3)
scale(x) # mean=0, sd=1

# 標準化－最小值/最大值法 -----

# R 練習-將 Cars93$Price 標準化至1~5之間
x <- Cars93[1:10,]
x$Price

(max.old <- max(x$Price))
(min.old <- min(x$Price))

price.new <- ((x$Price - min.old)/(max.old - min.old))*(5 - 1) + 1
price.new

# 使用R內建函數 -----
x <- c(6, 9, 2, 1, 9)

min(x)

which.min(x)

max(x)

which.max(x)

sort(x)

order(x)

which(x > 5)

c(1, 2, 3) %in% x # 小範圍 %in% 大範圍

x %in% c(1, 2, 3)

# 向量化運算思維 -----

# vectorized operation -----

x <- c(1:10)
(x.square <- x^2)

x <- runif(23000000)
system.time(x2 <- x^2)

# apply與lapply應用 -----

# apply 家族 –列,行的統計值
m <- matrix(c(1:8), ncol=2)

m

apply(m, 1, function(x) mean(x))

as.matrix(apply(m, 1, function(x) mean(x)))

apply(m, 2, function(x) mean(x))

# which, any, all 函數 -----
(x <- matrix(rnorm(10)*10, ncol=2))

x > 5

# !(x>5)

which(x>5) # return index

which(x>5, arr.ind=TRUE) # return (row,column)

any(x>5)

all(x>5)

# 群組分析 -----

# iris鳶尾花資料集 -----

iris

head(iris)

tail(iris)

str(iris)

summary(iris)

apply(iris[-5], 1, mean)

apply(iris[-5], 2, mean)

lapply(iris[-5], mean)

# 資料處理 -----
?rbind
?cbind

# 彙總計算 table, aggregate -----
# table     --> 次數統計表
# aggregate --> 類似 Excel 樞紐分析

data(Cars93, package = "MASS")

head(Cars93)

str(Cars93)

summary(Cars93) # 有NA值

table(Cars93$Type)

aggregate(Price ~ Type, data = Cars93, FUN = mean)

aggregate(Price ~ Type + Origin, data = Cars93, FUN = mean)

aggregate(Luggage.room ~ Type, data = Cars93, FUN = mean) # 預設NA為na.omit

# R - 資料框排序
df <- head(iris, n = 5)

# 遞增排序
df[order(df$Sepal.Length),]

# 遞減排序
df[order(df$Sepal.Length, decreasing = TRUE),]

# 群組個數 table
table(Cars93$AirBags)

# 群組個數 table-2個維度
table(Cars93$AirBags, Cars93$Origin)

# 群組邊界計算 addmargins-預設值為總和
addmargins(table(Cars93$AirBags, Cars93$Origin))

# 群組邊界計算 addmargins-mean
addmargins(table(Cars93$AirBags, Cars93$Origin), FUN = mean)

# 群組百分比計算 prop.table
prop.table(table(Cars93$AirBags, Cars93$Origin))

# table 多維度
# 安全氣囊, 進口別, 傳動系統
table(Cars93$AirBags, Cars93$Origin, Cars93$DriveTrain)

# 類別平均值計算
aggregate(formula = Price ~ AirBags, data = Cars93, FUN = mean)

aggregate(formula = Price ~ AirBags + Origin, data = Cars93, FUN = mean)

# 繪圖 {grapics} -----
# (1).高階繪圖(high-level plotting) 
# (2).低階繪圖(low-level plotting)

# 散佈圖 plot
data(Cars93, package = "MASS")

plot(Cars93$Horsepower, Cars93$Price)

# 盒鬚圖 boxplot
boxplot(Cars93$Price)

Cars93_Price <- boxplot(Cars93$Price)

Cars93_Price

# 群組盒鬚圖 OrchardSprays 果園噴霧劑 -----
boxplot(decrease ~ treatment, 
        data = OrchardSprays, 
        col = "bisque")

# 水平群組盒鬚圖
boxplot(decrease ~ treatment, 
        data = OrchardSprays, 
        col = "bisque",
        horizontal=TRUE)

# 群組盒鬚圖-Y軸取log值
boxplot(decrease ~ treatment, 
        data = OrchardSprays, 
        col = "bisque", 
        log = "y")

# 長條圖 barplot -----
counts <- table(mtcars$gear)

barplot(counts, 
        main="Car Distribution",
        xlab="Number of Gears")

# 直方圖 hist
hist(iris$Petal.Length,
     xlab = "Petal Length",
     col = "orange",
     border = "blue",
     main = "iris-Petal.Length 直方圖")

# 直方圖優化
hist(iris$Petal.Length,
     xlab = "Petal Length",
     col = "orange",
     border = "blue",
     main = "iris-Petal.Length 直方圖",
     ylim = c(0,40))

# 實作練習21
# 散佈圖矩陣 pairs -----

# 繪圖結果輸出 -----
# http://rwepa.blogspot.com/2013/05/r.html

data(Cars93, package = "MASS")

pdf("Cars93_xyplot.pdf")

plot(Cars93$Horsepower, Cars93$Price,
     main = "Cars93 Scatter Plot",
     xlab = "Horsepower",
     ylab = "Price",
     pch = 16,
     col = Cars93$Type)

legend("topleft", 
       legend = levels(Cars93$Type), 
       col = 1:length(levels(Cars93$Type)),
       pch = 16)

dev.off()

# 四大繪圖類型 -----
# 比較 Comparison
# 組成 Composition
# 分配 Distribution
# 關係 Relationship

# 參考資料
# http://www.tatvic.com/blog/7-visualizations-learn-r/

# 視覺化圖表
# https://datavizcatalogue.com/

# 九大圖形 -----
# Scatter Plot     散佈圖 	plot
# Line Plot        線圖 		plot( .., type="l")
# Histogram	       直方圖 	hist
# Bar Chart	       長條圖 	barplot
# Box Plot		     盒鬚圖 	boxplot
# Pie Chart	       圓形圖 	pie
# Heat Map	       熱繪圖 	image 
# Correlation	     相關圖 	corrplot {corrgram}
# Interactive plot 互動式繪圖  {shiny}

# 相關圖 - corrplot 套件
library(corrplot)

corr <- cor(mtcars)

corrplot(corr)

corrplot(corr, method="pie")

corrplot(corr, method="number")

# 熱繪圖 image {graphics} -----
help(image)

# 平行座標軸 -----
help(parcoord, package = "MASS")

# 個案討論 -----
# GFC案例

# https://github.com/rwepa/DataDemo/blob/master/gfc.csv

gfc <- read.table("gfc-ansi.csv", head=TRUE, sep=",")

head(gfc)

str(gfc)

summary(gfc)

plot(gfc$amount, type = "l")

# 08.資料操作dplyr,視覺化ggplot2,互動式表格視覺化 -----

# 資料操作 dplyr -----
# r cran dplyr
# https://cran.r-project.org/web/packages/dplyr/index.html
# dplyr: A Grammar of Data Manipulation 資料操作文法
# dplyr = data frame + plyr

# plyr 發音 plier (鉗子), plyr 是 dplyr 的前個套件版本, 作者推薦使用 dplyr 套件
# plyr: https://www.slideshare.net/hadley/plyr-one-data-analytic-strategy

# filter                 : 條件式篩選資料
# slice                  : 列的指標篩選資料
# arrange                : 排序
# select                 : 選取行/更改欄位名稱
# rename                 : 選取所有行/更改欄位名稱
# distinct               : 選取不重覆資料
# mutate                 : 新增欄位,保留原資料
# transmute              : 新增欄位,不保留原資料
# summarise              : 群組計算

library(dplyr)

library(nycflights13) # 2013年NYC機場航班資料, 33萬筆資料 -----

flights # 336776*19

class(flights) # "tbl_df" "tbl" "data.frame"

# 如何轉換為 tbl_df, 使用 as.tbl -----
mytbl <- as.tbl(iris) # deprecated in dplyr 1.0.0.
mytbl <- tibble::as_tibble(iris)
class(mytbl)

# 資料結構與摘要 -----
str(flights)

summary(flights) # 有NA

head(flights)

tail(flights) # 注意:資料不是依照月,日排序

# filter 條件式篩選資料 -----
filter(flights, month == 1, day == 1)

flights[flights$month == 1 & flights$day == 1, ] # 基本指令, same as filter

filter(flights, month == 1 | month == 2) # AND 條件篩選, 同理 OR 使用 | 

# slice 列的指標篩選資料 -----
slice(flights, 1)           # 第1筆

slice(flights, n())         # 最後一筆

slice(flights, 123456:n())  # 第123456筆至最後一筆

# arrange 排序 -----
arrange(flights, year, month, day) # 依照年,月,日遞增排序

arrange(flights, desc(arr_delay)) # 依照延誤時間遞減排序

# select 選取行  -----
select(flights, year, month, day)

# Select 選取行, 使用 : -----
select(flights, year:dep_delay)

# select 選取行, 使用 負號, 表示刪除 -----
select(flights, -(year:day))

# select 選取行並且更改欄位名稱 -----
select(flights, tail_num = tailnum) # select 只選取 tailnum 1行資料

# rename 選取所有行/更改欄位名稱 -----
rename(flights, ActualDepatureTime = dep_time) # rename 選取所有資料行

# distinct 選取不重覆資料 -----
set.seed(168)

df <- data.frame(
  x = sample(10, 100, replace = TRUE), # rep = replace
  y = sample(10, 100, rep = TRUE)
) # 100*2

head(df)

distinct(df)

nrow(distinct(df))

nrow(distinct(df, x, y))

distinct(df, x) # 與下列結果相同 unique(df$x)

distinct(df, y) # 與下列結果相同 unique(df$y)

# mutate 新增欄位,保留原資料 -----
mutate(mtcars, displ_l = disp / 61.0237)

# tidyr套件-長寬資料轉換 -----
library(tidyr)

olddata_wide <- read.table(header=TRUE, text="
                           subject sex control cond1 cond2
                           1   M     7.9  12.3  10.7
                           2   F     6.3  10.6  11.1
                           3   F     9.5  13.1  13.8
                           4   M    11.5  13.4  12.9
                           ")
# Make sure the subject column is a factor
olddata_wide$subject <- factor(olddata_wide$subject)
str(olddata_wide)
olddata_wide

olddata_long <- read.table(header=TRUE, text='
                           subject sex condition measurement
                           1   M   control         7.9
                           1   M     cond1        12.3
                           1   M     cond2        10.7
                           2   F   control         6.3
                           2   F     cond1        10.6
                           2   F     cond2        11.1
                           3   F   control         9.5
                           3   F     cond1        13.1
                           3   F     cond2        13.8
                           4   M   control        11.5
                           4   M     cond1        13.4
                           4   M     cond2        12.9
                           ')
# Make sure the subject column is a factor
olddata_long$subject <- factor(olddata_long$subject)
str(olddata_long)
olddata_long

# gather: From wide to long
data_long <- gather(olddata_wide, condition, measurement, control:cond2)
data_long

# spread: From long to wide
data_wide <- spread(olddata_long, condition, measurement)
data_wide

# 字串處理套件-stringr 套件件 -----
library(stringr)

# str_detect, str_subset 範例1

# stringr
strings <- c(
  "apple", 
  "219 733 8965", 
  "329-293-8753", 
  "Work: 579-499-7527; Home: 543.355.3679"
)

phone <- "([2-9][0-9]{2})[- .]([0-9]{3})[- .]([0-9]{4})"

# Which strings contain phone numbers?
str_detect(strings, phone)

str_subset(strings, phone)

# str_detect, str_subset 範例2
fruit <- c("apple", "banana", "pear", "pinapple", "ndc")

str_detect(fruit, "a")  # 包括字母a

str_detect(fruit, "^a") # 開頭是字母a

str_detect(fruit, "a$") # 結尾是字母a

str_detect(fruit, "b")  # 包括字母b

str_detect(fruit, "pp") # 包括字母pp

str_detect(fruit, "[aeiou]") # 包括字母a 或 e 或 i 或 o 或 u

# str_locate, str_locate_all 範例

# Where in the string is the phone number located?
(loc <- str_locate(strings, phone))

str_locate_all(strings, phone)

# str_extract 篩選(部分)字串範例
shopping_list <- c("apples x4", "bag of flour", "bag of sugar", "milk x2")
str_extract(shopping_list, "\\d")              # 數字[0-9]
str_extract(shopping_list, "[a-z]+")           # 第1個英文字 
str_extract(shopping_list, "[a-z]{1,4}")       # 符合1~4次
str_extract(shopping_list, "\\b[a-z]{1,4}\\b") # 符合1~4次且刪除左邊或右邊一個空白

# str_extract_all 篩選(部分)字串範例
str_extract_all(shopping_list, "[a-z]+")
str_extract_all(shopping_list, "\\b[a-z]+\\b")
str_extract_all(shopping_list, "\\d")

# 正規表示式 Regular expression
?regex

# STAT 545, Chapter 11 Character vectors
# https://stat545.com/character-vectors.html 

# 視覺化 ggplot2 -----

# https://ggplot2-book.org/index.html

library(ggplot2)

?diamonds

str(diamonds) # 53940*10
set.seed(123456)
dsmall <- diamonds[sample(nrow(diamonds), 500), ]

# qplot: 散佈圖
qplot(carat, price, data=dsmall)

# qplot: 散佈圖+變數轉換
qplot(log(carat), log(price), data=dsmall)

# qplot: 散佈圖+群組顏色
qplot(carat, price, data=dsmall, colour=color)

# qplot: 散佈圖+群組形狀
qplot(carat, price, data=dsmall, shape=cut)

# qplot: 散佈圖+迴歸模型
p <- qplot(carat, price, data=dsmall, geom=c("point","smooth"), method="lm") # ERROR

# revised: stat_smooth
p <- qplot(carat, price, data=dsmall)
p + stat_smooth(method=lm)

# qplot: 散佈圖+局域加權迴歸線
p <- qplot(carat, price, data=dsmall,
           geom=c("point","smooth"), span=0.4)
p # ERROR

# revised
p <- qplot(carat, price, data = dsmall)
p + geom_point() + geom_smooth(span = 0.4)

# 使用 ggplot -----

# ggplot: 散佈圖
p <- ggplot(data=dsmall, mapping=aes(carat, price, color=color)) + geom_point(size=4)
p

# ggplot: 散點圖+線性迴歸
p <- ggplot(dsmall, aes(carat, price)) + geom_point() +
  geom_smooth(method="lm", se=FALSE)
p

# ggplot: 散點圖+群組線性迴歸
ggplot(dsmall, aes(carat, price, group=color)) + geom_point(aes(color=color), size=2) + geom_smooth(aes(color=color), method="lm", se=FALSE)

# ggplot: 線圖
p <- ggplot(iris, aes(Petal.Length, Petal.Width, group=Species, color=Species)) + geom_line()
p

# ggplot: 線圖+分面
# refer to materials

# ggplot2 盒鬚圖
# refer to materials

# ggplot2 gallery -----
# https://www.r-graph-gallery.com/

# 互動式表格視覺化 -----

# kableExtra 套件 -----
# r cran kableExtra
# http://haozhu233.github.io/kableExtra/awesome_table_in_html.html

library(kableExtra)

# kableExtra 範例
data(Cars93, package = "MASS")
mydf <- Cars93[1:20, 1:10]
kbl(mydf)

mydf %>%
  kbl() %>%
  kable_styling()

mydf %>%
  kbl(caption = "2021年4月X日空氣指標統計表") %>%
  kable_classic(full_width = FALSE, html_font = "Cambria")

mydf %>%
  kbl() %>%
  kable_material(c("striped", "hover"))


# reactable 套件 -----
library(reactable)   # 表格格式設定

# 基礎表格 usage
reactable(iris)

# 群組與匯總
reactable(iris, groupBy = "Species", columns = list(
  Sepal.Length = colDef(aggregate = "count"),
  Sepal.Width = colDef(aggregate = "mean"),
  Petal.Length = colDef(aggregate = "sum"),
  Petal.Width = colDef(aggregate = "max")
))

# 列明細
reactable(iris, details = function(index) {
  htmltools::div(
    "Details for row: ", index,
    htmltools::tags$pre(paste(capture.output(iris[index, ]), collapse = "\n"))
  )
})

# 互動式繪圖 plotly -----
library(plotly)
fig <- plot_ly(data = iris,
               x = ~Sepal.Length,
               y = ~Petal.Length,
               color = ~Species,
               colors = "Set1")
fig

# 中文的文字雲視覺化 -----
library(tmcn) # toTrad 簡體字轉繁體字
library(wordcloud2)

demoFreqC$V2 <- toTrad(as.character(demoFreqC$V2))

wordcloud2(demoFreqC, size = 2, color = "random-light", backgroundColor = "grey")

# 09.地理資料視覺化leaflet,機器學習與深度學習應用 -----

# 地理資料視覺化 leaflet -----

# https://cran.r-project.org/web/packages/leaflet/index.html

# https://rstudio.github.io/leaflet/

# leaflet 套件練習
# refer to materials

# 主題式地圖(Thematic map) - 政府開放資料為例
# http://rwepa.blogspot.com/2018/10/thematicmap.html
library(rgdal)
library(tmap)
# refer to RWEPA

# 機器學習 -----

# 資料探勘生命週期－CRISP-DM
# https://en.wikipedia.org/wiki/Cross_Industry_Standard_Process_for_Data_Mining 

# 迴歸分析 -----

# https://github.com/rwepa/DataDemo/blob/master/regression_01.pdf

# 迴歸分析繪圖 R code

plot(women, main="線性迴歸散佈圖", xlab="自變數(X)", ylab="依變數(Y)", pch=16, col="darkblue")
abline(lm(weight ~ height, data=women), col="red", lty=2, lwd=2)
text(59, 150, expression(y[i] == beta[0] + beta[1] * x[i] + epsilon[i]), pos=4, cex=1.5)
text(59, 144, expression(hat(y[i]) == hat(beta[0]) + hat(beta[1]) * x[i]), pos=4, cex=1.5)
arrows(62, 140, 63, 130.5, col="red", lwd=2)

# Simple linear regression -----
?lm
# my.lm <- lm(formula, data="xxx")
# formula: y ~ x1 + x2 + ... +xn
# end

# women: Average Heights and Weights for American Women
# y: weight
# x: height
fit.lm <- lm(weight ~ height, data=women)
summary(fit.lm)
# weight = -87.52+3.45*height

# verify residuals
names(fit.lm)
women$weight   # actual
fitted(fit.lm) # predicted
residuals(fit.lm) # residual=actual-predicted
women$weight - fitted(fit.lm)

# plot data
plot(women$height,women$weight, xlab="Height (in inches)", ylab="Weight (in pounds)", main="Average Heights and Weights for American Women")
abline(fit.lm, col="red")

# 深度學習應用 -----

# Anaconda Prompt (anaconda3)安裝 Python - 2個模組
# conda install -c conda-forge tensorflow
# conda install -c conda-forge keras

# 安裝 R - keras套件
# install.packages("keras")
# reticulate::install_miniconda()
# keras::install_keras()

library(keras)

# num_words=10000 採用前 10000 個常出現的字詞
# label 中 0 表示負評(negative), 1 表示正評(positive)
imdb <- dataset_imdb(num_words = 10000)
c(c(train_data, train_labels), c(test_data, test_labels)) %<-% imdb

train_data
str(train_data) # List of 25000

train_labels
class(train_labels) # integer 向量

max(sapply(train_data, max)) # 9999

# 下載單字與數值對應表,數值以整數表示
word_index <- dataset_imdb_word_index()

# 建立數值與單字對應表
reverse_word_index <- names(word_index)
names(reverse_word_index) <- word_index

# 我們對評論進行解碼, 指標採偏移3個方式進行
# 前3個預留編碼表示:
# 0: padding
# 1: start of sequence
# 2: unknown
decoded_review <- sapply(train_data[[1]], function(index) {
  word <- if (index >= 3) reverse_word_index[[as.character(index - 3)]]
  if (!is.null(word)) word else "?"
})
decoded_review
cat(decoded_review)

#
vectorize_sequences <- function(sequences, dimension = 10000) {
  # Create an all-zero matrix of shape (len(sequences), dimension)
  results <- matrix(0, nrow = length(sequences), ncol = dimension)
  for (i in 1:length(sequences))
    # Sets specific indices of results[i] to 1s
    results[i, sequences[[i]]] <- 1
  results
}
# Our vectorized training data
x_train <- vectorize_sequences(train_data)
# Our vectorized test data
x_test <- vectorize_sequences(test_data)

str(x_train[1,])

# Our vectorized labels
y_train <- as.numeric(train_labels)
y_test <- as.numeric(test_labels)

# 建立模組
# output = relu(dot(W, input) + b)

model <- keras_model_sequential() %>% 
  layer_dense(units = 16, activation = "relu", input_shape = c(10000)) %>% 
  layer_dense(units = 16, activation = "relu") %>% 
  layer_dense(units = 1, activation = "sigmoid")

model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy",
  metrics = c("accuracy")
)

# 要一點點時間
history <- model %>% fit(
  x_train,
  y_train,
  epochs = 20,
  batch_size = 512,
  validation_data = list(x_test, y_test)
)

str(history)

plot(history)

# 大型與大量資料處理 -----

# 大型資料處理 (data.table)
# 建立2300萬筆模擬資料
working <- "C:/rdata"
setwd(working)
getwd()
datasize <- 23000000
mydata <- matrix(c(NA), nrow=datasize, ncol=5)
set.seed(168)
mydata[,1] <- sample(c(1:17770), datasize, replace = TRUE)
mydata[,2] <- sample(c(1:480189), datasize, replace = TRUE)
mydata[,3] <- sample(c(1:5), datasize, replace = TRUE)
mydata[,4] <- sample(c(1999:2014), datasize, replace = TRUE)
mydata[,5] <- sample(c(1:12), datasize, replace = TRUE)
colnames(mydata) <- c("movie", "customer","rating","year", "month")
write.table(mydata, file="bigdata.txt", sep=",", row.names=FALSE, col.names=TRUE)
# 2300萬*5, 491MB

# Ctrl + Shift + F10: 重新啟動R
system.time(bigdata1 <- read.csv("C:/rdata/bigdata.txt", header=TRUE)) # 85秒

# Ctrl + Shift + F10: 重新啟動R
library(data.table)

system.time(movies <- fread("C:/rdata/bigdata.txt")) # 1.22秒

dim(movies) # 23000000*5

summary(movies)

class(movies)

# 大量資料處理
working_path <- "C:/rdata"
setwd(working_path)
getwd()

sample1 <- iris[sample(1:nrow(iris),10),]
sample2 <- iris[sample(1:nrow(iris),10),]
sample3 <- iris[sample(1:nrow(iris),10),]

write.table(sample1, file="sample1.csv", sep=",", row.names=FALSE)
write.table(sample2, file="sample2.csv", sep=",", row.names=FALSE)
write.table(sample3, file="sample3.csv", sep=",", row.names=FALSE)

files <- dir(getwd(), pattern="sample.*.csv", recursive=TRUE, full.names=TRUE)
files
tables <- lapply(files, read.table, header=TRUE, sep=",") # list
sample.all <- do.call(rbind, tables) # data.frame
sample.all

# 10.基礎互動式shiny,進階互動式shinyServer佈署 -----

# https://shiny.rstudio.com/
# https://www.rstudio.com/resources/webinars/

# 自動安裝套件 -----
usedpackages <- c("shiny", "ggplot2")

verify.packages <- function(need.packages) {
  for (x in need.packages) {
    if (!x %in% installed.packages()[,"Package"])
      install.packages(x)
  }
}
verify.packages(usedpackages)

# 基礎互動式shiny -----

library(shiny)

# 顯示內建11個範例
dir(paste0(.libPaths(), "/shiny/examples"))

# shiny example - 01_hello
runExample("01_hello")

runExample("02_text")

runExample("03_reactivity")

# 實作練習22 -----
# 建立第一個shiny網頁程式 - myFirstShiny
# 以 "02_text"為基礎, 複製為"C:\rdata\myFirstShiny"資料夾,完成以下功能:
# 1.修改標題為　myFirstShiny 
# 2.整合 「01_hello」: sidebarInput
# 3.整合 「01_hello」: renderPlot(繪製第1個變數之直方圖)
# 4.將直方圖標題改為選取之資料集名稱

# 輸入控制項 -----
?selectInput

# selectInput 下拉式選單:如果資料有很多筆,可使用list物件

# 檔案上傳 -----
runExample("09_upload")

# 輸出控制項-文字/表報 -----

# render函數對照表
# *Output (ui.R)
ls("package:shiny", pattern="Output$") # 9個

# render* (server.R)
ls("package:shiny", pattern="^render") # 8個

runExample("02_text")
# 比對以下表格:
# 文字: verbatimTextOutput("summary") --> output$summary <- renderPrint({})
# 報表: tableOutput("view") --> output$view <- renderTable({})

# 輸出控制項 - ggplot2 -----
# server.R 採用 renderPlot

# shiny 範例 - shinyCurve -----

# 展示 https://rwepa.shinyapps.io/shinyCurve/

# 程式碼 https://github.com/rwepa/DataDemo/tree/master/shinyCurve

# 進階互動式shiny Server佈署 -----

# 版面配置 -----

# 1.側邊佈局 Sidebar Layout
# 2.網格佈局 Grid Layout
# 3.分頁佈局 Tabsets Layout
# 4.瀏覽選單佈局 Navbar Pages
# 5.瀏覽下拉式選單佈局 Navbar Menu

# HTML UI -----
# refer to materials

# 反應型函數(Reactive function) -----
# reactiveFunctionName <- reactive({
#    ...
# })
runExample("03_reactivity")

# isolate -----
# refer to materials

# shape檔案的輸入與處理 -----

# CRAN Task View: Analysis of Spatial Data
# https://cran.r-project.org/web/views/Spatial.html

# 空間地理視覺化-maps 套件 -----

library(maps)
help(package="maps")
help(map, package="maps")

# draw low resolution map of the world
map()
map("world", fill=TRUE, col=2:8)

# draw county map
map("usa")
map(database="state")
map("france")
map("italy")
map("nz")

# states map
map('state', c('new york', 'new jersey'))
map('county', c('new york','new jersey'), fill=TRUE, col=1:10)
map.axes()

# country map
map("world", "China")
map.cities(country = "China", capitals = 3)

# 台灣地圖 -----
# taiwan map
map("world", xlim=c(117,123), ylim=c(21.5,26), mar=c(3,2,1,1))
# map.cities(country = "Taiwan")
map.axes()
# str(x.taiwan)

# taiwan cities
data(world.cities)
x <- world.cities
x.taiwan <- x[x$country.etc=="Taiwan", ]
x.taiwan.city <- x.taiwan[x.taiwan$name %in% c("Taipei","Taichung","Kaohsiung"),]
map.cities(x.taiwan.city, capital=1) # taipei
map.cities(x.taiwan.city, label=TRUE)

# ESRI Shapefile（shp），或簡稱shapefile，是美國環境系統研究所公司（ESRI）開發的一種空間資料開放格式。該檔案格式已經成為了地理資訊軟體界的一個開放標準。

# 空間地理視覺化-sp 套件 -----
library(sp)
?sp

# 空間地理視覺化-maptools 套件 -----

# (1).鄉鎮市區界線(TWD97經緯度) shapes檔案(較詳細)
# https://data.gov.tw/dataset/7441

# 線上新版資料
# mapdata202104280245.zip --> 解壓縮至 C:\rdata\mapdata202104280245 目錄中

# (2).直轄市、縣市界線(TWD97經緯度) shapes檔案
# https://data.gov.tw/dataset/7442

library(maptools)
twn <- readShapePoly("C:/rdata/mapdata202104280245/TOWN_MOI_1100415.shp") 
# Warning message:
# readShapePoly is deprecated; use rgdal::readOGR or sf::st_read 

library(rgdal)
twn <- readOGR(dsn="C:/rdata/mapdata202104280245", "TOWN_MOI_1100415")

summary(twn)
class(twn) # SpatialPolygonsDataFrame
names(twn) # 7個欄位
names(attributes(twn)) # 7個屬性
head(twn@data) # 有亂碼

# 轉換縣市為正常中文顯示
twn@data$COUNTYNAME <- iconv(twn@data$COUNTYNAME, from = "UTF-8", to="UTF-8")

# 轉換區鄉縣鎮為正常中文顯示
twn@data$TOWNNAME <- iconv(twn@data$TOWNNAME, from = "UTF-8", to="UTF-8")

head(twn@data$COUNTYNAME)
head(twn@data$TOWNNAM)

str(twn@data)
head(twn@data)

str(twn@polygons[[1]])
twn@polygons[[1]]

plot(twn)

# 實作練習23
# 繪製台灣縣市界圖 -----
# https://data.gov.tw/dataset/7442

# 實作練習24
# 加入地理中心標籤 -----
# https://data.gov.tw/dataset/7442

# 實作練習25
# 繪製北北基地圖 -----
# https://data.gov.tw/dataset/7442

# 地理資料－shiny進階網頁程式-rgdal 套件 -----
# 配合 http://data.gov.tw/dataset/7442

library(rgdal)

twn <- readOGR(dsn="C:/rdata/mapdata202008310842", "COUNTY_MOI_1090820")

twn@data$COUNTYNAME <- iconv(twn@data$COUNTYNAME, from = "UTF-8", to="UTF-8")

twn@data
str(twn@data)
class(twn)

twn@polygons
length(twn@polygons)
which(twn@data$COUNTYNAME == "臺北市")

# str(twn@polygons)
twn@polygons[[7]] # 臺北市
str(twn@polygons[[7]])
slotNames(twn@polygons[[7]])
## [1] "Polygons" "plotOrder" "labpt" "ID" "area"

twn@polygons[[7]]@Polygons[[1]]@coords
str(twn@polygons[[7]]@Polygons[[1]]@coords) # 8473*2

plot(twn@polygons[[7]]@Polygons[[1]]@coords) # 臺北市

# 完成版
plot(twn@polygons[[7]]@Polygons[[1]]@coords, 
     pch=".",
     xlab="經度",
     ylab="緯度",
     main="臺北市地圖",
     sub="資料來源:政府資料開放平台 URL: http://data.gov.tw/node/7442",
     cex.sub=0.7)

abline(h=seq(25, 25.2, by=0.05), col="grey", lty="dotted")
abline(v=seq(121.5, 121.65, by=0.05), col="grey", lty="dotted")

# 顧客連接分析 demo -----
# https://github.com/rwepa/DataDemo/tree/master/shinyCustomerConnect 

# 如何擷取繪圖資料
# http://shiny.rstudio.com/articles/plot-interaction.html

# shiny 認證 (Authentication)
# https://github.com/PaulC91/shinyauthr

# shiny 二階段選取
library(shiny)
runApp(list(
  ui = bootstrapPage(
    selectInput('dataset', '選取資料集', c('mtcars', 'iris', 'Orange')),
    selectInput('columns', '欄位名稱', "")
  ),
  server = function(input, output, session){
    
    outVar <- reactive({
      mydata = get(input$dataset)
      names(mydata)
    })
    
    observe({
      updateSelectInput(session, "columns",
                        choices = outVar()
      )})
  }
))

# shiny App 如何佈署
# 方法1: shiny server 免費版(安裝於住家/公司)
# 方法2: shiny Server Pro 付費版
# 方法3: https://www.shinyapps.io/

# 彩蛋題-RFM分析 (RFM analysis) -----

# RFM是一種用於分析客戶價值的方法 
# 常用於銷售資料庫,零售和服務分析之中,包括3項重要的指標:
# 1.R 最近消費(Recency)   - 天數
# 2.F 消費頻率(Frequency) - 次數
# 3.M 消費金額(Monetary)  - 元數

# R 最近消費 -----

# 客戶最近購買與上次購買的時間差.
# 例: 將最近購買日期分為4個等級,編碼等級越高的客戶,表示最近購買比率較高
# 最近購買日期的前25%,R編碼為4
# 50%-75%,R編碼為3
# 25%~50%,R編碼為2
# %25以下,R編碼為1

# 最近消費日期很小  ......        # 最近消費日期很大
# 0 ..[4].. 25% ..[3].. 50% ..[2].. 75% ..[1].. 100%

# F 消費頻率 -----

# 客戶在一定期間內購買產品的次數.
# 編碼等級越大的客戶,其消費頻率越高,忠誠度與顧客價值也越高.
# 同理購買次數最多的前25%,編碼為4,其他依序為3,2,1

# M 消費金額 -----

# 客戶在一定期間內購買產品的總金額.
# 編碼等級越高的客戶,其消費金額越高,顧客價值也越高.
# 同理消費金額最多的前25%,編碼為4, 其他依序為3,2,1

# RFM功能 -----

# 1.了解企業的銷售統計分析.
# 2.有效的運用行銷預算,進行最佳銷售產品分析.
# 3.對不同的客群給予不同的優惠,進行客製化行銷.
# 4.增加顧客生命週期,培養每一位顧客成為貴客(新客-->常客-->貴客).

# 載入套件 -----

library(readxl) # 讀取 Excel 檔案
# 參考 R入門資料分析與視覺化應用 3-12 將R資料匯出為CSV/Excel檔案

library(dplyr) # 資料處理文法
# 參考 R入門資料分析與視覺化應用 3-11使用dplyr套件,加速資料處理

library(ggplot2) # 繪圖文法
# 參考 R入門資料分析與視覺化應用 4-3 圖形文法繪圖ggplot2套件

# 匯入銷售資料 -----
# 資料來源 http://archive.ics.uci.edu/ml/datasets/online+retail

# 欄位說明
# InvoiceNo   發票編號
# StockCode   產品編號
# Description 產品說明
# Quantity    數量
# InvoiceDate 發票日期
# UnitPrice   單價
# CustomerID  客戶編號
# Country     客戶居住國家

sale <- read_excel("Online Retail.xlsx") # 541909*8(約54萬筆)

# 資料結構
str(sale)

# 資料摘要
summary(sale)

# 資料處理 -----
# Quantity 有負數
# UnitPrice 有負數
# CustomerID 有NA

sale <- sale %>%
  mutate(Quantity = replace(Quantity, Quantity <= 0, NA),
         UnitPrice = replace(UnitPrice, UnitPrice <= 0, NA))

sale <- sale %>% na.omit(sale) # 397884*8

# 將字元向量轉換成因子(factor)向量
sale <- sale %>%
  mutate(InvoiceNo = as.factor(InvoiceNo),
         StockCode = as.factor(StockCode),
         InvoiceDate = as.Date(InvoiceDate, "%m/%d/%Y"),
         CustomerID = as.factor(CustomerID), 
         Country = as.factor(Country))

# 新增 商品銷售總金額 GMV (Gross Merchandise Volume) 欄位
sale <- sale %>%
  mutate(GMV = Quantity*UnitPrice) # 397884*9

# 篩選欄資料並新增 df_customer 物件 397884*3
df_customer <- sale %>%
  select(CustomerID, InvoiceDate, GMV)

# 前三大商品銷售總金額國家{英國,荷蘭,愛爾蘭}
sale %>%
  group_by(Country) %>%
  summarise(totalGMV = sum(GMV)) %>%
  arrange(desc(totalGMV)) %>%
  print(n = 3)

# 依國家別,由大至小排序繪製商品銷售總金額
totalGMV <- sale %>%
  group_by(Country) %>%
  summarise(totalGMV = round(sum(GMV))) %>%
  arrange(desc(totalGMV)) %>%
  print(n = Inf)

# 除了 United Kingdom 以外, 依國家別,繪製前10大國家之商品銷售總金額
totalGMV %>%
  slice(2:11) %>%
  ggplot(aes(x=reorder(Country, totalGMV), y=totalGMV)) +
  geom_bar(stat="identity", fill="darkgray") +
  coord_flip() +
  geom_text(aes(label=totalGMV)) +
  labs(title = "前10大國家之商品銷售總金額統計圖", x = "國家", y = "銷售總金額") +
  theme(plot.title = element_text(hjust = 0.5))

# RFM Analysis

analysis_date <- as.Date("2020/03/25")

df_RFM <- sale %>% 
  group_by(CustomerID) %>% 
  summarise(recency = as.numeric(analysis_date - max(InvoiceDate)),
            frequency = n_distinct(InvoiceNo),
            monetary = sum(GMV)) # 4338*4

summary(df_RFM)

# 建立 RFM分析

# R_分數
# 最近消費百分位數(25%, 50%, 75%),將資料分成4個區間.
# 數值愈小,表示最近消費愈佳,編碼為4
# 0% --- 25% --- 50% --- 75% --- 100%
# 編碼 4      3       2       1

df_RFM$R_Score <- NA
df_RFM$R_Score[df_RFM$recency >= quantile(df_RFM$recency, probs=0.75)] <- 1 # 日期愈遠,編碼愈小

df_RFM$R_Score[df_RFM$recency >= quantile(df_RFM$recency, probs=0.50) & 
                 df_RFM$recency < quantile(df_RFM$recency, probs=0.75)] <- 2

df_RFM$R_Score[df_RFM$recency >= quantile(df_RFM$recency, probs=0.25) & 
                 df_RFM$recency < quantile(df_RFM$recency, probs=0.50)] <- 3

df_RFM$R_Score[df_RFM$recency < quantile(df_RFM$recency, probs=0.25)] <- 4

# F_分數
# 消費頻率百分位數(25%, 50%, 75%),將資料分成4個區間.
# 數值愈小,表示消費頻率較少,編碼為1
# 0% --- 25% --- 50% --- 75% --- 100%
# 編碼 1      2       3       4

df_RFM$F_Score[df_RFM$frequency >= quantile(df_RFM$frequency, probs=0.75)] <- 4

df_RFM$F_Score[df_RFM$frequency >= quantile(df_RFM$frequency, probs=0.50) & 
                 df_RFM$frequency < quantile(df_RFM$frequency, probs=0.75)] <- 3

df_RFM$F_Score[df_RFM$frequency >= quantile(df_RFM$frequency, probs=0.25) & 
                 df_RFM$frequency < quantile(df_RFM$frequency, probs=0.50)] <- 2

df_RFM$F_Score[df_RFM$frequency < quantile(df_RFM$frequency, probs=0.25)] <- 1

##############################
# 實作練習參考說明
##############################

# 實作練習16 -----
# R 執行畫面
plot(runif(100), type="l", main= "R大數據分析")
demo(graphics)
demo(persp)
# analysis: refer to materials

# 實作練習17 -----
# 新增R檔案練習
# 使用R原生環境,輸入以下程式碼, 另儲存成 myfirst.R
plot(runif(10), type="b", main= "R大數據分析")
x <- rnorm(10)
x
pairs(iris[-5], pch=16, col=iris$Species, main="RWEPA-iris資料集散佈圖矩陣")
# analysis: refer to materials

# 實作練習18 -----
# 練習儲存 aq.Banqiao.Xizhi 為 aq.Banqiao.Xizhi.RData
# 練習載入 aq.Banqiao.Xizhi.RData

save(aq.Banqiao.Xizhi, file="aq.Banqiao.Xizhi.RData")
load("aq.Banqiao.Xizhi.RData")
# # analysis: refer to materials

# 實作練習19 -----

# 資料框的操作
# 練習1.iris {datasets} 操作
# 找出 Sepal.Length變數大於中位數的資料集
# analysis:
iris$Sepal.Length[iris$Sepal.Length > median(iris$Sepal.Length)]

# 練習2.Cars93 {MASS}操作,資料篩選
data(Cars93, package = "MASS")
Cars93
str(Cars93)
summary(Cars93)
# 練習列,行,條件式資料篩選

# analysis:
# 列資料篩選
Cars93[1:3,]
Cars93[c(2,4,6,90),]

# 行資料篩選
Cars93[1]
Cars93[,1]
Cars93["Manufacturer"]

Cars93[2:4]
Cars93[,2:4]

head(Cars93[c(1,3,5,7)])
head(Cars93[c("Manufacturer", "Type", "Price", "MPG.city")])

# 條件式資料篩選
Cars93[Cars93$Price > 30,]
Cars93[Cars93$Price > 30 & Cars93$Type == "Large",]

# 練習3.計算 Luggage.room 的平均值為何?
# 將 Luggage.room 的遺漏值以平均值填補
mean(Cars93$Luggage.room) # NA ???
mean(Cars93$Luggage.room, na.rm = TRUE)
sum(is.na(Cars93$Luggage.room)) # 11
Cars93$Luggage.room[is.na(Cars93$Luggage.room)] <- mean(Cars93$Luggage.room, na.rm = TRUE)
sum(is.na(Cars93$Luggage.room)) # 0

# 實作練習20 -----
# 自訂函數:輸入iris 資料集計算每列第2大數值的向量結果
# analysis: refer to materials and try it

# 實作練習21
# 散佈圖矩陣 pairs -----
# analysis: refer to materials and try it

# 實作練習22
# 建立第一個shiny網頁程式 - myFirstShiny -----
# 以 "02_text"為基礎, 複製為"C:\rdata\myFirstShiny"資料夾,完成以下功能:
# 1.修改標題為　myFirstShiny 
# 2.整合 「01_hello」: sidebarInput
# 3.整合 「01_hello」: renderPlot(繪製第1個變數之直方圖)
# 4.將直方圖標題改為選取之資料集名稱
# analysis: refer to materials and try it

# 實作練習23
# 繪製台灣縣市界圖 -----
# https://data.gov.tw/dataset/7442

library(rgdal)
twn <- readOGR("練習輸入")

summary(twn)

class(twn) # SpatialPolygonsDataFrame

names(twn) # 4個欄位

names(attributes(twn)) # 7個屬性

twn@data$COUNTYNAME <- iconv(twn@data$COUNTYNAME, from = "UTF-8", to="UTF-8")

str(twn@data)

head(twn@data)

str(twn@polygons[[1]])

twn@polygons[[1]]

attributes(twn@polygons[[1]])

plot(twn, main="台灣縣市界圖")

plot(twn, main="台灣縣市界圖", col = "grey93")

plot(twn, main="台灣縣市界圖", col = c(2:8))

plot(twn, main="台灣縣市界圖", col = colors()[1:22])

# 實作練習24
# 加入地理中心標籤 -----
# https://data.gov.tw/dataset/7442

plot(twn, main="台灣縣市界圖", col="cadetblue", border="grey")

twn.center <- data.frame(lon=120.9817558, lat=23.973786)

twn.center.sp <- SpatialPoints(as.matrix(twn.center))

plot(twn.center.sp, add=TRUE, col="firebrick", pch=16, size=4)

text(twn.center, labels = "虎子山")

# 實作練習25
# 繪製北北基地圖 -----
# https://data.gov.tw/dataset/7442

countryselect <- c("臺北市", "新北市", "基隆市")

ind <- which(twn@data$COUNTYNAME %in% countryselect)

twn.ttk <- twn[ind,]

plot(twn.ttk, main="北北基地圖", col=c("aquamarine4", "palegreen", "deepskyblue2"))

# shiny 範例 01_hello -----
runExample("01_hello")

# shiny 繪圖中文字型錯誤 -----
# updated: 2021.8.26

# 方法1 使用 family 參數
# 範例:使用 Windows 微軟正黑體字型
# plot(..., family = "Microsoft JhengHei UI")

# 方法2 使用 showtext 套件
library(shiny)
library(showtext)

## Loading Google fonts (https://fonts.google.com/)
font_add_google(name = "Noto Sans TC", family = "twn")
showtext_auto()

# hist(..., family = "twn")

# https://rwepa.shinyapps.io/myFirstShiny/
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
# 謝謝您的聆聽 , Q & A
# 完成R之旅 ^_^
