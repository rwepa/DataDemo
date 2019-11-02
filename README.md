# 資料集與使用範例
本項目提供資料集與範例分享, 資料集來自於 Open data或模擬資料.

# Part 1 資料 Data

### chorddiag.zip

資料說明: chorddiag Windows 版本套件壓縮檔

版本資訊: 0.1.2

資料來源: https://github.com/mattflor/chorddiag

### credit.csv

資料說明: Statlog (German Credit Data) Data Set

資料來源: https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)

資料筆數: 1000

欄位個數: 21

### gfc.csv

資料說明: 提供工廠訂單資料

資料來源: 模擬資料

資料筆數: 293

欄位個數: 3

欄位名稱: orderdate, supplier, amount

### hourly_44201_2018.zip

資料說明: 美國國家環境保護局 (United States Environmental Protection Agency) 2018年每小時臭氣資料

資料下載: https://aqs.epa.gov/aqsweb/airdata/download_files.html --> Tables of Hourly Data, Ozone (44201), 2018.

下載檔案: 68.8MB

解壓縮檔案: hourly_44201_2018.csv

解壓縮檔案大小: 2.05GB

資料筆數: 9,366,419 **(約936萬筆資料)**

欄位個數: 24

欄位名稱:  
"State Code", "County Code", "Site Num", "Parameter Code", "POC",  
"Latitude", "Longitude", "Datum", "Parameter Name", "Date Local",  
"Time Local", "Date GMT", "Time GMT", "Sample Measurement", "Units of Measure",  
"MDL", "Uncertainty", "Qualifier", "Method Type", "Method Code",  
"Method Name", "State Name", "County Name","Date of Last Change"

library(readr)  
system.time(ozone <- read_csv("hourly_44201_2018.csv", col_types = "cccnnnnccDtDtncnlccccccD")) # 37.78秒  
#### #  user  system elapsed   
#### # 36.14    2.30   37.78   

### nwind.csv

資料說明: 北風訂單資料

資料來源: Microsoft Access 北風資料庫

資料筆數: 2155

欄位個數: 8

欄位名稱: OrderDetailsID,	OrderID, ProductName, OrderDate, ProductID, CustomerID, UnitPrice, Quantity

### northwind_trans.csv

資料說明: 北風訂單資料, 提供於 arules package -北風資料庫操作篇之練習範例資料

[參考資料](http://rwepa.blogspot.com/2013/01/arules-package.html)

資料來源: Microsoft Access 北風資料庫

資料筆數: 2153

欄位個數: 5

欄位名稱: OrderID, ProductName, Price, Quantity, Discount

### population.taiwan.csv
資料筆數: 21

欄位個數: 6

欄位名稱: City, Lat, Long, City_Chinese, Population, Area

### production.csv
資料說明: 參考 R資料匯入與匯出

[參考資料](http://rwepa.blogspot.com/2018/04/readoutput.html)

資料筆數: 10

欄位個數: 5

欄位名稱: 工號, 生產日期, 機台, 生產量, 目標量

### prostate.csv

資料說明: Prostate Cancer

資料來源: Ledolter, J., Data Mining and Business Analytics with R, John Wiley & Sons, 2013.

資料筆數: 97

欄位個數: 6

### termDocMatrix.RData

資料說明: Term-Document Matrix of Twitter Posts

資料筆數: Terms: 21列, Documents: 154行

### 全國訂單明細.twbx

資料來源: 全國訂單明細.xlsx (沈浩，王濤，韓朝陽，李健, 觸手可及的大數據分析工具：Tableau案例集, 電子工業出版社, 2015.)

Tableau 測試版本: 2018.3.11

工作表個數: 24

工作表名稱:
1.排序 2.階層 3.日期-連續變數 4.群組Group 5.群組-demo 6.函數SUM-利潤比例, 新增計算欄位名稱 利潤比率, SUM([利潤額])/SUM([銷售額]) 7.函數COUNT-訂單總計,  新增計算欄位名稱 計算總計, COUNT([產品類別]) 8.函數-DATEDIFF-反應時間, 新增計算欄位名稱 反應時間, DATEDIFF("day",[訂單日期],[運送日期]) 9.函數IF, 新增計算欄位名稱 利率比例修正後, SUM(IF [產品類別] = "傢俱產品" THEN [利潤額] + [運輸成本] ELSE [利潤額] END)/SUM([銷售額]) // 修正利潤率 10.函數+參數 11.快速表格計算 12.地圖 13.地圖-填滿 14.地圖-條形圖 15.長條圖 16.長條圖-轉置 17.長條圖-堆疊 18.長條圖-併排 19.線形圖 20.面積圖 21.圓形圖 22.複合圖 23.群組趨勢線 24.盒鬚圖

### 全國訂單明細.xlsx

資料來源: 沈浩，王濤，韓朝陽，李健, 觸手可及的大數據分析工具：Tableau案例集, 電子工業出版社, 2015.

資料筆數: 6568

欄位個數: 19

欄位名稱: 訂單號,訂單日期,顧客姓名,訂單等級,訂單數量,銷售額,折扣點,運輸方式,利潤額,單價,運輸成本,區域,省份,城市,產品類別,產品子類別,產品名稱,產品包箱,運送日期

### 北風.xlsx

資料說明: 參考 Microsoft Access 北風資料庫

資料表個數: 6

資料表名稱: 員工, 供應商, 產品, 訂單, 訂單詳細資料, 客戶

# Part 2 教學 Tutorial

### 10m_pandas.ipynb

資料說明: Python pandas 套件的10分鐘快速導覽 (實際練習時間應該會大於10分鐘)

資料來源: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

### aMarvelousR_Lee(pp238).pdf
資料說明: R 基礎篇 - 國立台北商業技術學院上課教材(238頁, 2011.7.4)

整合下列五大主題：
      1. Basic R
      2. Preparing Data
      3. Graphics
      4. Applied Statistics

### AssociationRules.pdf
arules package - 提供資料探勘中關聯規則apriori algorithm

### AssociationRules.R
關聯規則範例檔案 - R 程式檔

### AssociationRules_northwind.pdf
文章說明將資料轉換至 transactions 格式說明。

### AssociationRules_northwind.R
北風資料庫範例檔案 - R 程式檔

### bms-2018.11.19.pdf
資料說明: 育達科技大學 經營管理講座 - Big Data Application

日期: 2018.11.19

### Foundation.pdf
### Foundation.R

R 基礎篇

提供以下四大主題:

1. Introduction 簡介

2. Data Manipulation 資料處理

3. Descriptive Statistics 敘述統計

4. Graphics 繪圖

[參考網址](http://rwepa.blogspot.com/2013/01/r_4.html)

### installRMySQLtutorial.pdf
資料說明: Windows 環境中, 使用 RMySQL原始欄案, 自行編譯 RMySQL 套件

[自行編譯 RMySQL 套件](http://rwepa.blogspot.com/2013/01/windows-rmysql.html)

### prob.pdf
資料說明: 常用累計機率表

資料來源: 統計學：觀念、方法、應用(第4版), 賀力行、林淑萍、蔡明春, 前程文化, 2008.

### R3.0.0with_index_of_size 2^31.pdf
資料說明: R-3.0.0 已經支援數值索引值(numeric index values)達到 2^31 以上

資料來源: https://taichimd.us/mediawiki/index.php/R#Handling_length_2.5E31_and_more_in_R_3.0.0

### rattle-ROCcurve.pdf

資料說明: R圖形化使用者介面 rattle 套件 執行 ROC curve 比較

[參考資料](http://rwepa.blogspot.com/2013/08/data-mining-with-rattle-roc-curve-svm.html)

### RconnectMySQL.R

資料說明: R連結 MySQL範例程式

[參考資料](http://rwepa.blogspot.com/2013/01/windows-rmysql.html)

### Rcpp-Rtools-tutorial.pdf

資料說明: Rcpp 套件與C++應用

[參考資料](http://rwepa.blogspot.com/search?q=c%2B%2B)

### roc_introduction.pdf

資料說明: ROC Curve (Receiver Operating Characteristics) 簡介

### roc_r_example.pdf

資料說明: ROCR套件執行ROC計算繪圖
