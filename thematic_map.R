# title    : 主題式地圖(Thematic Map)-以政府開放資料為例
# file     : thematic_map.R
# author   : Ming-Chang Lee
# date     : 2022.07.28
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

# 本例說明考量社會經濟等開放式資料，輔以主題式繪圖方式，提升資料視覺化品質，便於資料呈現與溝通。

# 參考網址: http://rwepa.blogspot.com/2018/10/thematicmap.html

# 步驟1: 下載社會經濟等開放式資料
# 本例以臺北市住宅竊盜點位資訊為例，資料筆數；422，欄位個數：5，欄位名稱：編號，案類，發生(現)日期，發生時段，發生(現)地點。
# 原始資料已經下架： https://data.gov.tw/datasets/history/73886
# GitHub 下載： https://github.com/rwepa/DataDemo/blob/master/%E8%87%BA%E5%8C%97%E5%B8%8210401-10806%E6%B1%BD%E8%BB%8A%E7%AB%8A%E7%9B%9C%E9%BB%9E%E4%BD%8D%E8%B3%87%E8%A8%8A.csv

# 步驟2: 下載地圖資料
# https://data.gov.tw/dataset/7441
# 本例考量分析台北市各區資料，因此下載「 鄉鎮市區界線(TWD97經緯度)」，下載檔案為「 mapdata202203151020.zip」，解壓縮為「C:\rdata\mapdata202203151020」資料夾

# 下載世界地圖
# http://www.diva-gis.org/gdata

# 步驟3: 匯入地圖資料至R
# 使用 rgdal 套件的 readOGR函數 以匯入地圖資料，使用 tmap 套件以製作主題式地圖

library(rgdal) # readOGR
# Loading required package: sp
# Please note that rgdal will be retired by the end of 2023,
# plan transition to sf/stars/terra functions using GDAL and PROJ
# at your earliest convenience.

library(tmap) # qtm

# 匯入地理資料
twn <- readOGR(dsn="C:/rdata/mapdata202203151020", layer="TOWN_MOI_1100415", encoding="UTF-8")

head(twn@data) # 中文正常
names(twn@data)

# 如果有中文亂碼,使用 iconv 函數進行轉換
twn@data$COUNTYNAME <- iconv(twn@data$COUNTYNAME, from = "UTF-8", to="UTF-8")
twn@data$TOWNNAME <- iconv(twn@data$TOWNNAME, from = "UTF-8", to="UTF-8")
head(twn@data) # 中文正常顯示

names(attributes(twn)) # 7個屬性
summary(twn) # 資料摘要
names(twn) # 7個欄位
class(twn) # SpatialPolygonsDataFrame
str(twn@data) # 368*7

# 篩選臺北市地理資料
twn.taipei <- twn[twn@data$COUNTYNAME == "臺北市",]
twn.taipei@data

str(twn.taipei@polygons[1])
str(twn.taipei@polygons[5])

# 步驟4: 匯入臺北市住宅竊盜點位資訊資料
theft <- read.table("C:/rdata/臺北市10401-10806汽車竊盜點位資訊.csv", header=TRUE, sep=",") # 422*5

# 將發生.現.日期由民國年轉為西元年
theft$發生.現.日期 <- as.Date(unlist(lapply(theft$發生.現.日期, function(x) {
  if (nchar(x) == 6) return(paste0(as.numeric(substr(x,1,2))+1911, "-", substr(x,3,4), "-", substr(x,5,6)))
  if (nchar(x) == 7) return(paste0(as.numeric(substr(x,1,3))+1911, "-", substr(x,4,5), "-", substr(x,6,7)))
})))

# 新增行政區欄位
theft$行政區 <- substr(theft$發生.現.地點,4,6)

# 篩選2018年&台北市資料
theft.2018 <- theft[theft$發生.現.日期 >= as.Date("2018-01-01") & substr(theft$發生.現.地點,1,3) == "台北市" ,] # 109*6

# 使用 aggregate 樞紐分析各行政區住宅竊盜次數小計
theaft.area <- aggregate(案類~行政區, data=theft.2018[c(2,6)], length)
names(theaft.area) <- c("行政區", "住宅竊盜發生數")
summary(theaft.area)

# 步驟5: 將臺北市住宅竊盜點位資訊資料整合至 twn.taipei@data
# merge函數中,sort參數須設定為FALSE,否則繪圖位置會有錯誤
twn.taipei@data <- merge(twn.taipei@data, theaft.area, by.x = "TOWNNAME", by.y = "行政區", sort=FALSE)
twn.taipei@data

# 步驟6: 臺北市住宅竊盜分佈圖

# method 1 採用 plot{graphics}
住宅竊盜發生數.color <- cut(twn.taipei@data$住宅竊盜發生數, 
                     breaks=c(0,10,15,20,30,Inf), 
                     labels=c("10以下", "11~15", "16~20", "21~30", "31以上"))

# 建立彩色調色盤(color palette)
# 內建調色盤 rainbow, heat.colors, terrain.colors, topo.colors, cm.colors, 本例以heat.colors為主
twn.taipei@data$Col <- heat.colors(5)[as.numeric(住宅竊盜發生數.color)]

plot(twn.taipei, col=twn.taipei@data$Col, main="2018年臺北市住宅竊盜分佈圖")
text(coordinates(twn.taipei)[,1], coordinates(twn.taipei)[,2], twn.taipei$TOWNNAME, cex=0.7)
legend("topright", legend=levels(住宅竊盜發生數.color), fill=twn.taipei@data$Col, col= heat.colors(5), title="住宅竊盜發生數")

# method 2 採用 qtm{tmap}
qtm(shp=twn.taipei, fill="住宅竊盜發生數", text="TOWNNAME", fill.title="住宅竊盜發生數", title="2018年臺北市住宅竊盜分佈圖")

qtm(shp=twn.taipei, fill="住宅竊盜發生數", text="TOWNNAME", fill.title="住宅竊盜發生數", title="2018年臺北市住宅竊盜分佈圖", fill.palette="Blues")

qtm(shp=twn.taipei, fill="住宅竊盜發生數", text="TOWNNAME", fill.title="住宅竊盜發生數", title="2018年臺北市住宅竊盜分佈圖", fill.palette="Greens")
# end
