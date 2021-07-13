# title    : iPAS營運智慧分析師
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

# 載入 MASS 套件中的 Cars93 資料集
data(Cars93, package = "MASS")

# 顯示前6筆資料
head(Cars93)

# 資料結構
str(Cars93)

# 資料摘要-敘述統計
summary(Cars93)

# 次數分配表
table(Cars93$Type)

# 相對次數分配表
prop.table(table(Cars93$Type))

# 相對次數分配表(%)
round(prop.table(table(Cars93$Type))*100, 2)

# 長條圖 (bar graph)
barplot(sort(table(Cars93$Type), decreasing = TRUE), main = "汽車型式長條圖")

# 圓形圖 (pie chart)
lbls <- paste(names(table(Cars93$Type)), "\n", table(Cars93$Type), "%", sep="")
pie(table(Cars93$Type), labels = lbls, main = "汽車型式圓形圖")

# 盒鬚圖 boxplot
data(Cars93, package = "MASS")

boxplot(Cars93$Price)

# 盒鬚圖的5個指標
# Lower bound  下邊界
# 25% quantile 25百分位數
# Median       中位數
# 75% quantile 75百分位數
# Upper bound  上邊界

Cars93_Price <- boxplot(Cars93$Price)
Cars93_Price

# 群組盒鬚圖
boxplot(Price ~ Origin, data = Cars93)

# 散佈圖矩陣 Scatter Plot Matrix
pairs(iris[-5], col=iris$Species, pch = 16, main = "iris資料集散佈圖矩陣")

Cars93$Price

# 平均值
mean(Cars93$Price)

# 變異數
var(Cars93$Price)

# 標準差
sd(Cars93$Price)

# t檢定
set.seed(168)

x <- rnorm(n=10, mean =5)
x
t.test(x, mu = 5)

# 集群法示範 -----

library(animation)

kmeans.ani(x = cbind(X1 = runif(50), X2 = runif(50)), 
           centers = 3, 
           hints = c("Move centers!", "Find cluster?"), 
           pch = 1:3, 
           col = 1:3)

# KNN demo
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

# ggplot2-散佈圖矩陣
library(GGally)
ggpairs(iris[-5], aes(colour = iris$Species, alpha = 0.4))
cor(iris[-5])
