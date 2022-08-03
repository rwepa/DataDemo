# File     : shiny_ggplot2_app.R
# Author   : Ming-Chang Lee (2022)
# Email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

library(shiny)
library(ggplot2)
options(shiny.usecairo = TRUE)

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("Old Faithful Geyser Data - shiny with ggplot2"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            sliderInput("bins",
                        "Number of bins:",
                        min = 1,
                        max = 50,
                        value = 30)
        ),

        # Show a plot of the generated distribution
        mainPanel(
           plotOutput("distPlot")
        )
    )
)

# Define server logic required to draw a histogram

server <- function(input, output) {

    output$distPlot <- renderPlot({
      
        # generate bins based on input$bins from ui.R
        x    <- faithful[2]
        bins <- seq(min(x), max(x), length.out = input$bins + 1)
        ggplot(x, aes(x=waiting)) + 
          geom_histogram(bins=input$bins, fill="lightblue", color="gray")
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
# end
