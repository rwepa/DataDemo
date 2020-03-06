主題: 大量航班資料匯入至R

日期: 2020.3.6

壓縮檔案: AirlineDelays.tar.bz2

下載連結: https://reurl.cc/xZDER5

航班資料: AirlineDelays.tar.bz2(1.54GB), 解壓縮後包括22個檔案, 檔名為: 1987.csv, 1988.csv, ..., 2008.csv

資料大小: 22個檔案合計11.2GB, 檔案大小(121MB ~ 670MB)

![airline_multiples_22files](https://user-images.githubusercontent.com/36437869/76059899-f6f49000-5fba-11ea-87ef-deaf08a57dbf.png)

使用一般 read.csv 即可直接讀取

```{r  eval=FALSE}
system.time(delay1987 <- read.csv("1987.csv"))
            
str(delay1987)
```

完成畫面

![airline_multiples_R](https://user-images.githubusercontent.com/36437869/76058949-9b290780-5fb8-11ea-80f4-f115b5598a4b.png)
