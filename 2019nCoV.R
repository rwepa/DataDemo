# title: 2019新型冠狀病毒視覺化
# date: 2020.2.13
# author: Ming-Chang Lee
# email: alan9956@gmail.com
# RWEPA: http://rwepa.blogspot.tw/
# GitHub: https://github.com/rwepa

# data: https://github.com/CSSEGISandData/2019-nCoV

library(leaflet)
library(htmltools) # tag

# 確診 Confirmed
ncovConfirmedUrl <- "https://raw.githubusercontent.com/CSSEGISandData/2019-nCoV/master/time_series/time_series_2019-ncov-Confirmed.csv"

ncovConfirmed <- read.table(ncovConfirmedUrl, header=TRUE, sep=",")

names(ncovConfirmed) <- gsub("X", "", names(ncovConfirmed))

mydf <- as.data.frame(matrix(unlist(strsplit(names(ncovConfirmed)[-c(1:4)], "\\.")), ncol=5, byrow=TRUE))

myname <- c()
for (i in 1:nrow(mydf)) {
  myname <- c(myname, paste0(paste0("20", mydf[i, 3]), "-", mydf[i, 1], "-", mydf[i, 2], " ", mydf[i, 4], ":", mydf[i, 5]))
}

rm(mydf)

names(ncovConfirmed)[-c(1:4)] <- myname

head(ncovConfirmed)

ncovConfirmedAgg <- aggregate(`2020-2-10 19:30` ~ Country.Region, 
  data=ncovConfirmed, 
  sum)

ncovConfirmedAgg <- aggregate(get(names(ncovConfirmed)[ncol(ncovConfirmed)]) ~ Country.Region, 
  data=ncovConfirmed, 
  sum)

names(ncovConfirmedAgg) <- c("CountryRegion", "Confirmed")

ncovConfirmedAgg <- ncovConfirmedAgg[order(ncovConfirmedAgg$Confirmed, decreasing=TRUE),]

(ncovTotalConfirmed <- sum(ncovConfirmedAgg$Confirmed))

# 死亡 Death
ncovDeath <- "https://raw.githubusercontent.com/CSSEGISandData/2019-nCoV/master/time_series/time_series_2019-ncov-Deaths.csv"

ncovDeath <- read.table(ncovDeath, header=TRUE, sep=",")

names(ncovDeath) <- gsub("X", "", names(ncovDeath))

mydf <- as.data.frame(matrix(unlist(strsplit(names(ncovDeath)[-c(1:4)], "\\.")), ncol=5, byrow=TRUE))

myname <- c()
for (i in 1:nrow(mydf)) {
  myname <- c(myname, paste0(paste0("20", mydf[i, 3]), "-", mydf[i, 1], "-", mydf[i, 2], " ", mydf[i, 4], ":", mydf[i, 5]))
}

rm(mydf)

names(ncovDeath)[-c(1:4)] <- myname

head(ncovDeath)

ncovDeathAgg <- aggregate(`2020-2-10 19:30` ~ Country.Region, data=ncovDeath, sum)

ncovDeathAgg <- aggregate(get(names(ncovDeath)[ncol(ncovDeath)]) ~ Country.Region, 
  data=ncovDeath, 
  sum)

names(ncovDeathAgg) <- c("CountryRegion", "Death")

ncovDeathAgg <- ncovDeathAgg[order(ncovDeathAgg$Death, decreasing=TRUE),]

(ncovTotalDeath <- sum(ncovDeathAgg$Death))

# 建立leaflet互動式地圖

title <- tags$h2("2019新型冠狀病毒感染人數全球分佈圖")

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
      ";", ncovConfirmed[,ncol(ncovConfirmed)])) %>%
  addControl(title, position="topright") %>%
  addControl(datasource, position="bottomleft") %>%
  addControl(publish, position="bottomright")


m  # Print the map
# end
