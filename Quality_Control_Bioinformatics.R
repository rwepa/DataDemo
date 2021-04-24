# title    : Quality Control in Bioinformatics
# Place    : 中華民國品質學會(Chinese Society for Quality, CSQ)
# file     : Quality_Control_Bioinformatics.R
# date     : 2021.04.26
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

# 大綱 -----
# 1.R語言與RStudio軟體簡介
# 2.Bioconductor實務應用
# 3.品質控制技術
# 4.結論與未來展望

# 1.R語言與RStudio軟體簡介 -----

# 下載R,RStudio -----
# http://rwepa.blogspot.com/

plot(runif(100), type="l", main= "R大數據分析")

demo(graphics)

demo(persp)
# 工作目錄 Working Directory -----

# 取得工作目錄
getwd()

# 設定工作目錄
# 先建立 C:/rdata 資料夾
setwd("C:/rdata")

getwd()

# qcc package -----
# https://cran.r-project.org/web/packages/qcc/index.html

library(qcc) -----
  
  # qcc - xbar chart
  data(pistonrings)
diameter <- with(pistonrings, qcc.groups(diameter, sample))
head(diameter)
qcc(diameter[1:25,], type="xbar", newdata=diameter[26:40,])

# pareto.chart - Pareto chart (柏拉圖) -----
defect <- c(80, 27, 66, 94, 33)
names(defect) <- c("price code", "schedule date", "supplier code", "contact num.", "part num.")
pareto.chart(defect, ylab = "Error frequency", xlab = "Error causes", las=1)
pareto.chart(defect, ylab = "Error frequency", col=rainbow(length(defect)))

# cause.and.effect - Cause and effect diagram (要因分析圖) -----
cause.and.effect(
  cause=list(
    Measurements=c("Micrometers", "Microscopes", "Inspectors"), 
    Materials=c("Alloys", "Lubricants", "Suppliers"), 
    Personnel=c("Shofts", "Supervisors", "Training", "Operators"), 
    Environment=c("Condensation", "Moisture"), 
    Methods=c("Brake", "Engager", "Angle"), 
    Machines=c("Speed", "Lathes", "Bits", "Sockets"))
  , effect="Surface Flaws"
  , titl="Cause-and-Effect Diagram"
  , cex = c(1, 0.9, 1)
  , font=c(1,3,2))

# process.capability - process capability index (製程能力 Cp) -----
data(pistonrings)
attach(pistonrings)
diameter <- qcc.groups(diameter, sample)
q <- qcc(diameter[1:25,], type="xbar", nsigmas=3, plot=FALSE)

process.capability(q, spec.limits=c(73.95,74.05))
process.capability(q, spec.limits=c(73.95,74.05), target=74.02)

# 2.Bioconductor實務應用 -----

# https://www.bioconductor.org/

# 安裝 Bioconductor 基礎套件 -----
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install(version = "3.12")

# Common work flows -----
# http://www.bioconductor.org/packages/release/BiocViews.html#___Workflow

# rnaseqGene 套件 -----
# https://bioconductor.org/packages/release/workflows/html/rnaseqGene.html

BiocManager::install("rnaseqGene")

# 線上說明 -----
browseVignettes("rnaseqGene")

# 3.品質控制技術 -----

# BiocManager::install("ALLMLL")

library("affy")
library("ALLMLL")

data(MLL.B)
MLL.B
?AffyBatch 

# 全部20arrays,取出8個arrays
Data <- MLL.B[, c(2, 1, 3:5, 14, 6, 13)]
sampleNames(Data) <- letters[1:8]
Data

# plot of the log intensities
palette.gray <- c(rep(gray(0:10/10), times = seq(1, 41, by = 4)))

image(Data[, 1], transfo = function(x) x, col = palette.gray)
image(Data[, 1], col = palette.gray)

# Multi-array approaches

library("RColorBrewer")
cols <- brewer.pal(8, "Set1")

# 盒鬚圖 -----
# array f 明顯與其他不相同
boxplot(Data, col = cols, main = "MLL.B 8個群組盒鬚圖")

# 直方圖 -----
# array a 有2個高峰, 即雙峰分配 (bimodal distribution)
hist(Data, col = cols, 
     lty = c(2, rep(1,7)),
     lwd=3,
     xlab = "Log (base 2) intensities",
     main = "MLL.B 8個群組直方圖")
legend("topright", letters[1:8], col = cols, lwd=3, lty = c(2, rep(1,7)))

# qcmetrics套件 -----
# https://www.bioconductor.org/packages/release/bioc/html/qcmetrics.html

# BiocManager::install("qcmetrics")

library("qcmetrics")

# 建立 QcMetric 物件 -----
qc <- QcMetric(name = "A test metric")
class(qc)
qc

# qcdata: 實際儲存資料
qcdata(qc, "x") <- rnorm(100)
qcdata(qc) ## all available qcdata

qc
show(qc)
summary(qcdata(qc, "x"))

# status: 狀態屬性 {TRUE, FALSE}
status(qc) <- TRUE
qc

# 函數 boxplot -----

# 預設繪圖有錯誤
plot(qc)

# 新增繪圖方法
plot(qc) <- function(object, ... ) boxplot(qcdata(object, "x"), ...)

# 繪製盒鬚圖
plot(qc, main = "qcmetrics繪圖")

qcm <- QcMetrics(qcdata = list(qc))
qcm

# Metadata 元資料 -----
metadata(qcm) <- list(author = "李明昌(ALAN LEE)",
                      lab = "Big array lab")
qcm

mdata(qcm)

# 更新元資料
metadata(qcm) <- list(author = "李明昌(ALAN LEE)",
                      lab = "Big array lab",
                      organization = "中華民國品質學會")
mdata(qcm)

# 函數 yaqc – 計算 YAQC統計 -----

# MAQCsubsetAFX套件內建資料集 refA
# BiocManager::install("MAQCsubsetAFX")

library("MAQCsubsetAFX")
data(refA)
refA

library("affy")

# 計算 RNA degradation

# Austin Bowles, RNA Degradation and NUSE Plots, 2011
# https://math.usu.edu/~jrstevens/stat5570/Bowles.pdf
# RNA達到使用壽命後（即已參與蛋白質合成），就會被細胞酶“降解”。
# 某些陣列可能是使用具有“壞” RNA的樣品製備的，已降解的RNA已無法提供有用的信息。

# Chapter 3, Bioinformatics and Computational Biology Solutions Using R and Bioconductor, 2005.

https://math.usu.edu/~jrstevens/stat5570/Bowles.pdf
deg <- AffyRNAdeg(refA)
deg

# BiocManager::install("yaqcaffy")
library("yaqcaffy")

# 計算 YAQCStats
yqc <- yaqc(refA)
show(yqc)

plot(yqc)

qc1 <- QcMetric(name = "Affy RNA degradation slopes")
qcdata(qc1, "deg") <- deg

# AffyRNAdeg {affy} - deg 繪圖
plot(qc1) <- function(object, ...) {
  x <- qcdata(object, "deg")
  nms <- x$sample.names
  plotAffyRNAdeg(x, col = 1:length(nms), ...)
  legend("topleft", nms, lty = 1, cex = 0.8,
         col = 1:length(nms), bty = "n")
}
status(qc1) <- TRUE

qc2 <- QcMetric(name = "Affy RNA degradation ratios")
qcdata(qc2, "yqc") <- yqc
plot(qc2) <- function(object, ...) {
  par(mfrow = c(1, 2))
  yaqcaffy:::.plotQCRatios(qcdata(object, "yqc"), "all", ...)
}
status(qc2) <- FALSE
qc2

maqcm <- QcMetrics(qcdata = list(qc1, qc2))
maqcm

# qcReport 建立報表 -----
qcReport(maqcm, 
         reportname = "RNA-deg", 
         type = "html",
         author = "Ming-Chang Lee")

# 4.結論與未來展望 -----

# Recap -----

# 1.R, RStudio 簡介 - qcc 套件
# 2.Bioconductor 實務應用 - rnaseqGene 套件
# 3.品質控制技術 - qcmetrics 套件
# 4.生物資訊研究方向
# Tallulah S. Andrews, Vladimir Yu Kiselev, Davis McCarthy & Martin Hemberg , Tutorial: guidelines for the computational analysis of single-cell RNA sequencing data, Nature Protocols volume 16, pages 1–9 (2021)
# https://www.nature.com/articles/s41596-020-00409-w

# 參考資料 -----

# Sorin Drăghici (2012), Statistics and Data Analysis for Microarrays: Using R and Bioconductor, Second Edition, CRC Press, 2012.

# Gatto L (2020), qcmetrics: A Framework for Quality Control. R package version 1.28.0, https://github.com/lgatto/qcmetrics.

# Robert Gentleman, Vince Carey, Wolfgang Huber, Rafael Irizarry, Sandrine Dudoit, Bioinformatics and Computational Biology Solutions Using R and Bioconductor, Springer, 2005.

# R教學-基礎篇(免費)
# http://rwepa.blogspot.tw/2013/01/r-201174.html

# R入門資料分析與視覺化應用教學(付費)
# https://courses.mastertalks.tw/courses/R-teacher

# R商業預測與應用(付費)
# https://courses.mastertalks.tw/courses/R-2-teacher
