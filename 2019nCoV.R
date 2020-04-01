# title: 2019新型冠狀病毒視覺化
# date: 2020.2.13
# updated: 2020.3.17
# author: Ming-Chang Lee
# email: alan9956@gmail.com
# RWEPA: http://rwepa.blogspot.tw/
# GitHub: https://github.com/rwepa

# updated note:
# 1. 修改 read.table 為 read.csv

# data: https://github.com/CSSEGISandData/2019-nCoV

library(leaflet)
library(htmltools) # tag

# 確診 Confirmed
ncovConfirmedUrl <- "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
# 匯入資料
ncovConfirmed <- read.csv(ncovConfirmedUrl)

# 將 X 取代為空白
names(ncovConfirmed) <- gsub("X", "", names(ncovConfirmed))

# 使用strsplit, 依據 "." 進行字串分割
# unlist 將分割的 list 轉換為向量
# matrix 的 byrow=TRUE 可以將資料依玥順序排列
# as.data.frame 轉換為 data.frame 方便後序操作
# 月 日 年
mydf <- as.data.frame(matrix(unlist(strsplit(names(ncovConfirmed)[-c(1:4)], "\\.")), ncol=3, byrow=TRUE))

# 儲存轉換後的欄位名稱向量
myname <- c()

# 將欄位名稱 "1.22.20" 轉換為 "2020-1-21", 即 "年-月-日" 格式
# for (i in 1:...) { }, nrow(mydf) 表示列個數

for (i in 1:nrow(mydf)) {
  myname <- c(myname, paste0(paste0("20", mydf[i, 3]), "-", mydf[i, 1], "-", mydf[i, 2]))
}

# 刪除 mydf 物件
rm(mydf)

names(ncovConfirmed)[-c(1:4)] <- myname

head(ncovConfirmed)

# 使用 aggregate 計算各國家 2020-3-16 的合計, 須使用 ‵  ‵ 字元
ncovConfirmedAgg <- aggregate(`2020-3-16` ~ Country.Region, 
                              data=ncovConfirmed, 
                              sum)

# 使用 aggregate 計算各國家最近日期的合計
# names(ncovConfirmed)[ncol(ncovConfirmed)] 取出最後一個欄位名稱,其結果為字串
# get(names(ncovConfirmed)[ncol(ncovConfirmed)]) 將欄位名稱轉換為物件名稱

ncovConfirmedAgg <- aggregate(get(names(ncovConfirmed)[ncol(ncovConfirmed)]) ~ Country.Region, 
                              data=ncovConfirmed, 
                              sum)

names(ncovConfirmedAgg) <- c("CountryRegion", "Confirmed")

ncovConfirmedAgg <- ncovConfirmedAgg[order(ncovConfirmedAgg$Confirmed, decreasing=TRUE),]

(ncovTotalConfirmed <- sum(ncovConfirmedAgg$Confirmed))

# 死亡 Death
ncovDeath <- "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

ncovDeath <- read.csv(ncovDeath)

names(ncovDeath) <- gsub("X", "", names(ncovDeath))

mydf <- as.data.frame(matrix(unlist(strsplit(names(ncovDeath)[-c(1:4)], "\\.")), ncol=3, byrow=TRUE))

myname <- c()

for (i in 1:nrow(mydf)) {
  myname <- c(myname, paste0(paste0("20", mydf[i, 3]), "-", mydf[i, 1], "-", mydf[i, 2]))
}

rm(mydf)

names(ncovDeath)[-c(1:4)] <- myname

head(ncovDeath)

ncovDeathAgg <- aggregate(`2020-3-16` ~ Country.Region, data=ncovDeath, sum)

ncovDeathAgg <- aggregate(get(names(ncovDeath)[ncol(ncovDeath)]) ~ Country.Region, 
                          data=ncovDeath, 
                          sum)

names(ncovDeathAgg) <- c("CountryRegion", "Death")

ncovDeathAgg <- ncovDeathAgg[order(ncovDeathAgg$Death, decreasing=TRUE),]

(ncovTotalDeath <- sum(ncovDeathAgg$Death))

# 建立leaflet互動式地圖

title <- tags$h2(paste0("2020新型冠狀病毒感染人數全球分佈圖, ", date()))

datasource <- tags$div(
  HTML("Data: https://github.com/CSSEGISandData/2019-nCoV")
)

publish <- tags$div(
  HTML("Powerby:@RWEPA, Feb. 13, 2020.")
)

m <- leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(
    lng=ncovConfirmed$Long,
    lat=ncovConfirmed$Lat,
    popup=paste0(ncovConfirmed$Province.State, 
                 ", ", 
                 ncovConfirmed$Country.Region, 
                 " ",
                 names(ncovConfirmed)[ncol(ncovConfirmed)], 
                 " 確診: ", ncovConfirmed[,ncol(ncovConfirmed)])) %>%
  addControl(title, position="topright") %>%
  addControl(datasource, position="bottomleft") %>%
  addControl(publish, position="bottomright")

m  # Print the map
# end
