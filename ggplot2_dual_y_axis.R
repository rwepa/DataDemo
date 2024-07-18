# file     : ggplot2_dual_y_axis.R
# title    : Dual Y axis with ggplot2
# author   : Ming-Chang Lee
# date     : 2017.09.09
# updated  : 2024.5.27
# YouTube  : https://www.youtube.com/@alan9956
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Email    : alan9956@gmail.com

# 2024.5.27 - 更新ggplot2 - dual y axis標題等語法

# 載入套件
library(XML)
library(ggplot2)

# 下載套件清單
urls <- "http://cran.csie.ntu.edu.tw/web/packages/available_packages_by_date.html"
mydf <- readHTMLTable(urls, stringsAsFactors = FALSE)
str(mydf) # list

# 取出list的第1個資料框物件
mydf <- mydf[[1]]

# 刪除欄位名稱中的前後空白字元
names(mydf) <- trimws(names(mydf))

# 將Date欄位轉換為日期字元
mydf$Date <- as.Date(mydf$Date)

# 計算每年為群組的套件個數
mydf <- data.frame(table(format(mydf$Date, "%Y")), stringsAsFactors=FALSE)

# 新增每年為群組的累計套件個數
mydf$AccumulatedPackages <- cumsum(mydf$Freq)

# 更改欄位名稱
names(mydf)[1:2] <- c("Year", "Packages")

# 檢視資料集
mydf

ggplot(mydf, aes(x = Year)) +
  # 建立"Packages per year"長條圖, 另可使用 geom_bar {ggplot2} 繪製.
  geom_col(aes(y = Packages*2), fill="grey") + 
  
  # 繪製累計套件數線圖
  geom_line(aes(y = AccumulatedPackages, group = 1), linetype = 2, color = "blue") +
  
  # 繪製累計套件數點圖
  geom_point(aes(y = AccumulatedPackages, group = 1), color = "blue") +
  
  # 標記累計套件數文字
  geom_text(aes(y = AccumulatedPackages, label = AccumulatedPackages), 
            vjust = -0.3, size = 3.5, color = "blue") +
  
  # 設定主要標題與左右置中
  ggtitle("CRAN Packages Chart - Powered by RWEPA[https://rwepa.blogspot.com/]") + 
  theme(plot.title = element_text(hjust = 0.5)) + 
  
  # 設定X軸標題, Y軸標題
  xlab(paste0("Year(2008.01 ~ ", format(Sys.Date(), "%Y.%m"), ")")) +
  ylab("Accumulated packages") +
  
  # 設定第2Y軸刻度為主Y軸刻度的一半
  scale_y_continuous(sec.axis = sec_axis(name = "Packages per year", trans = ~./2)) +
  
  # 設定X軸刻度標題位置旋轉45度與Y軸標題,第2Y軸標題顏色
  theme(axis.text.x = element_text(face="bold", angle=45),
        axis.title.y = element_text(colour = "blue"),
        axis.title.y.right = element_text(color = "black"))
# 警告訊息：
# The `trans` argument of `sec_axis()` is deprecated as of ggplot2 3.5.0.
# ℹ Please use the `transform` argument instead.
# This warning is displayed once every 8 hours.
# Call `lifecycle::last_lifecycle_warnings()` to see where this warning was generated. 
# end
