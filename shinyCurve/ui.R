# file     : plot function with shiny package-ui.R
# author   : Ming-Chang Lee
# date     : 2013.1.2
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

library(shiny)
shinyUI(pageWithSidebar(
  headerPanel("RWEPA - shiny app - curve, PoweredBy: alan9956@gmail.com, 網站: http://rwepa.blogspot.com/"),  
  sidebarPanel(
    textInput("plot.function", "Function:" , "x^3-6*x^2+9*x+10"), 
    textInput("xlimit.lower", "x 座標 下限:", -5), 
    textInput("xlimit.upper", "x 座標 上限:", 5)
    # submitButton("Go Plot!")
    ),
  mainPanel(
      plotOutput("distPlot")    
  )
))