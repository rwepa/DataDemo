# 主題: 單一大型航班資料匯入至R

# 日期: 2020.3.6

# 壓縮檔案: airline_int_cols.csv.bz2

# 下載連結: https://reurl.cc/62gDNV

# 航班資料: airline_int_cols.csv.bz2, 解壓縮後的檔名為 airline_int_cols.csv

# 資料大小: 10.7GB

# 測試環境: Intel Core i7-8550U CPU, RAM 8GB, Windows 10 64位元

# 方法1
library(data.table)

system.time(airline <- fread("airline_int_cols.csv"))
# 錯誤: 無法配置大小為 518.7 Mb 的向量
# Timing stopped at: 0.45 0 1.17

# 方法2 bigmemory package
library(bigmemory)

system.time(airline <- read.big.matrix("airline_int_cols.csv", 
                                       header = TRUE,
                                       backingfile = "airline.bin",
                                       descriptorfile = "airline.desc",
                                       type = "integer"))

dim(airline)
