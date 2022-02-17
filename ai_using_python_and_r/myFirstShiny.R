# title   : myFirstShiny
# date    : 2022.02.18
# author  : Ming-Chang Lee
# email   : alan9956@gmail.com
# RWEPA   : http://rwepa.blogspot.tw/
# Encoding: UTF-8

library(shiny)

# Define UI for dataset viewer app ----
ui <- fluidPage(
    
    # App title ----
    titlePanel("myFirstShiny-2022.2.18"),
    
    # Sidebar layout with a input and output definitions ----
    sidebarLayout(
        
        # Sidebar panel for inputs ----
        sidebarPanel(
            
            # Input: Selector for choosing dataset ----
            selectInput(inputId = "dataset",
                        label = "Choose a dataset:",
                        choices = c("rock", "pressure", "cars")),
            
            # Input: Numeric entry for number of obs to view ----
            numericInput(inputId = "obs",
                         label = "Number of observations to view:",
                         value = 10),
            
            sliderInput(inputId = "bins",
                        label = "Number of bins:",
                        min = 1,
                        max = 50,
                        value = 30)
        ),
        
        # Main panel for displaying outputs ----
        mainPanel(
            
            # Output: Verbatim text for data summary ----
            verbatimTextOutput("summary"),
            
            # Output: HTML table with requested number of observations ----
            tableOutput("view"),
            
            plotOutput(outputId = "distPlot")
            
        )
    )
)

# Define server logic to summarize and view selected dataset ----
server <- function(input, output) {
    
    # Return the requested dataset ----
    datasetInput <- reactive({
        switch(input$dataset,
               "rock" = rock,
               "pressure" = pressure,
               "cars" = cars)
    })
    
    # Generate a summary of the dataset ----
    output$summary <- renderPrint({
        dataset <- datasetInput()
        summary(dataset)
    })
    
    # Show the first "n" observations ----
    output$view <- renderTable({
        head(datasetInput(), n = input$obs)
    })
    
    output$distPlot <- renderPlot({
        
        df <- datasetInput()
        x <- df[,1]
        bins <- seq(min(x), max(x), length.out = input$bins + 1)
        
        hist(x, breaks = bins, col = "#75AADB", border = "white",
             xlab = "Waiting time to next eruption (in mins)",
             main = input$dataset)
        
    })
    
}

# Create Shiny app ----
shinyApp(ui = ui, server = server)
# end
