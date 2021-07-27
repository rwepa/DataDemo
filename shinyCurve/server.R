# file     : plot function with shiny package-server.R
# author   : Ming-Chang Lee
# date     : 2013.1.2
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

library(shiny)
shinyServer(function(input, output) {
  output$plot.function <- reactiveText(function() {
    input$plot.function
  })
  output$xlimit.lower <- reactiveText(function() {
    input$xlimit.lower
    })
  output$xlimit.upper <- reactiveText(function() {
    input$xlimit.upper
    })
  output$distPlot <- reactivePlot(function() {
    do.call("curve",list(expr=parse(text=input$plot.function),
                         from=input$xlimit.lower,
                         to=input$xlimit.upper))
  })
})