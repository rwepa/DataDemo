# program : 物聯網與大數據整合應用
# title   : 溫度感測案例分析
# author  : Ming-Chang Lee
# email   : alan9956@gmail.com
# RWEPA   : http://rwepa.blogspot.tw/
# GitHub  : https://github.com/rwepa
# date    : 2020.10.15

# 資料說明
# https://github.com/rwepa/DataDemo#iot-tempcsv

# 下載 IOT-temp.csv 資料集
# https://github.com/rwepa/DataDemo/blob/master/IOT-temp.csv

# 使用 read.table 匯入資料
# header = TRUE   資料第1列是標題列
# sep = ","       區隔符號

iot <- read.table('C:/rdata/IOT-temp.csv', header = TRUE, sep = ",")

# 顯示資料集
iot

# 顯示前6筆資料
head(iot)

# 顯示前3筆資料
head(iot, n = 3)

# 顯示最後6筆資料
tail(iot)

# 資料摘要 97606*5
str(iot)

# 資料摘要,資料沒有NA
summary(iot)

# 字串轉換為因子factor
iot$room_id.id <- factor(iot$room_id.id)

iot$out.in <- factor(iot$out.in)

# 字串轉換為日期
iot$noted_date <- as.POSIXct(iot$noted_date, format="%d-%m-%Y %H:%M")

str(iot) # 資料型態轉換完成

# 除了id欄位,刪除重覆列, 37268*4
iot <- unique(iot[-1])

# 將資料依照noted_date, out.in 由小至大排序
iot <- iot[order(iot$noted_date, iot$out.in),]

head(iot)
# room_id.id          noted_date temp out.in
# 97604 Room Admin 2018-07-28 07:06:00   31     In
# 97577 Room Admin 2018-07-28 07:07:00   31     In
# 97580 Room Admin 2018-07-28 07:07:00   32    Out
# 97572 Room Admin 2018-07-28 07:08:00   31     In
# 97574 Room Admin 2018-07-28 07:08:00   31    Out
# 97570 Room Admin 2018-07-28 07:09:00   32    Out

tail(iot)
# room_id.id          noted_date temp out.in
# 11 Room Admin 2018-12-08 09:25:00   42    Out
# 9  Room Admin 2018-12-08 09:26:00   29     In
# 7  Room Admin 2018-12-08 09:28:00   29     In
# 5  Room Admin 2018-12-08 09:29:00   31     In
# 3  Room Admin 2018-12-08 09:29:00   41    Out
# 1  Room Admin 2018-12-08 09:30:00   29     In

summary(iot)

# 資料說明
# room_id.id: 只有1個資料值 Room Admin
# noted_date: 2018/7/28 ~ 2018/12/8
# temp: 21~51

# out.in: 二種組合

table(iot$out.in)

table(iot$out.in)/nrow(iot)

# 問題討論

# Q1.最高和最低溫度是多少？
# analysis:

# 最高溫度: 51
# 最低溫度: 21
# 差距溫度: 51 - 21 = 30

# Q2.室外溫度與室內溫度有何關係？
# analysis:

boxplot(iot$temp)

boxplot(temp ~ out.in, data = iot, main = '2018年7-12月溫度盒鬚圖統計圖')

# 盒鬚圖 boxplot
# 圓形: 離群值
# 最上方直線: 上限 upper bound
# 75百分位數: Q3
# 50百分位數: Q2 中位數
# 25百分位數: Q1
# 最下方直線: 下限 lower bound
# 上方離群值 x > Q3 + (Q3-Q1)*1.5
# 下方離群值 x < Q1 - (Q3-Q1)*1.5

box1 <- boxplot(iot$temp)
box1

box2 <- boxplot(temp ~ out.in, data = iot)
box2

# Q3.室內和室外的溫度變化如何？
# analysis:

# 室內溫度中位數 31
# 室內溫度       IQR = 32 - 29 = 3
# 室外溫度中位數 39
# 室外溫度       IQR = 43 - 34 = 9
# 室外溫度IQR較室內溫度IQR大

# Q4.資料趨勢如何？
# analysis:

iot$YearMonthDay <- format(iot$noted_date, "%Y-%m-%d")

aggregate(temp ~ out.in, data = iot, mean)

# 每日平均溫度
dayMean <- aggregate(temp ~ YearMonthDay, data = iot, mean)

dayMean$YearMonthDay <- as.Date(dayMean$YearMonthDay)

plot(dayMean$YearMonthDay, dayMean$temp,
     xlab="日期", 
     ylab="溫度", 
     main="2018年7-12月平均溫度統計圖",
     type = 'b')
grid()

library(ggplot2)

# ggplot2-線圖
ggplot(dayMean, aes(YearMonthDay, temp)) +
  geom_line() +
  ggtitle("2018年7-12月平均溫度統計圖") +
  theme(plot.title = element_text(hjust = 0.5)) # 設定標題置中排列

# ggplot2-群組線圖
dayoutinMean <- aggregate(temp ~ YearMonthDay + out.in, data = iot, mean)

dayoutinMean$YearMonthDay <- as.Date(dayoutinMean$YearMonthDay)

dayoutinMean

ggplot(dayoutinMean, aes(YearMonthDay, temp), group = out.in) +
  geom_line(aes(color = out.in)) +
  ggtitle("2018年7-12月平均溫度群組統計圖") +
  theme(plot.title = element_text(hjust = 0.5))
# 8月中旬室內溫度升高,但室外溫度降低
# 9月中旬開始有發現什麼嗎?

# Q5.您可以使用時間序列法來預測未來情況嗎？
# analysis:

library(forecast)

dayMean # 86*2

# 使用auto.arima
fit <- auto.arima(dayMean$temp)

forecast(fit, h=7) # 預測未來1週溫度

plot(forecast(fit, h=7))

# Q6.哪個月最熱/最冷？
# analysis:

# 10月最熱
# 9月最冷

# Q7.有找到來自氣候災難的警告信號(離群值)?

# 依據群組盒鬚圖有發現室內溫度有些較小是離群值
boxplot(temp ~ out.in, data = iot)
# end
