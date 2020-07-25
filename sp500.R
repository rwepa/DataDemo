# title    : sp500.R
# date     : 2020.7.25
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# Encoding : UTF-8

# sp500 資料處理與視覺化

# source: https://github.com/rwepa/DataDemo/blob/master/sp500.RData

library(zoo)

library(tidyverse)

load("sp500.RData")

str(sp500) # spec_tbl_df’, ‘tbl_df’, ‘tbl’ and 'data.frame

head(sp500)

tail(sp500)

# 方法1: 使用 ggplot2 視覺化
sp500 %>%
  ggplot(aes(x = date, y = close)) +
  geom_line(size = 1) +
  labs(title = "sp500收盤價",
       x = "Date", y = "Close")

# 方法2: 轉換為 zoo 物件並進行視覺化

mydf <- read.zoo(sp500, format = "%Y-%m-%d")

head(mydf)

tail(mydf)

str(mydf) # zoo

plot(mydf$close,
     main = "SP500 (1950-2015)",
     xlab="Date",
     ylab="Close")

grid()
