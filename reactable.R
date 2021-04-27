# title    : reactable package
# date     : 2021.04.27
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# Encoding : UTF-8

# 範例1 - 表格應用
library(reactable)

reactable(CO2)

# 範例2 - shiny 加上表格應用
library(shiny)

library(reactable)

ui <- fluidPage(
  titlePanel("reactable package example"),
  reactableOutput("table")
)

server <- function(input, output, session) {
  output$table <- renderReactable({
    reactable(CO2)
  })
}

shinyApp(ui, server)

# 範例3 - 表格加上折線圖 sparkline

library(dplyr)
library(sparkline)
library(reactable)

mydata <- iris %>%
  group_by(Species) %>%
  summarise(width = list(Petal.Width)) %>%
  mutate(boxplot = NA, sparkline = NA)

reactable(mydata, columns = list(
  width = colDef(cell = function(values) {
    sparkline(values, type = "bar", chartRangeMin = 0, chartRangeMax = max(iris$Petal.Width))
  }),
  boxplot = colDef(cell = function(value, index) {
    sparkline(mydata$width[[index]], type = "box")
  }),
  sparkline = colDef(cell = function(value, index) {
    sparkline(mydata$width[[index]])
  })
))
# end
