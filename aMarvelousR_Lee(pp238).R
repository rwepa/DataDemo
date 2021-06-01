# program : A Marvelous R -  Foundation
# author  : Ming-Chang Lee
# email   : alan9956@gmail.com
# RWEPA   : http://rwepa.blogspot.tw/
# GitHub  : https://github.com/rwepa
# reference: http://rwepa.blogspot.com/2013/01/r-201174.html
# Date    : 2011.7.4
# Updated : 2020.6.3
# Updated : 2021.4.11 新增 Chapter 6. iPAS-R-program (Chapter 6.iPAS - 科目二：資料處理與分析概論)
# Updated : 2021.4.11 新增 Chapter 7. ggplot2 套件

# 大綱 -----
# Chapter 1. Basic R
# Chapter 2. Preparing Data
# Chapter 3. Graphics
# Chapter 4. Applied Statistics
# Chapter 5. Application
# Chapter 6. iPAS - 科目二：資料處理與分析概論
# Chapter 7. ggplot2 套件

# Chapter 1. Basic R -----

# p.10
# hist and plot
x <- c(1:100)
y <- rnorm(100)*100
hist(y)
test.model <- lm(y ~ x)
test.model
plot(x,y)
library(help="graphics")
# end

# On-line help
?rnorm
?plot

#Information on package 'base'
library(help="base")
# end

# p.22
x <- c(1:10)
summary(x)
# end

# P.27
library(qcc)
?qcc

# p.28
# X-bar quality control chart
# load qcc library
library(qcc)
data(pistonrings)
attach(pistonrings)
pistonrings
diameter <- qcc.groups(diameter, sample)
qcc(diameter[1:25,], type="xbar")
# end

# TRY!
head(pistonrings)
head(pistonrings, n=3)
tail(pistonrings)
# end

# Chapter 2. Preparing Data -----

# p.40
# mode and length
x <- c(1:10)
mode(x)
length(x)
# end

# p.41
# name of object
A <- "WEPA"; compar <- TRUE; z <- 3+4i
mode(A); mode(compar); mode(z)
# end

# p.43
# Special numbers: Inf, -Inf, NaN, NA
x <- 5/0
x
exp(x)
exp(-x)
x - x
0/0
# NA
x.NA <- c(1,2,3)
x.NA
length(x.NA) <- 4
x.NA
# end

# p.46
# Joining (concatenating) vectors: c
x <- c(2,3,5,2,7,1)
x
y <- c(10,15,12)
y
z <- c(x, y)
z
# end

# p.47
# Subsets of vectors: Specify the numbers of the elements 
# that are to be extracted
# Assign to x the values 3, 11, 8, 15, 12
x <- c(3,11,8,15,12)

# Extract elements no. 2 and 4
x[c(2,4)]

# Use negative numbers to omit elements:
x[-c(2,4)]

# Generate a vector of logical (T or F)
x > 10

# Subset for user's defined conditions
x[x > 10]

# Vectors have named elements- method 1
c(ALAN=100, SERENA=2000, ANDY=300, ALPHA=400)[c("ALAN","ANDY")]

# Vectors have named elements- method 2
score <- c(ALAN=100, SERENA=2000, ANDY=300, ALPHA=400)
score[c("ALAN","ANDY")]
# end

# p.49
# Regular sequences: seq
x1 <- 1:100
x2 <- 100:1
x3 <- seq(1,10, 0.5)
x4 <- seq(length=9, from=1, to=5)
x5 <- c(1,2,2.5,6,10)
# Regular sequences: scan
x6 <- scan()

# p.50
# Regular sequences: rep
rep(1,5)

# Regular sequences: sequence
sequence(5)

# Error !!!
sequence(5,2)
# Now, it is correct for R-4.0.0.

# the concatenated sequences 1:5 and 1:2
sequence(c(5,2))

# the concatenated sequences 1:5, 1:2 and 1:3
sequence(c(5,2,3))
# end

# p.52
# gl
gl(3, 5)
gl(3, 5, length=30)
gl(2, 5, label=c("Male", "Female"))
# end

# TRY
x <- gl(3, 4, label=c("優良", "普通", "加油"), length=27)
x
# end

# p.54
# Built-in Constants
# Upper-case letters 
x <- LETTERS
x
length(x)

# Lower-case letters
y <- x[-c(2:10)]
y
length(y)

# Three-letter abbreviations for the month names
monthname.abb <- month.abb
monthname.abb
monthname.abb[c(1:10)]

# English names for the months 
monthname.full <- month.name
monthname.full

# Ratio of the circumference of a circle to its diameter
circle.area <- pi*10^2
circle.area
# end

# p.55
# NA
x <- c(pi, 1, 2,3)
x
x[c(2,4)] <- NA
x
is.na(x[2])
is.na(x[1])

# To replace all NAs by 0
x[is.na(x)] <- 0
x
# end

# p.58
# A vector of five numbers
v1 <- c(.29, .30, .15, .89, .12)
v1
class(v1)
typeof(v1)

# Coerces into a single type
v2 <- c(.29, .30, .15, .89, .12, "wepa")
v2
class(v2)
typeof(v2)

# vector(mode, length)
x1 <- vector(mode="numeric", length=1000000)

# View x1
head(x1)

# Verify a vector
is.vector(x1)

# vector
x2 <- c("Taiwan", "China", "USA")
x2
is.vector(x2)

# Expand the length of a vector
length(x2) <- 5
x2
# end

# p.61
# list
list.test1 <- list(1,2,3,4,5)
list.test1[1]
list.test1[[1]]

# Each element in a list may be given a name
product <- list(destination="Taipei",
                dimensions=c(3,6,10),price=712.19)
product[2]
product[[2]]
product$price
# end

# list all available data sets
data()
head(cars,n=3)
pts <- list(x=cars[,1], y=cars[,2])
plot(pts)
# end

# p.64
# factor
f1 <- factor(1:3)
f2 <- factor(1:3, levels=1:5)
f3 <- factor(1:3, labels=c("A", "B", "C"))
f4 <- factor(letters[1:6], label="YDU")
f4
class(f4)
eye.colors <- factor(c("brown", "blue", "blue", "green", 
                       "brown", "brown", "brown"))
eye.colors
levels(eye.colors)
# end

# p.66
# array
a1 <- array(letters)
class(a1)
dim(a1)

# array
a2 <- array(1:3, c(2,4))
a2
dim(a2)
length(a2)
a2[1, ] # select row 1
a2[, 4] # select column 4
# end

# p.67
# array
a3 <- array(data=1:24,dim=c(3,4,2))
a3
# end

# p.69
# matrix
matrix.data <- matrix(c(1,2,3,4,5,6), 
                      nrow = 2, ncol = 3, byrow=TRUE, 
                      dimnames = list(c("row1", "row2"), c("C1", "C2", "C3")))
matrix.data
# end

# p.71
# data.frame
x <- c(1:4); n <- 10; m <- c(10, 35); y <- c(2:4)
df1 <- data.frame(x, n)
df1
df2 <-data.frame(x, m)
df2
# end

# p.71
# TRY !
df3 <- data.frame(x, y) # ERROR
df4 <- data.frame(var1= rnorm(5), var2=LETTERS[1:5])
df4
# end

# p.72
# The data give the speed of cars and 
# the distances taken to stop.
data(cars)

help(cars)

class(cars)

head(cars)
# end

# p.75
# Time-series
data.ts <- ts(c(2,5,4,6,3,7,9:8),start=c(2009,2),frequency=4)
data.ts
is.ts(data.ts)
start(data.ts)
end(data.ts)
frequency(data.ts)
deltat(data.ts) # 0.25(=1/4)
plot(data.ts, type="b")
# end

# p.79
# Accessing Data
x <- c(1:8)

# how many elements?
length(x)

# ith element, i=2
x[2]

# all but ith element, i=2
x[-2]

# first k elements, k=5
x[1:5]

# last k elements, k=5
x[(length(x)-5+1):length(x)]

# specific elements
x[c(1,3,5)]

# all greater than some value
x[x>3]

# biger than or less than some values
x[x<3 | x>7]

# which indices are largest
which(x==max(x))
# end

# p.82
# Import/Export data
# Create a data directory C:\R.data
# Get working directory
getwd()

# Set working directory
dir.create("C:/R.data")
workpath <- "C:/R.data"
setwd(workpath)
getwd()

# p.86
# Create a CSV file (C:\R.data\score.csv)
# in which each field is separated by commas.
# Import dataset

# https://github.com/rwepa/DataDemo/blob/master/score.csv

score1 <- read.table(file="score.csv", header= TRUE, sep=",")

# TRY !
# score1 <- read.table(file="score.csv", header= TRUE)
score1
dim(score1)
names(score1)
row.names(score1)


# Add new column data for mid_term
mid.term <- matrix(c(60,80,65,85,80,90,99), nrow=7, ncol=1, 
                   byrow=FALSE,   dimnames = list(c(),c("mid.term")))
mid.term

# Merge two data.frame( score1 and mid_term)
score2 <- data.frame(score1, mid.term)
score2

# Export dataset
write.table(score2 , file= "score.final.txt", 
            sep = "\t", 
            append=FALSE, 
            row.names=FALSE, 
            col.names = TRUE, 
            quote= FALSE)
# end

# Chapter 3. Graphics -----

# p.91
demo(graphics)
# end

# p.96
# plot
data(cars)
head(cars, n=3)
plot(cars) # x-axis:speed; y-axis: dist

# p.97
# use the variable symbol "$"
plot(cars$dist, cars$speed)

# p.98
plot(cars, type="b")
# end

# p.99
# Available colors (#657)
# colors()
plot(cars, type="b", pch=5, col="red",
     xlab="Speed(mph)", ylab="Stop distance(ft)", 
     main="Speed and Stopping Distances of Cars",
     sub= "Figure 1: Plotting demonstration")
# end

# p.100
# Barplot
CarArrived <- table(NumberOfCar <- rpois(100, lambda=5))
CarArrived
barplot(CarArrived)
barplot(CarArrived, col=rainbow(14))
#end

# p.101
# pie
# Sales ratio
pie.sales <- c(0.14, 0.30, 0.26, 0.15, 0.10, 0.05)
# Sales area
names(pie.sales) <- c("Taipei1", "Taipei2", "Taipei3", "Taichung", 
                      "Kao", "Other")
# default colours
pie(pie.sales)
# end

# p.102
# pie with customized colour
pie(pie.sales, col = c("purple", "violetred1", "green3", 
                       "cornsilk", "cyan", "white"))
# end

# p.103
# pie with density of shading lines
pie(pie.sales, density = c(5,20), clockwise=TRUE)
# end

# p.104
# Box-and-whisker plot(s) of the given (grouped) values.
mat <- cbind(Uni05 = (1:100)/21, Norm=rnorm(100), T5 = rt(100,df= 5), 
             Gam2 = rgamma(100, shape = 2))
head(mat)
boxplot(data.frame(mat), main = "boxplot")
# end

# p.106
# stem plot
mat <- round(rnorm(10,30,10),0)
mat
stem(mat)
# end

# p.108
# Customized plot for 6-Sigma Quality Level
z <- pretty(c(44,56), 50) # Find 50 equally spaced points
ht <- dnorm(z, mean=50,sd=1) # By default: mean=0, standard deviation=1
plot(z, ht, type="l", main="6-Sigma Quality Level", 
     xlab="Qualty characteristic", ylab="Quality Level" , 
     axes=FALSE, xlim=c(42,58), ylim=c(0,0.5))

# Add axis
# 1=below, 2=left, 3=above and 4=right
axis(side=1, c(42:58),tick = TRUE)
axis(side=2, tick = TRUE)

# Add vertical line
# h=0: horizontal line(s);v=0: vertical line(s)
abline(v=c(44,50,56), lty=c(1,2,1), col=c("red","blue","red"))  

# Add text
text(44,0.5,"LSL", adj = c(-0.2,0))
text(50,0.5,"T",adj = c(-0.2,0))
text(56,0.5,"USL",adj = c(-0.2,0))
# end

# p.111
# 3D plot
# scatterplot3d package
# setup plotting environment for 2 rows and 2 columns
# par(bg = "white")
op <- par(mfrow = c(2,2))

# method 1: scatterplot3d (type=point) - Parabola
library(scatterplot3d)
x <- seq(-3, 3, length = 30)
y <- x
f <- function (x,y) {a <- 9; a - x^2 - y^2}
scatterplot3d(x, y, f(x,y),
              highlight.3d=TRUE, col.axis="blue",
              pch=20,
              main="Euclidean Utility Function - parabola, (type=point)",
              xlab="X", ylab="Y", zlab="f(x,y)", 
              zlim=c(0,9),
              col.grid="lightblue", 
              type="p"
)

# method 2: scatterplot3d (type=point)
library(scatterplot3d)
x <- seq(-3, 3, length = 30)
f <- function (x,y) {a <- 9; a - x^2 - y^2}
x1 <- rep(x, 30)
x2 <- rep(x, each=30)
znew <- f(x1, x2)
scatterplot3d(x1, x2, znew,
              highlight.3d=TRUE, col.axis="blue",
              pch=20,
              main="Euclidean Utility Function, (type=point)",
              xlab="X", ylab="Y", zlab="f(x,y)", 
              zlim=c(0,9),
              col.grid="lightblue", 
              type="p"
)

# method 3: scatterplot3d (type=line)
library(scatterplot3d)
x <- seq(-3, 3, length = 30)
f <- function (x,y) {a <- 9; a - x^2 - y^2}
x1 <- rep(x, 30)
x2 <- rep(x, each=30)
znew <- f(x1, x2)
scatterplot3d(x1, x2, znew,
              highlight.3d=TRUE, col.axis="blue",
              pch=20,
              main="Euclidean Utility Function (type=line)",
              xlab="X", ylab="Y", zlab="f(x,y)", 
              zlim=c(0,9),
              col.grid="lightblue", 
              type="l"
)

# method 4: persp
x <- seq(-3,3,length = 30)
y <- x
f <- function (x,y) { a <- 9; a-x^2-y^2}
z <- outer(x,y,f)
persp(x,y,z,zlim = range(c(-10:10), na.rm = TRUE), 
      expand=1,theta = 30, phi = 30,
      col = "lightblue",ticktype="detailed", 
      xlab="X", ylab="Y", zlab="f(x,y)",
      main="Euclidean Utility Function")

# method 5: misc3d (need "rgl" package)
# misc3d package
library(misc3d)
parametric3d(
  fx = function(u, v) u,
  fy = function(u, v) v,
  fz = function(u, v) -9 - u^2 - v^2 ,
  fill = FALSE,
  color = "blue",
  scale = FALSE,
  umin = -3, umax = 3, vmin = -3, vmax = 3, n = 100)

# setup plotting environment to the default
# par(mfrow=c(1,1))
par(op)
# end

# p.120
# 3D plot - sample
?persp
demo(persp)
# end

# Chapter 4.Applied Statistics -----

# p.122
# descriptive statistics
# Set working directory
workpath <- "C:/R.data"
setwd(workpath)
# import data
score <- read.table(file="score.csv", header= TRUE, sep=",")
# view data
score
# end

# summary data
# TRY summary(score)
score[2]
score[, 2]
score[3, ]
score$quiz1
quiz1 <- score$quiz1
mean(quiz1)
max(quiz1)
min(quiz1)
# end

# standard deviation
std(quiz1) # error function

# solution 1
sqrt( sum( (quiz1 - mean(quiz1))^2 /(length(quiz1)-1)))

# solution 2
# user's function
std = function(x) sqrt(var(x))
std(quiz1)

# solution 3
sd(quiz1)
# end

# p.129
# sample- t.test
# H0: u=95, H1: u<>95
t.test.data <- rnorm(50, mean=100, sd=15)
t.test(t.test.data, mu=95)
# p value is small, reject H0
# end

# p.130
# wilcox.test(x, conf.int=TRUE)
wilcox.test.data <- rnorm(50, mean=100, sd=15)
wilcox.test(wilcox.test.data, conf.int=TRUE, conf.level=0.99)
# end

# p.133
# prop.test
prop.test(39,215,0.15)
# end

# p.135
# shapiro.test
shapiro.test(rnorm(100, mean = 5, sd = 3))
shapiro.test(runif(100, min = 2, max = 4))
# end

# p.139
# QQ plot without logarithmic transformation
# first: qqnorm, second: qqline
data(Cars93, package="MASS")
qqnorm(Cars93$Price, main="Q-Q Plot: Price")
qqline(Cars93$Price)

# QQ plot without logarithmic transformation
qqnorm(log(Cars93$Price), main="Q-Q Plot: log(Price)")
qqline(log(Cars93$Price), col=2)
# end

# p.145
# one-way amova
# Copy the data to C:\R.data

# Import data
# https://github.com/rwepa/DataDemo/blob/master/drink.csv

drink.sales <- read.table("drink.csv", header=TRUE, sep=",")
head(drink.sales)

# drink.type <- factor(gl(4,5,label=c(letters[1:4])))
drink.type <- gl(4,5,label=c(letters[1:4]))
drink.type

drink <- data.frame(drink.type=drink.type, drink.sales)
head(drink)
class(drink)

# method 1. oneway.test
drink.oneway <- oneway.test(drink$sales ~ drink$drink.type, 
                            var.equal=TRUE)
drink.oneway

# method 2. aov
drink.anova <- aov(drink$sales ~ drink$drink.type)
summary(drink.anova)

# method 3. Linear model
drink.lm <- lm(drink$sales ~ drink$drink.type)
anova(drink.lm)
# end

# p.149
# linear regression
# Build-in data: cars
# x: speed, y: dist
head(cars)
dim(cars)

# linear model
cars.lm <- lm(dist~speed, data=cars)
summary(cars.lm)
# end

# regression information
anova(cars.lm)
coefficients(cars.lm)
coef(cars.lm)
confint(cars.lm)
deviance(cars.lm)
effects(cars.lm)
fitted(cars.lm)
residuals(cars.lm)
resid(cars.lm)
summary(cars.lm)
vcov(cars.lm)
# end

# Chapter 5.Application -----

# p.157
# Rcmdr package
# install.packages("Rcmdr", dependencies=TRUE)

# p.160
# Run in native R, NOT FOR RSTUDIO.
library(Rcmdr)

# p.169
# View all available data sets
data()
# end

# p.171
# List the data sets in specific package 
data(package="qcc")
# end

# p.174
# Load the data sets in specific package
data(pistonrings, package="qcc")
# end

# p.174
# TRY
# Select data with "sampe=1"?
pistonrings.sample1 <- pistonrings[pistonrings$sample == 1,]
pistonrings.sample1
# end

# P.177
# Help and column names
help("pistonrings")
names(pistonrings)
# end

# p.182
# set global options
x <- sqrt(2)
x
options(digits=16)
x
# end

# P.183
# 下載10萬筆測試資料
# https://github.com/rwepa/DataDemo/blob/master/R03_Orders.txt

# p.193
# Probability function 
dnorm(1.96, 0, 1)
pnorm(1.96, 0, 1)
qnorm(0.975, 0, 1)
rnorm(5, 0, 1)
# end

dnorm(1.645)
pnorm(1.645)
pnorm(1.96)
pnorm(2)
qnorm(0.95, 0, 1)
# end

# p.194
# Random generation
# also runif(1,min=0,max=2)
runif(1,0,2) 

runif(5,0,2)

# 5 random numbers in [0,1]
runif(5) 

x <- runif(100) # get the random numbers U(0,1)
hist(x,probability=TRUE,col=gray(.9),main="uniform on [0,1]")
# end

# p.195
# Sample - binomial distribution
pbinom(3, 10, 0.1)
# end

# p.197
# Sample - normal distribution
pnorm(c(2.5), mean=0, sd=1, lower.tail=TRUE)
# end

# p.197
# The ppt is disabled.
# TRY P(Z<=a)=0.95
a <- qnorm(c(0.95), mean=0, sd=1, lower.tail=TRUE)
a
# end

# p.219
# Quality Control Chart
library(qcc)
workpath = "c:/R.data"
setwd(workpath)

# 先將資料複製到 C:\R.data 目錄
# 匯入資料

# https://github.com/rwepa/DataDemo/blob/master/hw1.csv
hw1 <- read.table("hw1.csv", header=TRUE, sep=",")
# 顯示資料
hw1

# 取出全部資料的第2-4欄
pcb <- hw1[, c(2:4)]; pcb

dim(pcb) # 包括 25列, 3行 資料

qcc(pcb, type="xbar") # 第22筆資料超出管制界限

qcc(pcb, type="R")    # 第15筆資料超出管制界限

pcb.modified <- pcb[-c(15,22), ] # 移除第15,22筆資料

dim(pcb.modified) # 包括 23列, 3行 資料

qcc(pcb.modified, type="xbar") # 製程有在管制界限之內嗎?

qcc(pcb.modified, type="R") # 製程有在管制界限之內嗎?
# end

# p.233
# The example of R for Support Vector Machines(SVM)
# 安裝SVM 套件 e1071
# 載入套件 e1071
library(e1071)
library(mlbench)

# 載入資料集 Glass in mlbench package
# 資料集 214 個觀測值,9 個變數,第9 個數數名稱為Type,
# 有7 個種類(1:7)
data(Glass)
head(Glass)

# 設定變數index 為編號1,2,…214.
index <- 1:nrow(Glass)

# 準備隨機抽樣並設定測試資料的編號
# 利用sample 取樣,將資料的1/3 做為測試資料的序號
testindex <- sample(index, trunc(length(index)/3))
# 設定測試資料 testset,共71 筆資料
testset <- Glass[testindex, ]
# > dim(testset) # 可知道有71 筆測試資料
# 將其他資料設定訓練資料 trainset,共143 個筆資料
trainset <- Glass[-testindex, ]

# 利用svm 執行並將結果存入變數svm.model
svm.model <- svm(Type ~ ., data = trainset, cost = 100, gamma = 1)

# 利用predict 執行測試資料的分類預測
svm.pred <- predict(svm.model, testset[, -10])
print(svm.pred)

# 利用 write 輸出結果
# 將結果輸出成CSV 檔案
write.table(svm.pred, file = "svm.test.csv", sep = ",")
# end

# Chapter 6.iPAS - 科目二：資料處理與分析概論 -----

setwd("C:/rdata")

# 1-1資料組織與清理 -----

# KNN demo -----
library(animation)

# 設定動畫參數
ani.options(interval = 1, nmax = 10)

# 建立訓練集,測試集
set.seed(168)
df <- iris[iris$Species != "setosa",]
df$Species <- factor(df$Species)
ind <- sample(2, nrow(df), replace = TRUE, prob = c(0.8, 0.2))
traindata <- df[ind == 1, 3:4]
testdata <- df[ind == 2, 3:4]

# KNN示範
knn.ani(train = traindata, test = testdata, cl = df$Species[ind == 1], k = 20)

# 資料標準化 -----
data(Cars93, package = "MASS")

# 直方圖
hist(Cars93$Price)
summary(Cars93$Price) # 原始資料 [7.4, 61.9]

# (0,1)標準化 -----

PriceMin <- min(Cars93$Price)
PriceMax <- max(Cars93$Price)

Cars93$PriceZeroOne <- (Cars93$Price - PriceMin)/(PriceMax - PriceMin)
head(Cars93$PriceZeroOne)
summary(Cars93$PriceZeroOne) # (0,1)標準化 [0, 1]

# min-max 標準化 -----

PriceMinNew <- 1
PriceMaxNew <- 10

Cars93$PriceMinMax <- PriceMinNew + 
  ((Cars93$Price - PriceMin)/(PriceMax - PriceMin))*(PriceMaxNew - PriceMinNew)

summary(Cars93$PriceMinMax)

# 標籤編碼 (Label encoding) -----

# 範例1 german_credit
# 參考 <<<R商業預測與應用>>>第3章 監督式學習商業預測
# https://courses.mastertalks.tw/courses/R-2-teacher

# https://github.com/rwepa/DataDemo/blob/master/german_credit.csv
credit <- read.csv("german_credit.csv") # 1000*10

str(credit)

head(credit)

# label encoding -----
credit$RiskEncoding <- ifelse(credit$Risk == "good", 1, 0)

head(credit$RiskEncoding)

table(credit$RiskEncoding)

# One-hot encoding -----

# Job 工作 {0,1,2,3}
# 0 - unskilled and non-resident 非技術人員和非居民
# 1 - unskilled and resident 非技術人員和居民
# 2 - skilled 技術人員
# 3 - highly skilled 高度技術人員

# 轉換為 factor
credit$JobOneHot <- factor(credit$Job, label = c("unskilled and non-resident", 
                                                 "unskilled and resident", 
                                                 "skilled", 
                                                 "highly skilled"))

str(credit$JobOneHot)

levels(credit$JobOneHot)

# method 1-使用 model.matrix {stats}
myonehot <- model.matrix(object = ~ JobOneHot - 1, data = credit) # matrix
head(myonehot)

# method 2-使用 dummyVars {caret}
library(caret)

dummy <- dummyVars(" ~ JobOneHot", data = credit)
dummy

# 範例2 鐵達尼號 : 使用 dummyVars 直接進行預測
library(earth)

data(etitanic, package = "earth")

head(etitanic)

head(model.matrix(survived ~ ., data = etitanic))

dummies <- dummyVars(survived ~ ., data = etitanic)

etitanic$PedictSurvived <- predict(dummies, newdata = etitanic)

head(etitanic)

# 1-2.資料摘要與彙總 -----

# 盒鬚圖 boxplot -----
data(Cars93, package = "MASS")

boxplot(Cars93$Price)

# 盒鬚圖的5個指標
# Lower bound, 25% quantile, Median, 75% quantile, Upper bound
# 下邊界, 25百分位數, 中位數, 75百分位數, 上邊界
Cars93_Price <- boxplot(Cars93$Price)
Cars93_Price

# 群組盒鬚圖 - 基礎繪圖
boxplot(Price ~ Origin, data = Cars93)

# 盒鬚圖 - ggplot2 -----

library(ggplot2)
p <- ggplot(Cars93, aes(y = Price)) + 
  geom_boxplot()
p

# 群組盒鬚圖 - ggplot2
p1 <- ggplot(Cars93, aes(x = Origin,y = Price)) + 
  geom_boxplot()
p1

# 匯出資料
write.table(Cars93, file = "C:/rdata/Cars93.csv", sep =",", row.names = FALSE)

# R - 排序 sort, order -----

x <- c(9,2,6,3,1)

sort(x)

order(x)

x[order(x)]

sort(x, decreasing = TRUE)

# 資料框排序 -----

df <- head(iris, n = 5)

# 遞增排序
df[order(df$Sepal.Length),]

# 遞減排序
df[order(df$Sepal.Length, decreasing = TRUE),]

# 群組個數 table -----
data(Cars93, package = "MASS")

table(Cars93$AirBags)

# 群組個數 table-2個維度

table(Cars93$AirBags, Cars93$Origin)

# 群組邊界計算 addmargins-預設值為總和
addmargins(table(Cars93$AirBags, Cars93$Origin))

# 群組邊界計算 addmargins-mean
addmargins(table(Cars93$AirBags, Cars93$Origin), FUN = mean)

# 群組百分比計算 prop.table
prop.table(table(Cars93$AirBags, Cars93$Origin))

# table 多維度: 安全氣囊, 進口別, 傳動系統
table(Cars93$AirBags, Cars93$Origin, Cars93$DriveTrain)

# 類別平均值計算
aggregate(formula = Price ~ AirBags, data = Cars93, FUN = mean)

aggregate(formula = Price ~ AirBags + Origin, data = Cars93, FUN = mean)

# 摘要 -----
summary(Cars93)

# 1-3.屬性轉換與萃取 -----

# 奇異值分解 (Singular Value Decomposition, SVD) -----
x <- matrix(1:6, byrow = TRUE, ncol = 2)
x
(s <- svd(x))
class(s) # list

# Mean normalization -----
# (x - mu)/(max - min)

x <- c(1, 2, 2, 4, 5)
(xmean <- mean(x))
(xmax <- max(x))
(xmin <- min(x))
(x - xmean)/(xmax - xmin)

# 裝箱 (Binning) -----

?cut

data(Cars93, package = "MASS")

quantile(Cars93$Price)

Cars93$Price

cut(x = Cars93$Price, breaks = c(0, 13, 23, Inf), labels = c("低", "中", "高"))

# scale
x <- head(Cars93[c('Price', 'Horsepower')])
x

apply(x, 2, mean)
apply(x, 2, sd)
scale(x)

op <- par(mfrow=c(1,2))
hist(Cars93$Price)
hist(scale(Cars93$Price))
par(op)

# 2-1.統計分析基礎 -----

# 百分位數 -----
# 預設值 0% 25% 50% 75% 100%
quantile(iris$Sepal.Length)

# 平均數𝜇之區間估計 - 母體變異數已知 -----
# 95%之信賴區間
alpha <- 0.05
sampleSD <- 5
sampleSize <- 16
sampleMean <- 60
zScore <- qnorm(p = alpha/2,  lower.tail = FALSE)
zScore

lowerBound <- sampleMean - zScore*sampleSD/sqrt(sampleSize)
upperBound <- sampleMean + zScore*sampleSD/sqrt(sampleSize)
print(c(lowerBound, upperBound))
# [1] 57.55005 62.44995

# 99%之信賴區間
alpha <- 0.01
zScore <- qnorm(p = alpha/2,  lower.tail = FALSE)
zScore

lowerBound <- sampleMean - zScore*sampleSD/sqrt(sampleSize)
upperBound <- sampleMean + zScore*sampleSD/sqrt(sampleSize)
print(c(lowerBound, upperBound))
# [1] 56.78021 63.21979

# t-檢定 -----
set.seed(168)
x <- rnorm(n = 10, mean = 5)
x           
t.test(x, mu = 5)

# 卡方檢定 -----
chisq.test(c(230,220,450))

mytest <- chisq.test(c(230,220,450))
names(mytest)
mytest$p.value

# 2-2.探索式資料分析與非監督式學習 -----

# 使用 dbscan {fpc} -----

library(fpc)
# https://cran.r-project.org/web/packages/fpc/index.html

df <- iris[,-5]

df.dbscan <- dbscan(df, eps=0.42, MinPts=5)

df.dbscan
# 資料分成3群(編碼1,2,3)
# 編碼0(第1行)表示離群值/噪音值

# border 邊界點
# seed   密度點
# DBSCN  計算集群的平均值(中心點)與K-means意義相同嗎?

# 2-3.線性模型與監督式學習 -----

# 線性模型 – R: lm {stats}
# 參考 https://github.com/rwepa/DataDemo/blob/master/marketing.R

# 下載資料
# https://github.com/rwepa/DataDemo/blob/master/marketing.csv

# 建立 y = β0 + β1 * x1 + β2 * x2 + β3 * x3

# x1: 自變數 youtube, x2: 自變數 facebook, x3: 自變數 newspaper
# y: 依變數 sales

sales_lm_all <- lm(sales ~ youtube + facebook + newspaper, data = marketing)

# 檢視模型結果
summary(sales_lm_all)

# 結果包括4大項目
# 1.Call: lm() 線性
# 2.Residuals: 線性迴歸模型的殘差
# 3.Coefficients: 迴歸係數, newspaper 的p值 大於 0.05, 考慮刪除此自變數.
# 4.統計值: 殘差標準差, R平方, 調整後R平方, F統計值, 自由度(DF), p-value

# Chapter 7. ggplot2 套件 -----

# https://cran.r-project.org/web/packages/ggplot2/index.html
# ggplot2: Create Elegant Data Visualisations Using the Grammar of Graphics
# 參考資料 https://ggplot2-book.org/

# ggplot2概念
# 1.以圖層(layers)為基礎的繪圖套件,它實現了Wilkinson (2005)的繪圖文法(Grammar of Graphics)概念.
# 2.一個圖形是由數個圖層所組成,其中一層包含了資料(data)層.
# 3.Wilkinson認為圖形繪製須結合數據與繪製規範,規範並非是圖形視覺效果的名稱(例如:長條圖,散佈圖,直方圖等).
# 4.規範應是一組共同決定圖形如何建立的規則 – a grammar of graphics.

library(ggplot2)

?diamonds

str(diamonds) # 53940*10

set.seed(168)

dsmall <- diamonds[sample(nrow(diamonds), 500),]

# ggplot: 散佈圖
p <- ggplot(data=dsmall, mapping=aes(carat, price, color=color)) + 
  geom_point(size=4)
p

# ggplot: 散點圖+線性迴歸
p <- ggplot(dsmall, aes(carat, price)) + 
  geom_point() +
  geom_smooth(method="lm", se=FALSE)
p

p <- ggplot(dsmall, aes(carat, price)) + 
  geom_point() +
  geom_smooth(method="lm", se=TRUE)
p

# ggplot: 散點圖+群組線性迴歸
ggplot(dsmall, aes(carat, price, group=color)) + 
  geom_point(aes(color=color), size=2) + 
  geom_smooth(aes(color=color), method="lm", se=FALSE)

# ggplot: 線圖
p <- ggplot(iris, aes(Petal.Length, Petal.Width, group=Species, color=Species)) +
  geom_line()
p

# ggplot: 線圖+分面 facet_wrap()
p <- ggplot(iris, aes(Sepal.Length, Sepal.Width)) + 
  geom_line(aes(color=Species), size=1) + 
  facet_wrap(~Species, ncol=1)
p

ggplot(mpg, aes(displ, hwy)) + 
  geom_point() + 
  facet_wrap(~class)

# ggplot2: 線圖+散佈圖
ggplot(mpg, aes(displ, hwy)) +
  geom_point() +
  geom_line()

# ggplot2: 散佈圖+線圖+群組
ggplot(mpg, aes(displ, hwy)) +
  geom_point(aes(color=factor(cyl))) +
  geom_line()

# R軟體開放資料應用-高速公路篇 使用ggplot2
# http://rwepa.blogspot.com/2019/05/highway.html
# end
