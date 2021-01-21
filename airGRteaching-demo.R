# title   : 水文建模shiny應用
# author  : Ming-Chang Lee
# email   : alan9956@gmail.com
# RWEPA   : http://rwepa.blogspot.tw/
# GitHub  : https://github.com/rwepa
# resource: https://rwepa.blogspot.com/2021/01/shiny-hydrological-modelling-with-shiny.html

# 安裝2個基本套件
# install.packages(c("airGR", "airGRteaching"))

# 使用remotes套件, 安裝最新版htmlwidgets套件
# install.packages("remotes")
# remotes::install_github("ramnathv/htmlwidgets")

library(airGRteaching)

# 載入L0123001資料集
data(L0123001, package = "airGR")

# 顯示物件清單
ls()
# [1] "BasinInfo" "BasinObs"

head(BasinObs)
# "DatesR": 年-月-日, POSIXct物件
# "P"  : average precipitation [mm/time step] 每日平均降雨量
# "T"  : catchment average air temperature [℃]  平均氣溫
# "E"  : catchment average potential evapotranspiration [mm/day] 平均潛在蒸發量
# "Qls": outlet discharge [l/s] 出水口排出量
# "Qmm": outlet discharge [mm/day] 出水口排出量

# 建立低地盆地資料
BV_L0123001 <- BasinObs[0001:6000, c("DatesR", "P", "E", "Qmm", "T")]

# 建立多山盆地資料
BV_L0123002 <- BasinObs[5000:9999, c("DatesR", "P", "E", "Qmm", "T")]
BI_L0123002 <- BasinInfo

# 建立互動式網頁資料分析
ShinyGR(ObsDF = list("Low-land basin" = BV_L0123001, "Mountainous basin" = BV_L0123002),
        ZInputs = list(NULL, median(BI_L0123002$HypsoData)),
        HypsoData = list(NULL, BI_L0123002$HypsoData),
        NLayers = list(5, 5),
        SimPer = list(c("1994-01-01", "1998-12-31"), c("2004-01-01", "2006-12-31")),
        theme = "United")
