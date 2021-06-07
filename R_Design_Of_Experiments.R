# title    : R - Design Of Experiments (DOE)
# date     : 2021.06.07
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

# 大綱 -----
# 1.實驗設計簡介
# 2.R, RStudio簡介
# 3.一因子實驗-變異數分析
# 4.隨機化完全區集設計
# 5.因子設計
# 6.2^3因子設計
# 7.反應曲面法

# 1. 實驗設計簡介 -----

# 實驗設計的三個基本原理
# a.隨機化(Randomization)
# b.重複化(Replication)
# c.區集化(Blocking)

# 2. R, RStudio簡介 -----

# 步驟一: R下載
# 步驟二: RStudio下載

# R 基礎篇 - 國立台北商業技術學院上課教材(238頁, 2011.7.4)
# http://rwepa.blogspot.com/2013/01/r-201174.html

# R入門資料分析與視覺化應用
# https://courses.mastertalks.tw/courses/R-teacher

# R商業預測與應用
# https://courses.mastertalks.tw/courses/R-2-teacher

# 3. 一因子實驗-變異數分析 -----

# 晶圓蝕刻製程
# 水準 𝑎=4 {160,180,200,220W}
# 重複 𝑛=5
# 只考慮RF功率，因此是一因子實驗
# 全部實驗次數20

# 步驟1.進行隨機化實驗
rf <- c("160", "180", "200", "220")

rfPower <- gl(4, 5, label=rf)
rfPower

# 隨機化
set.seed(168)
ind <- sample(4*5, 20)
rfPowerRandom <- rfPower[ind]
head(rfPowerRandom)
# [1] 200 220 220 200 160 180
# Levels: 160 180 200 220
# 第1筆試驗為200W,第2筆為220W

# 步驟2.實驗結果
EtchRate <- c(575, 542, 530, 539, 570,
              565, 593, 590, 579, 610,
              600, 651, 610, 637, 629,
              725, 700, 715, 685, 710)

plasmaEtch <- data.frame(rfPower = as.factor(rfPower), EtchRate)
plasmaEtch

# 步驟3.ANOVA分析

y_dot_dot <- mean(plasmaEtch$EtchRate) # 617.75

sum(plasmaEtch$EtchRate - y_dot_dot)^2 # ERROR
SST <- sum((plasmaEtch$EtchRate - y_dot_dot)^2) # 72209.75

y_i_dot <- aggregate(EtchRate ~ rfPower, data = plasmaEtch, FUN = mean)
y_i_dot
SSTreatment <- 5*sum((y_i_dot$EtchRate - y_dot_dot)^2)
SSTreatment # 66870.55

SSE <- SST - SSTreatment # 5339.2
SSE

MSTreatment <- 66870.55/3 # 22290.18
MSE <- 5339.2/16 # 333.7

F0 <- MSTreatment/MSE # 66.8

# a.using critical values
F_critical <- qf(p = 0.95, df1 = 3, df2 = 16) # 3.238872

ifelse(F0 >= F_critical, "Reject Ho", "Accept H0") # "Reject Ho"

# b.using pvalue
pvalue <- pf(q = F0, df1 = 3, df2 = 16, lower.tail = FALSE) # 2.882866e-09, p值很小

ifelse(pvalue < 0.05, "Reject Ho", "Accept H0") # "Reject Ho"

# ANOVA分析-aov
plasmaEtchANOVA <- aov(EtchRate ~ rfPower, data=plasmaEtch)

# 模型結果
plasmaEtchANOVA
summary(plasmaEtchANOVA)

# 4. 隨機化完全區集設計 -----

# 步驟1. 將資料輸入Excel
# 路徑 C:/rdata/R-rcbd.xlsx

# 步驟2. 使用 readxl 套件匯入Excel
library(readxl) # read_excel
library(dplyr) # v.1.0.6 mutate


artificialVein <- read_excel("C:/rdata/R-rcbd.xlsx")
artificialVein

# 步驟3.將前2欄轉換為factor – mutate {dplyr}
artificialVein <- artificialVein %>%
  mutate(across(c(extrusionPressure, batch),
                factor))
artificialVein

# 步驟4.建立 RCDB模型
artificialVeinRCBD <- aov(yield ~ extrusionPressure + batch, data=artificialVein)

artificialVeinRCBD

summary(artificialVeinRCBD)

# 5. 因子設計 -----

# 步驟1. 將資料輸入Excel
# 路徑 C:/rdata/R-fd.xlsx

# 步驟2. 使用 readxl 套件匯入Excel
library(readxl) # read_excel
library(dplyr) # v.1.0.6 mutate

batteryLife <- read_excel("C:/rdata/R-fd.xlsx")
batteryLife

# 步驟3.將前3欄轉換為factor – mutate {dplyr}
batteryLife <- batteryLife %>%
  mutate(across(c(material:replication),
                factor))
batteryLife

# 步驟4.建立 二因子模型
batteryLifeFD <- aov(life ~ material*temperature, data=batteryLife)

batteryLifeFD

summary(batteryLifeFD)

# 反應圖
interaction.plot(x.factor     = batteryLife$temperature,
                 trace.factor = batteryLife$material,
                 response     = batteryLife$life,
                 fun = mean,
                 type = "b",
                 col = c("black","red","blue"),
                 pch = c(19, 17, 15),
                 fixed = TRUE,
                 legend = FALSE,
                 cex=2,
                 xlab = "溫度(℉)",
                 ylab = "平均壽命(小時)",
                 main = "電池壽命二因子實驗反應圖")

legend("topright", 
       legend = c("材料1", "材料2", "材料3"),
       pch = c(19, 17, 15), lty = c(2, 2, 1),
       col = c("black","red","blue"), 
       text.col = c("black","red","blue"))

grid()

# 6.2^3因子設計 -----

pf(q=53.15, df1 = 1, df2 = 8, lower.tail = FALSE)

pf(q=19.13, df1 = 1, df2 = 8, lower.tail = FALSE)

pf(q=2.13, df1 = 1, df2 = 8, lower.tail = FALSE)

# 7.反應曲面法 -----

# 步驟1.載入套件
library(rsm)

# 步驟2.載入資料集
ChemReact

ChemReact1 # Time: 85±5, Temp: 175±5
ChemReact2

# 步驟3.編碼變數(coded variable)
# (variable - center)/(half of width)
# Time: 中心點=80, 寬度的一半=5
# Temp: 中心點=175, 寬度的一半=5

CR1 <- coded.data(ChemReact1, x1 ~ (Time - 85)/5, x2 ~ (Temp - 175)/5)
CR1

# 編碼變數轉換為data.frame
as.data.frame(CR1)

# 步驟4.建立反應曲面設計
# ccd: central-composite designs(CCD, 中心組合設計)
# 中心組合設計包括:(1) 2^k要因實驗:2^k個,主軸實驗:2k個,中心點實驗:n_center
# bbd: Box-Behnken design (for 3 to 7 factors)

# bbd(k, n0, coding)
# k: 變數個數
# n0: 每個區集的中心點個數
# coding: 編碼公式

# 建立5個變數A,B,C,D,E-CCD模型
des1 <- ccd(y1 + y2 ~ A + B + C + D, generators = E ~ - A * B * C * D, n0 = c(6, 1))
des1

# 建立3個變數x1,x2,x3-BBD模型
des2 <- bbd(3, n0 = 2, coding = list(x1 ~ (Force - 20)/3, x2 ~ (Rate - 50)/10, x3 ~ Polish - 4))
des2

# 步驟5.建立反應曲面模型

# FO  - first-order
# TWI - two-way interaction
# PQ  - pure quadratic
# SO  - second-order

CR1.rsm <- rsm(Yield ~ FO(x1, x2), data = CR1)
summary(CR1.rsm) # Lack of fit: p值~0.01034 不顯著

# 步驟6.優化反應曲面模型, 加入 two-way interactions

CR1.rsmi <- update(CR1.rsm, . ~ . + TWI(x1, x2))
summary(CR1.rsmi) # # Lack of fit: p值~0.005221, 已經減小.
# end