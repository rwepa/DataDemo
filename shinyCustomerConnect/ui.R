# title    : shiny - Customer Connect
# date     : 2016.10.23
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# Encoding : UTF-8

library(shiny)
library(leaflet)

fluidPage(

  # Application title
  titlePanel("RWEPA - shiny 顧客連接分析, alan9956@gmail.com, 網站: http://rwepa.blogspot.com/"),

  # Sidebar with a slider input for the number of distance
  sidebarLayout(
    sidebarPanel(
      
      numericInput("focusLng", label="查詢經度(Lng): ", value=121.517080),
      
      numericInput("focusLat", label="查詢緯度(Lat): ", value=25.047923),
      
      sliderInput("dists",
                  "連接距離(m)",
                  min = 1,
                  max = 10000,
                  value = 1000)
    ),

    # Show a plot of the generated distribution
    mainPanel(
      leafletOutput("distPlot",  width="100%", height=600)
    )
  )
)
