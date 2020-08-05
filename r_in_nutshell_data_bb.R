# title: 載入 SQLite 資料集
# date: 2020.8.5

# 下載資料 r_in_nutshell_data_bb.zip, 解壓縮為 bb.db
# https://github.com/rwepa/DataDemo/blob/master/r_in_nutshell_data_bb.zip

library(RSQLite)

# 載入資料庫驅動程式
drv <- dbDriver("SQLite")

# 建立資料庫連結
con <- dbConnect(drv, dbname = "bb.db")

class(drv)

# 資料庫元資料
dbGetInfo(con)

# 資料表清單
dbListTables(con)

# 欄位清單
dbListFields(con,"Allstar")

# SQL 查詢資料
wlrecords <- dbGetQuery(con, "SELECT * FROM Teams")

wlrecords.2008 <- dbGetQuery(con, "SELECT teamID, W, L FROM Teams where yearID = 2008 and lgID = 'AL'")

# 讀取資料表全部內容
batters <- dbReadTable(con, "Batting")

# 資料結構
str(batters)

# 資料摘要
summary(batters)
