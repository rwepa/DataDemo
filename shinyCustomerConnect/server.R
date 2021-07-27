# title    : shiny - Customer Connect
# date     : 2016.10.23
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# Encoding : UTF-8

library(shiny)
library(geosphere) # distm 計算大圓距離
library(leaflet) # map

# x軸: 經度 longitude
# y軸: 緯度 latitude

customer <- read.csv("data/711_門市清單_台北市_lonlat.csv", header=TRUE, stringsAsFactors=FALSE) # 275*8

function(input, output) {

  output$distPlot <- renderLeaflet({    
    
    # 松山火車站 25.049398, 121.578248
    # 台北火車站 25.047923, 121.517080
    # distm(c(121.578248, 25.049398), c(121.517080, 25.047923), fun = distHaversine) # 公尺
    
    setradius <- input$dists # 半徑
    setlng <- input$focusLng # 經度
    setlat <- input$focusLat # 緯度
    # setradius <- 1000
    # setlng <- 121.517080
    # setlat <- 25.047923
    
    distselect <- c()
    for (i in 1:nrow(customer)) {
      distselect[i] <- distm(c(setlng, setlat), c(customer$lon[i], customer$lat[i]))
      }
    
    customer$distm <- distselect
    
    customerSelect <- customer[customer$distm <= setradius, ]
    
    m1 <- leaflet(customer) %>%
      addTiles() %>%
      setView(lng = setlng, lat = setlat, zoom=14) %>%
            addCircles(lng = setlng, lat = setlat, weight = 1,
                 radius = setradius, popup = paste0(setradius,"m")) %>%
      addCircleMarkers(data=customerSelect, lng= ~lon, lat= ~lat, popup=~店名, col="red")
    m1

  })

}
