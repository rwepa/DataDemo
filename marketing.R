# title    : marketing資料集-迴歸分析(regression analysis)
# file     : marketing.R
# date     : 2020.12.3
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

# 安裝 rgl, car 套件
library(rgl)
library(car)

# 匯入 marketing 資料
urls <- "https://github.com/rwepa/DataDemo/blob/master/marketing.csv" # ERROR
urls <- "https://raw.githubusercontent.com/rwepa/DataDemo/master/marketing.csv" # OK
marketing <- read.csv(urls, header=TRUE, sep=",")
marketing

# 資料結構
str(marketing) # 200*4

# 資料摘要, facebook 有NA值
summary(marketing)

# 直方圖
hist(marketing$facebook)

# 計算 facebook 的中位數
marketingFacebookMedian <- median(marketing$facebook, na.rm=TRUE)

# 以中位數填補 facebook 遺漏值 (missing values)
marketing$facebook[is.na(marketing$facebook)] <- marketingFacebookMedian

# 資料摘要, facebook沒有NA值
summary(marketing)

# 散佈圖矩陣!有發現什麼樣式(patterns)嗎?
pairs(marketing, pch=16, cex=0.5)

# 建立線性模型
marketing_lm <- lm(sales ~ ., data=marketing)

# newspaper: p值沒有小於0.05,考慮刪除此變數
summary(marketing_lm)

# 建立修正後線性模型
marketing_lm_revised <- lm(sales ~ youtube + facebook, data=marketing)

summary(marketing_lm_revised)

# 繪製3d圖
scatter3d(sales ~ youtube + facebook, data=marketing, surface=FALSE)

# 加上線性預測
scatter3d(sales ~ youtube + facebook, data=marketing)

# 加上2次式預測
scatter3d(sales ~ youtube + facebook, data=marketing, fit="quadratic") 

# 加上平滑預測
scatter3d(sales ~ youtube + facebook, data=marketing, fit="smooth") 

# 顯示3筆 outliers
scatter3d(sales ~ youtube + facebook, data=marketing, id=list(n=3))
# end
