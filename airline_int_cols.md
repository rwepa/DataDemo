主題: 單一大型航班資料匯入至R

作者: Ming-Chang Lee

日期: 2020/3/6

下載檔案: airline_int_cols.csv.bz2 (1.38GB)

下載連結: https://reurl.cc/62gDNV

航班資料: airline_int_cols.csv.bz2 解壓縮後的檔名為 airline_int_cols.csv

資料大小: 10.7GB

![airline_int_cols_10 7GB](https://user-images.githubusercontent.com/36437869/76048218-277b0080-5fa0-11ea-839e-59f712fbaafb.png)

測試環境: Intel Core i7-8550U CPU, RAM 8GB, Windows 10 64位元

```{r  eval=FALSE}
方法1
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
```

完成畫面

![airline_int_cols_R](https://user-images.githubusercontent.com/36437869/76055387-729c1000-5fae-11ea-83f1-ffa72f559742.png)       
