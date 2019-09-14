# import data
# 使用記事本開啟 gfc.csv, 另存新檔 ANSI 編碼格式, 檔名改為 gfc-ansi.csv
gfc <- read.table("gfc.csv", header=TRUE, sep=",") # Error in Windows OS
gfc <- read.table("gfc-ansi.csv", header=TRUE, sep=",")
gfc
str(gfc) # 293筆資料,3個欄位
summary(gfc)
plot(gfc$amount, type="l") # 應如何進行資少分析?
# end
