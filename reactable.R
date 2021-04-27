# date     : 2021.04.27
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# Encoding : UTF-8

# 範例1
library(reactable)

reactable(CO2)

# 範例2
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
# end
