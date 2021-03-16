# title    : taiwan_birth.R
# date     : 2021.03.16
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# Encoding : UTF-8

library(readxl)    # read_excel
library(crosstalk) # SharedData
library(leaflet)   # leaflet
library(DT)        # datatable
library(htmltools) # tags

# 匯入資料
# https://github.com/rwepa/DataDemo/blob/master/taiwan_birth.xlsx
birth <- read_excel("taiwan_birth.xlsx")

# 將資料轉換為 SharedData 物件
df <- SharedData$new(birth[c("city", "annua_crude_birth_rate", "longitude", "latitude")])

# 建立標題標題
rr <- tags$div(
  HTML('<a href="http://rwepa.blogspot.com/">110年2月粗出生率%</a>')
)

# 建立2行互相聯動效果
bscols(widths = c(5, 7),
  leaflet(df, height=700) %>% 
    addTiles() %>% 
    addMarkers(popup = ~city) %>% 
    setView(lng = 120.9876, lat = 23.8387, zoom = 7) %>%
    addControl(rr, position = "topright"),
  datatable(df,
            rownames = FALSE,
            colnames = c("地區","110年2月台灣粗出生率%", "經度", "緯度"),
            options = list(pageLength = 10,
                           searching = FALSE),
            height=700)
)
# end
