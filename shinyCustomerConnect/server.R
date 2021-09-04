# title    : shiny - Customer Connect
# date     : 2016.10.23
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# Encoding : UTF-8

library(shiny)
library(geosphere) # distm- great circle
library(leaflet) # map

# x longitude
# y latitude
# https://rwepa.shinyapps.io/shinyCustomerConnect/

load('customer.RData')
function(input, output) {

  output$distPlot <- renderLeaflet({    
    
    setradius <- input$dists 
    setlng <- input$focusLng 
    setlat <- input$focusLat 
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
      addCircleMarkers(data = customerSelect, 
                       lng = ~ lon, 
                       lat = ~ lat, 
                       popup = ~ StoreName,
                       col="red")
    m1

  })

}
