# file     : ggplot2_dual_y_axis.R
# author   : Ming-Chang Lee
# date     : 2017.09.09
# YouTube  : https://www.youtube.com/@alan9956
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Email    : alan9956@gmail.com

library(XML)
library(ggplot2)
urls <- "http://cran.csie.ntu.edu.tw/web/packages/available_packages_by_date.html"
mydf <- readHTMLTable(urls, stringsAsFactors = FALSE)
str(mydf)
mydf <- mydf[[1]]
names(mydf) <- trimws(names(mydf))
mydf$Date <- as.Date(mydf$Date)
mydf <- data.frame(table(format(mydf$Date, "%Y")), stringsAsFactors=FALSE)
mydf$AccumulatedPAckages <- cumsum(mydf$Freq)
names(mydf)[1:2] <- c("Year", "Packages")
mydf
ggplot(mydf, aes(x = Year)) +
  geom_col(aes(y = Packages*2), fill="grey") + 
  theme(plot.title = element_text(hjust = 0.5)) + 
  # xlab("年") + 
  xlab(paste0("年 (2005-01 ~ ", format(Sys.Date(), "%Y-%m"), ")")) +
  ylab("累計套件數") +
  ggtitle("CRAN-套件統計圖 - by RWEPA") + 
  scale_y_continuous(sec.axis = sec_axis(trans = ~. /2)) + 
  theme(axis.title.y = element_text(colour = "blue")) + 
  annotate("text", x=13, y=5500, label= "套件數(年)", angle = -90) + 
  geom_line(aes(y = AccumulatedPAckages, group = 1), linetype = 2, color = "blue") +
  theme(axis.text.x = element_text(face="bold", angle=45),
        axis.text.y = element_text(face="bold", color="black", size=10)) +
  geom_point(aes(y = AccumulatedPAckages, group = 1), color = "blue") +
  geom_text(aes(y = AccumulatedPAckages, label = AccumulatedPAckages), 
            vjust = -0.3, size = 4, color = "blue")
# end
