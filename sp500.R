# sp500 data processing

# source: https://github.com/rwepa/DataDemo/blob/master/sp500.RData

library(zoo)

load("sp500.RData")

str(sp500) # data.frame, 16607*7

head(sp500)

tail(sp500)

# data processing

sp500 <- read.zoo(sp500, format = "%Y-%m-%d")

head(sp500)

tail(sp500)

str(sp500) # zoo

plot(sp500$close,
     main = "SP500 (1950-2015)",
     xlab="Year",
     ylab="Close")

grid()
