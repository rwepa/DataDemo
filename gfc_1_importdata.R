# title    : 匯入 gfc 資料集
# date     : 2019.9.14
# updated  : 2022.6.16
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# Encoding : UTF-8

# 方法1 有錯誤訊息
# gfc <- read.table("gfc.csv", header=TRUE, sep=",")

# 方法2 正確匯入資料

# 在 Windows 作業系統中, 使用記事本開啟 gfc.csv, 另存新檔 ANSI 編碼格式, 檔名改為 gfc-ansi.csv

gfc <- read.table("gfc-ansi.csv", header=TRUE, sep=",")

# 2022.6.16 R-4.2.0
# 直接匯入 UTF-8編碼, 結果正確顯示, 沒有錯誤.
gfc <- read.table("gfc.csv", header=TRUE, sep=",")

gfc
str(gfc) # 293筆資料,3個欄位
summary(gfc)
plot(gfc$amount, type="l") # 應如何進行資少分析?
# end
