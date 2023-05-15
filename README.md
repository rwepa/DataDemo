# 資料集與使用範例
提供資料集與範例分享, 資料集來自於 Open data或模擬資料.

---

常用變數名稱:

X: 自變數, 獨立變數 independent variable, 預測變量 predictor variable, 解釋變量 explanatory variable, 共變量 covariate.

Y: 反應變數 response variable, 因變數, 依變數, 應變數, 被解釋變數 dependent variable, 結果變數 outcome variable.

# Part 1 資料 Data (依英文字母排序)

### adult.csv

資料來源: https://www.kaggle.com/datasets/wenruliu/adult-income-dataset

資料筆數: 48842

欄位個數: 15

欄位名稱:

age              年齡

workclass        工作類型(8個, 包括?)

fnlwgt           權重 (數值資料)

education        教育程度(16個)

educational-num  教育程度的數值型態(1~16)

marital-status   婚姻狀態(7個)

occupation       產業別(14個, 包括?)

relationship     家庭成員(6個)

race             種族(5個)

gender           性別(2個)

capital-gain     資本收益

capital-loss     資本損失

hours-per-week   每週工時

native-country   國籍(有?)

income           收入(2個, <=50K, >50K)

### airline_int_cols.md

資料說明: 單一大型航班資料

下載檔案: airline_int_cols.csv.bz2 (1.38GB)

參考連結: https://github.com/rwepa/DataDemo/blob/master/airline_int_cols.md

航班資料: airline_int_cols.csv.bz2 解壓縮後的檔名為 airline_int_cols.csv (10.7GB)

### airline_multiples.md

資料說明: 多筆大型航班資料

下載檔案: AirlineDelays.tar.bz2 (1.54GB)

參考連結: https://github.com/rwepa/DataDemo/blob/master/airline_multiples.md

解壓縮後包括22個檔案, 檔名為: 1987.csv, 1988.csv, ..., 2008.csv (檔案大小: 121MB ~ 670MB)

資料大小: 22個檔案, 合計11.2GB

### antidiabeticdrug.csv

資料說明: 從1992年到2008年，澳大利亞每月的抗糖尿病藥物銷售量。

資料來源: R語言 a10 {fpp}

資料筆數: 204

欄位個數: 2

欄位名稱: date, sale

資料匯出:

library(fpp)

a10

seasonplot(a10)

sale <- c(a10)

date <- seq(from = as.Date('1991-7-1'), to = as.Date('2008-6-1'), by = 'month')

antidiabeticdrug <- data.frame(date, sale)

write.csv(antidiabeticdrug, file = 'antidiabeticdrug.csv', row.names = FALSE)

### aqx_p_434_20200720134939.csv

資料說明: 日空氣品質指標(AQI)

資料來源: https://data.gov.tw/dataset/40507

資料筆數: 1000

欄位個數: 11

欄位名稱: SiteId, SiteName, MonitorDate, AQI, SO2SubIndex, COSubIndex, O3SubIndex, PM10SubIndex, NO2SubIndex, O38SubIndex, PM25SubIndex

### bank_deposit.csv

資料說明: 銀行定期存款商品銷售

資料來源:

https://archive.ics.uci.edu/ml/datasets/Bank+Marketing

資料筆數: 45211

欄位個數: 17

欄位名稱:

age       : 年齡

job       : 工作

marital   : 婚姻 {divorced, married, single}

education : 教育程度

default   : 是否有個人違約記錄

balance   : 帳戶餘額

housing   : 是否有房屋

loan      : 是否有個人貸款

contact   : 連絡方式

day       : 最近連絡日

month     : 最近連絡月

duration  : 最近連絡通話時間秒數. duration愈小時, subscribed 較可能為no.

campaign  : 連絡次數

pdays     : 最近與客戶聯繫之後經過的天數, -1表示以前未與客戶聯繫

previous  : 連絡次數 

poutcome  : 最近行銷結果 {failure, other, success, unknown}

subscribe : {yes 有購買定期存款商品, no 沒有購買定期存款商品} --> 反應變數

### boston.csv

資料來源: UCI Machine Learning Repository [https://archive.ics.uci.edu/ml/machine-learning-databases/housing/]

資料筆數: 506

欄位個數: 14

欄位名稱:

CRIM      : per capita crime rate by town 人均犯罪率

ZN        : proportion of residential land zoned for lots over 25,000 sq.ft. 超過2萬5仟平方呎住宅用比例

INDUS     : proportion of non-retail business acres per town 商業用地的比例

CHAS      : Charles River dummy variable (= 1 if tract bounds river; 0 otherwise) 1:靠近查爾斯河岸, 0:沒有

NOX       : nitric oxides concentration (parts per 10 million) 一氧化氮濃度

RM        : average number of rooms per dwelling 每戶平均房間數

AGE       : proportion of owner-occupied units built prior to 1940 在1940前屋主自建比例

DIS       : weighted distances to five Boston employment centres  距離波士頓5個就業中心的加權距離

RAD       : index of accessibility to radial highways 高速公路便利指標

TAX       : full-value property-tax rate per $10,000 每$10000元總價與房屋稅的比例

PTRATIO   : pupil-teacher ratio by town  生師比

B         : 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town 非裔指標

LSTAT     : % lower status of the population 低收人口比例

MEDV      : Median value of owner-occupied homes in $1000's 自用住宅的房價中位數 --> 反應變數

### Cars93.csv

資料來源: R語言 - Cars93 {MASS}

資料筆數: 93

欄位個數: 27

data(Cars93, package = "MASS")

write.csv(Cars93, file = "Cars93.csv", row.names=FALSE)

### ChemicalManufacturingProcess.csv

資料說明: 醫藥產品製程分析資料集

資料來源: R語言 - ChemicalManufacturingProcess {AppliedPredictiveModeling}

資料筆數: 176

欄位個數: 58

欄位說明: 全部資料型態皆為數值, Yield 為反應變數

### chorddiag.zip

資料說明: chorddiag Windows 版本套件壓縮檔

版本資訊: 0.1.2

資料來源: https://github.com/mattflor/chorddiag

### claim.cls

資料說明: 保險理賠(簡體版本)

資料筆數: 20479

欄位個數: 15

### concrete.csv

混凝土強度估計資料集

資料來源: https://archive.ics.uci.edu/ml/datasets/concrete+compressive+strength

參考: I.-C. Yeha, Modeling of strength of high-performance concrete using artificial neural networks, Cement and Concrete Research, Volume 28, Issue 12, 1797-1808, 1998.

資料筆數: 1030

欄位個數: 9

欄位名稱:

cement : 水泥

slag : 礦渣

ash : 飛灰

water : 水

superplastic : 強塑劑

coarseagg : 粗骨材

fineagg : 細骨料

age     : 齡期

strength : 強度 --> 反應變數

### credit.arff

資料說明: Statlog (German Credit Data) Data Set

資料來源: https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)

資料筆數: 1000

欄位個數: 21

檔案說明: 採用 ARFF(Attribute-Relation File Format), 即屬性-關係檔案格式, 為 WEKA 軟體資料格式檔案.

### credit.csv

資料說明: Statlog (German Credit Data) Data Set

資料來源: https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)

資料筆數: 1000

欄位個數: 21

### diabetes.csv

資料說明: Pima Indian Diabetes (糖尿病) Dataset

資料來源: https://www.kaggle.com/uciml/pima-indians-diabetes-database

資料筆數: 768

欄位個數: 9

欄位名稱:

Pregnancies              懷孕次數

Glucose                  血漿葡萄糖濃度

BloodPressure            舒張壓

SkinThickness            三頭肌皮脂厚度

Insulin                  胰島素濃度

BMI                      身體質量指數

DiabetesPedigreeFunction 糖尿病函數,依家族糖尿病史而計算個人患有糖尿病的風險值

Age                      年齡

Outcome                  {1:有糖尿病, 0:無糖尿病} --> 反應變數

### drink.csv

資料說明: 配合R基礎篇2011年操作資料集 http://rwepa.blogspot.com/2013/01/r-201174.html

資料筆數: 20

欄位個數: 1

欄位名稱: sales

### german_credit.csv

資料說明: 德國銀行貸款風險資料

資料來源: https://www.kaggle.com/kabure/german-credit-data-with-risk, https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)

資料筆數: 1000

欄位個數: 10

欄位名稱:

Age 年齡

Sex 性別 {male, female}

Job 工作 {0,1,2,3}

    0 - unskilled and non-resident 非技術人員和非居民
    
    1 - unskilled and resident 非技術人員和居民
    
    2 - skilled 技術人員
    
    3 - highly skilled 高度技術人員

Housing 住宅 {own, rent, free}

Saving.accounts 儲蓄賬戶 {little, moderate, rich, quite rich}

Checking.account 存款金額 {little, moderate, rich}

Credit.amount 貸款金額 (德國馬克)

Duration 貸款期間(月)

Purpose 貸款用途 {car, furniture/equipment, radio/TV, domestic appliances, repairs, education, business, vacation/others}

Risk 風險指標 {good, bad}, good:表示通過貸款或信用評估為良好 --> 反應變數

![image](https://github.com/rwepa/DataDemo/blob/master/imgs/credit.png)

### gfc.csv

資料說明: 提供工廠訂單資料

資料來源: 模擬資料

資料筆數: 293

欄位個數: 3

欄位名稱: orderdate, supplier, amount

### h_nhi_ipdte103.sas7bdat

資料說明: 103年模擬全民健保處方及治療明細檔_西醫住院檔

資料筆數: 14297

欄位個數: 80

檔案大小: 7.25MB

### hourly_44201_2018.csv

更新日期: 2019/11/2

資料說明: 美國國家環境保護局 (United States Environmental Protection Agency) 2018年每小時臭氣資料

資料下載: https://aqs.epa.gov/aqsweb/airdata/download_files.html --> Tables of Hourly Data, Ozone (44201), 2018.

檔案名稱: hourly_44201_2018.zip (https://aqs.epa.gov/aqsweb/airdata/hourly_44201_2018.zip)

檔案大小: 68.8MB

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
##### #  user  system elapsed   
##### # 36.14    2.30   37.78   

參考網站: http://rwepa.blogspot.com/2019/11/r-makenames-base.html  

### human_resource.csv

資料說明: 人力資源資料

資料來源: https://github.com/Surya-Murali/Human-Resource-Analytics-in-R/tree/master/Dataset

資料筆數: 14999

欄位個數: 10

欄位名稱:

last_evaluation       : 最近考核分數 0~1分

number_project        : 每年平均專案個數

average_montly_hours  : 每月平均工作小時

time_spend_company    : 在公司時間

Work_accident         : 工安意外, 1:有, 0:沒有

satisfaction_level    : 工作滿意度

left                  : 是否離職, 1:離職, 0:沒有 --> 反應變數

promotion_last_5years : 近5年是否有升遷, 1:有, 0:沒有

role                  : 服務單位

salary                : 薪資別: high, median, low

### hw1.csv

資料說明: 配合R基礎篇2011年操作資料集 http://rwepa.blogspot.com/2013/01/r-201174.html

資料筆數: 25

欄位個數: 4

欄位名稱: No, x1, x2, x3

### IOT-temp.csv

資料說明: 物聯網溫度資料

資料來源: https://www.kaggle.com/atulanandjha/temperature-readings-iot-devices

資料筆數: 97606

欄位個數: 5

欄位說明: id, room_id/id, noted_date, temp, out/in

id : 編號 unique IDs for each reading, 如果有重複值, 須進行資料處理

room_id/id : 房間代碼 room id in which device was installed (inside and/or outside) -> currently 'admin room' only for example purpose.

noted_date : 日期 date and time of reading

temp : 溫度 temperature readings

out/in : 房間內/外 whether reading was taken from device installed inside or outside of room?

任務:

1. 最高和最低溫度是多少？

2. 室外溫度與室內溫度有何關係？

3. 室內和室外室溫的溫度變化如何？

4. 資料趨勢如何？

5. 您可以使用時間序列法來預測未來情況嗎？

6. 哪個月最熱/最冷？

7. 有找到來自氣候災難的警告信號(離群值)?

### insurance.csv

資料說明: 醫療費用預測資料集

資料來源: Machine Learning with R, Second Edition, 2015.

資料筆數: 1338

欄位個數: 7

欄位名稱:

age: 受益人的年齡

sex: 性別

bmi: 理想 BMI 18.5 to 24.9

children: 保險計劃所涵蓋的子女/家屬人數

smoker: 是否有抽煙

region: 美國四大區 {northeast, southeast, southwest, or northwest}

expenses: 醫療費用

### letterdata.csv

資料說明: 英文字母OCR分類問題

資料來源: https://archive.ics.uci.edu/ml/datasets/letter+recognition

資料筆數: 20000

欄位個數: 17

欄位名稱: 

應變數 (dependent variable): letter (A~Z)

自變數 (independent variable) 16個: xbox,ybox,width,height,onpix,xbar,ybar,x2bar,y2bar,xybar,x2ybar,xy2bar,xedge,xedgey,yedge,yedgex

### marketing.csv

資料說明: 行銷廣告資料

資料來源: R語言 - marketing {datarium}

資料筆數: 200

欄位個數: 4

欄位名稱: youtube, facebook, newspaper, sales

資料預覽:

![image](https://github.com/rwepa/DataDemo/blob/master/imgs/marketing.png)

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

### OnlineRetail.csv.zip

資料來源: https://www.kaggle.com/vijayuv/onlineretail

說明: 本資料與 OnlineRetail.xlsx 相同, 解壓縮後格式為 csv

### OnlineRetail.xlsx

資料來源: http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx

資料筆數: 541909

欄位個數: 8

欄位名稱: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

說明: 原下載檔名為 Online Retail.xlsx, 中間有個空白, 建議另存新檔時,刪除空白為 OnlineRetail.xlsx

### opendata109b141_birth.csv

資料說明: 109年度嬰兒出生數按嬰兒性別及生父母年齡分（按發生）

資料來源: https://data.gov.tw/dataset/146626

資料筆數: 66240

欄位個數: 8

欄位名稱英文: statistic_yyy, according, district_code, site_id, sex, father_age, mother_age, birth_count

欄位名稱中文: 統計年度, 按照別, 區域別代碼, 區域別, 嬰兒性別, 生父年齡, 生母年齡, 嬰兒出生數

### PowerBI_consumption.zip

資料說明: 台北市, 桃園市, 新北市的食衣住行消費資料, 合計3個資料夾, 12個CSV檔案

資料來源: https://www.nccc.com.tw/wps/wcm/connect/zh/home

### PowerBI_creditcard.xlsx

資料說明: 信用卡刷卡模擬資料集, 9個工作表

資料來源: 謝邦昌等,Power BI 金融大數據分析應用 -- 貼近產業實務，掌握決策效率, 碁峰資訊, 2021.

### pokemon.csv

資料筆數: 894

欄位個數: 12

欄位名稱: 

Number      寶可夢編號, 會有重複值

Name        名字

Type1       第1屬性

Type2       第2屬性

HP          血量

Attack      攻擊力

Defense     防禦力

SpecialAtk  特殊攻擊力

SpecialDef  特殊防禦力

Speed       速度

Generation  世代(1~7)

Legendary   是否為神獸(TRUE, FALSE)

Source: https://www.kaggle.com/datasets/rounakbanik/pokemon

參考: 林英志, TQC Python 3.x 機器學習基礎與應用特訓教材, 全華, 2021.  

### population.taiwan.csv

資料筆數: 21

欄位個數: 6

欄位名稱: City, Lat, Long, City_Chinese, Population, Area

### production.csv

資料說明: 參考 R 資料匯入與匯出 [參考資料](http://rwepa.blogspot.com/2018/04/readoutput.html)

資料筆數: 10

欄位個數: 5

欄位名稱: 工號, 生產日期, 機台, 生產量, 目標量

### prostate.csv

資料說明: Prostate Cancer

資料來源: Ledolter, J., Data Mining and Business Analytics with R, John Wiley & Sons, 2013.

資料筆數: 97

欄位個數: 6

### R03_Orders.txt

資料說明: 配合R基礎篇2011年操作資料集 http://rwepa.blogspot.com/2013/01/r-201174.html

資料筆數: 10萬

欄位個數: 5

欄位名稱: OrderID, OrderDate, BookID, Quantity, Price

### r_in_nutshell_data_bb.zip

資料說明: 

1. Adler, Joseph, R In a Nutshell, O'Reilly Media, 2012. 範例資料集

2. 資料來源 https://resources.oreilly.com/examples/9780596801717/tree/master/nutshell/data

3. 解壓縮後為 bb.db 檔案, 可使用 RSQLite 套件載入

### r_in_nutshell_data_Rdata.zip

資料說明: 

1. Adler, Joseph, R In a Nutshell, O'Reilly Media, 2012. 範例資料集

2. 資料來源 https://resources.oreilly.com/examples/9780596801717/tree/master/nutshell/data

3. 20筆 rda 資料集

GSE2034

SPECint2006

audioscrobbler

batting.2008

births2006.smpl: births2006.idx

consumption

doctorates

dow30

field.goals

ham.price.ts

mort06.smpl

sanfrancisco.home.sales: sanfranscisco.home.sales.testing.indices sanfrancisco.home.sales.training.indices

schiller.index: schiller.other.data

spambase

team.batting.00to08

tires.sus (輪胎耐磨性測試資料)

top.bacon.searching.cities

toxins.and.cancer

turkey.price.ts

yosemite

### school.sav

資料說明: SPSS 軟體 SAV 檔案

資料筆數: 200

欄位個數: 19

### score.csv

資料說明: 配合R基礎篇2011年操作資料集 http://rwepa.blogspot.com/2013/01/r-201174.html

資料筆數: 7

欄位個數: 3

欄位名稱: s.id, quiz1, quiz2

### server_logs.csv

資料說明: 主機日誌檔

資料來源: https://www.kaggle.com/kartikjaspal/server-logs-suspicious

資料筆數: 172838

欄位個數: 16

欄位說明: class欄位包括以下三種情形 {normal, suspicious, unknown}

### shinyStockVis.zip

資料說明: shiny Taiwan Stock App

https://rwepa.shinyapps.io/shinyStockVis/

程式碼: https://github.com/rwepa/DataDemo/blob/master/shinyStockVis.zip

### snsdata.csv

資料說明: FB社群找出青少年目標族群

資料筆數: 30000

欄位個數: 40

### sonar.csv

資料說明: 水雷與岩石分類問題

資料來源: http://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks)

資料筆數: 208

欄位個數: 61

第61行: R: rock  岩石, M: mine 水雷

### sp500.RData

資料說明: 採用 sp500 {gt}, 記錄 1950/1/3 - 2015/12/31, 原資料集依日期遞減排序, 已更新依日期遞增排序.

資料筆數: 16607

欄位個數: 7

欄位名稱: date, open, high, low, close, volume, adj_close

參考資料: sp500.R [https://github.com/rwepa/DataDemo/blob/master/sp500.R]

### sse.RData

資料說明: 2009-2013年上證指數相關資料(上海證券交易所綜合股價指數, SSE Composite Index), SSE: Shanghai Stock Exchange.

資料來源: 量化投資：以R語言為工具, 蔡立耑, 電子工業出版社.

資料筆數: 18164列, 8行

欄位名稱: sseindex, date, DayWeek, open, high, low, close, return

使用方法: load(url("https://github.com/rwepa/DataDemo/blob/master/sse.RData?raw=true"), verbose = TRUE)

### Tableau_Financial_Products_Case_Study.pdf

### Tableau_Financial_Products_Case_Study.twbx

資料說明: 國立臺北科技大學資訊與財金管理系(所) - Tableau金融商品案例分析

### T-Bike-tainan-station(CSV).xlsx

資料說明: 整合2個CSV為1個 Excel 檔案

(1).T-Bike 臺南市公共自行車租賃站資訊(CSV) 工作表

資料說明: T-Bike 臺南市公共自行車租賃站資訊

資料來源: https://data.gov.tw/dataset/53909

資料筆數: 75

欄位個數: 9

欄位名稱:

Id                    編號

Station Name          站名

Address               地址

Capacity              格位數 (格位數=可借車輛數+可停空位數)

Avaliable Bike Count  可借車輛數

Avaliable Space Count 可停空位數

Update Time           更新時間

Latitude              緯度

Longitude             經度

(2).T-Bike-tainan-station-district 工作表

資料說明: T-Bike 臺南市公共自行車租賃站-區域對照表

資料來源:筆者整理

資料筆數: 77

欄位個數: 2

欄位名稱: 站點區域, 站點名稱

### TelcoChurn.csv

資料說明: 電信公司客戶流失資料集

資料來源: https://www.kaggle.com/blastchar/telco-customer-churn

資料筆數: 7043

欄位個數: 21

自變數:

customerID, customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges 等20個

依變數: Churn {Yes, No}

### termDocMatrix.RData

資料說明: Term-Document Matrix of Twitter Posts

資料筆數: Terms: 21列, Documents: 154行

### titanic.csv

資料說明: 鐵達尼號資料集

資料筆數: 1313

欄位個數: 11

欄位名稱: row.names, pclass, survived, name, age, embarked, home.dest, room, ticket, boat, sex

### tmdb-movie-metadata.zip

資料說明: 電影資料 TMDB 5000 Movie Dataset, 

資料來源: https://www.kaggle.com/tmdb/tmdb-movie-metadata

使用𦑦明: 解壓縮zip後為2個檔案 (tmdb_5000_credits.csv, tmdb_5000_movies.csv)

檔名: tmdb_5000_credits.csv (38.1MB)

資料筆數: 4803

欄位個數: 4

檔名: tmdb_5000_movies.csv (5.43MB)

資料筆數: 4803

欄位個數: 20

### tw2000.csv

資料說明: 2000年1月1日~2019年12月31日台灣加權股價指數

資料筆數: 5017

欄位個數: 7

欄位名稱: Date, TWII.Open, TWII.High, TWII.Low, TWII.Close, TWII.Volume, TWII.Adjusted

### tw_stock_list.xlsx

資料說明: 台灣上市,上櫃股票代碼

更新日期: 2022.4.20

資料筆數: 1758

欄位個數: 7

資料來源: https://isin.twse.com.tw/isin/C_public.jsp?strMode=2

### tx_1min_2014.csv

資料說明: 台指期2014年1分鐘Tick資料集

資料筆數: 74217

欄位個數: 7

欄位名稱: Date, Time, Open, High, Low, Close, TotalVolume

資料範圍: 2014/1/2 08:46:00 - 2014/12/31 13:45:00

### web_traffic.csv

資料說明: 網頁流量資料

資料筆數: 743

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

### 臺北市10401-10806汽車竊盜點位資訊.csv

資料說明: 政府資料開放平臺 臺北市汽車竊盜點位資訊

資料來源: https://data.gov.tw/dataset/116806

資料筆數: 422

欄位個數: 5

欄位名稱: 編號,案類,發生(現)日期,發生時段,發生(現)地點

日期: 2020.4.1

---

# Part 2 教學 Tutorial

### 10m_pandas.ipynb

資料說明: Python pandas 套件的10分鐘快速導覽 (實際練習時間應該會大於10分鐘)

資料來源: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

### 2019nCoV.R

資料說明: 2020新型冠狀病毒視覺化

使用套件: leaflet, htmltools

日期: 2020.2.13

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

### ggplot2-hcl.R

資料說明: 使用 ggplot2套件與 hcl 客製化繪圖顏色之R程式碼

參考網頁: http://rwepa.blogspot.com/2020/09/ggplot2-hcl-customized-color.html

### greek.pdf

資料說明: 希臘字母讀音表

### installRMySQLtutorial.pdf

資料說明: Windows 環境中, 使用 RMySQL原始欄案, 自行編譯 RMySQL 套件

[自行編譯 RMySQL 套件](http://rwepa.blogspot.com/2013/01/windows-rmysql.html)

### iot_bigdata.pdf

### 主題: 物聯網與⼤數據的整合應⽤

### 內容:

1. 資料分析/視覺化成果

2. 大數據簡介

3. 大數據分析工具與架構

4. R簡介、下載與安裝

5. RStudio 簡介、下載與安裝

6. R使用環境

7. 溫度感測案例分析

### prob.pdf
資料說明: 常用累計機率表

資料來源: 統計學：觀念、方法、應用(第4版), 賀力行、林淑萍、蔡明春, 前程文化, 2008.

### Python_Programming_Lee.pdf

資料說明: Python 程式設計 - 李明昌 (免費電子書)

目錄:

第 1 章 Python 語言簡介
1.1 Python 簡介
1.2 Python 特性與應用
1.3 Python 安裝
1.4 Python 操作

第 2 章 Anaconda 簡介與安裝
2.1 Anaconda 特性
2.2 Anaconda 下載與安裝
2.3 Anaconda 套件管理
2.4 Spyder 操作

第 3 章 Python 語法與流程控制
3.1 資料型別與運算子
3.2 NumPy 模組的使用
3.3 reshape 應用
3.4 離群值處理
3.5 if 與 for 處理

第 4 章 資料型別與資料處理
4.1 Tuple 序列
4.2 List 串列
4.3 Set 集合
4.4 Dictionaries 字典

第 5 章 檔案匯入與匯出
5.1 認識 pandas 模組
5.2 資料輸入/輸出

第 6 章 視覺化應用
6.1 視覺化簡介
6.2 認識 matplotlib 模組
6.3 matplotlib 繪圖應用
6.4 seaborn 模組繪圖
6.5 互動式繪圖

第 7 章 迴歸分析
7.1 迴歸模型 Regression Model
7.2 迴歸分析 - 使用 scikit-learn 模組

第 8 章 決策樹
8.1 決策樹
8.2 鐵達尼號資料集-決策樹應用

第 9 章 關聯規則應用
9.1 購物籃分析（market-basket analysis）
9.2 mlxtend 模組

第 10 章 推薦系統
10.1 何謂推薦系統 Recommender System
10.2 電影推薦系統

參考文獻

### Python_Programming_Lee_ipynb.zip

更新日期: 2020.2.28

資料說明: Python程式設計-李明昌.pdf 書籍的原始 ipynb 檔案

建壓縮後目錄 python.book.lee 包括以下:

Python程式設計-李明昌.ipynb

img 目錄 - 原始圖檔

data 目錄 - 包括書籍資料檔案

###### 範例資料集:

- p.093 [322] 台灣電力公司_各縣市再生能源別購入情形 data/RenewableEnergy.csv

- p.097 [331] 台灣電力公司_煙道資料即時量測值 data/flue.xml

- p.128 [361] 網頁流量資料集 data/web_traffic.csv

- p.130 [366] 水雷資料集 https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data

- p.159 [393] 波士頓房價資料 https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data

- p.174 [409] 鐵達尼號資料集 data/data/titanic.csv

- p.185 [431] 線上購物資料集 data/OnlineRetail.xlsx https://github.com/rwepa/DataDemo/blob/master/OnlineRetail.xlsx

- p.199 [443] 電影資料集 data/tmdb-movie-metadata/tmdb_5000_credits.csv

- p.200 [444] 電影推薦資料集 data/tmdb-movie-metadata/tmdb_5000_movies.csv

### R-4.0.1-Rcmdr-correct.pdf
資料說明: 使用R-4.0.1語言, 開啟Rcmdr套件自動關閉異常現象, 改用 R-4.0.0 已經正常開啟 Rcmdr 視窗.

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

### regression_01.pdf

資料說明: 提供迴歸模型最小平方法的簡易數理證明

### roc_introduction.pdf

資料說明: ROC Curve (Receiver Operating Characteristics) 簡介

### svm_example-R.pdf

資料說明: R 的 SVM 使用說明, 範例包括：214筆資料，輸入變數維度為9個.

### svm_introduction.pdf

資料說明: 支持向量機(Support Vector Machines, SVM) 概念介紹.

### roc_r_example.pdf

資料說明: ROCR套件執行ROC計算繪圖

### weblog.csv

資料說明: 網頁日誌資料檔

資料來源: https://www.kaggle.com/shawon10/web-log-dataset

檔案名稱: weblog.csv

欄位個數: 4

欄位名稱: IP, Time, URL, Staus

資料筆數: 16007

### windows_intall_R.pdf

資料說明: Windows 環境安裝R的完整步驟

### Windows 11 取消工作列合併 

參考: https://github.com/valinet/ExplorerPatcher

下載: https://github.com/valinet/ExplorerPatcher/releases/latest/download/ep_setup.exe

執行安裝程式: ep_setup.exe, 按左鍵二下即安裝完成.

設定方式: Windows 11 \ 最底下工作列 \ 右鍵 \ 內容: <ins>Taskbar</ins> \ Combine taskbar icons on primary taskbar: Never combine(default) 預設為不合併.

### pyTranscriber

免費程式並提供圖形化操作介面, 將影音檔 (MP3, MP4, WAV, M4A, WMA) 自動擷取並產生中文(或其他語言)字幕srt檔案, 可作為 YouTube 字幕檔.

網站更新: https://github.com/raryelcostasouza/pyTranscriber/releases

下載連結: https://github.com/raryelcostasouza/pyTranscriber/releases/download/v1.9/pyTranscriber-1.9-win-installer.exe
