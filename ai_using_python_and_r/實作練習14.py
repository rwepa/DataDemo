# 實作練習14
# 檔案日期時間處理

# 下載 https://github.com/rwepa/DataDemo/blob/master/weblog.csv
# 檔案名稱: weblog.csv
# 欄位個數:4
# 資料筆數:16007
# IP	Time	URL	Staus
# 10.128.2.1	[29/Nov/2017:06:58:55	GET /login.php HTTP/1.1	200
# 10.128.2.1	[29/Nov/2017:06:59:02	POST /process.php HTTP/1.1	302
# 10.128.2.1	[29/Nov/2017:06:59:03	GET /home.php HTTP/1.1	200
# 資料來源: https://www.kaggle.com/shawon10/web-log-dataset

# 練習使用 open, datetime 等處理技術, 計算下列3個時段的資料筆數
# 06:00-14:00, 14:00-22:00, 22:00-06:00
# analysis: refer to materials and try it

import os
from datetime import datetime

os.chdir("C:/mydata") # 變更工作目錄
myfile = "weblog.csv"

##############################
# Part 1.分析模式
##############################

# 讀取資料 readlines
with open(myfile, "r") as infile:
    for line in infile:
        print(line)

# 解析日期,時間-方法1, 取代"["字元為空白
mystr = "10.128.2.1,[29/Nov/2017:06:58:55,GET /login.php HTTP/1.1,200"
mystr.split(",")
mystr.split(",")[1] # '[29/Nov/2017:06:58:55'
mystrDatetime = mystr.split(",")[1].replace("[", "")
mystrDatetime # '29/Nov/2017:06:58:55'

# str 轉換為 datetime
format_string = "%d/%b/%Y:%H:%M:%S"
x = datetime.strptime(mystrDatetime, format_string)
x
x.hour # datetime 取出小時
str(x) # datetime 轉換為 str

# 解析日期,時間-方法2, 保留"["字元
datetime.strptime("[29/Nov/2017:06:58:55", "[%d/%b/%Y:%H:%M:%S")

# 測試 IndexError
'Dec'.split(",")[1].replace("[", "")

# 測試 ValueError
datetime.strptime('Dec', format_string)

# 使用 try
try:
    datetime.strptime('Dec', format_string)
    'Dec'.split(",")[1].replace("[", "")
except (ValueError, IndexError):
        print('Error')
else:
    print("OK")

# 06:00-14:00, 14:00-22:00, 22:00-06:00
# period1, period2, period3(左側有等號,右側沒有等號)

##############################
# Part 2.整合版本
##############################

period1 = list()
period2 = list()
period3 = list()

with open(myfile, "r") as infile:
    next(infile) # 第1列為標題列, 先跳過並執行下一筆資料
    format_string = "%d/%b/%Y:%H:%M:%S" # str 轉換為 datetime
    for data in infile:
        try:
            tmp = data.split(",")[1].replace("[", "") # 取代
            mydatetime = datetime.strptime(tmp, format_string) # 轉換為 datatime
            mydatetimeHour = mydatetime.hour # 取出小時
        except (ValueError, IndexError): # 使用 except 處理錯誤
            pass
        else:
            # print(tmp)
            # print(str(mydatetimeHour))
            if mydatetimeHour >= 22:
                period3.append(str(mydatetimeHour))
            elif mydatetimeHour >= 14 and mydatetimeHour < 22:
                period2.append(str(mydatetimeHour))
            elif mydatetimeHour >= 6 and mydatetimeHour < 14:
                period1.append(str(mydatetimeHour))
            elif mydatetimeHour < 6:
                period3.append(str(mydatetimeHour))
    print('...資料讀取完成')
# end for reading
            
##############################
# Part 3.結論
##############################
print(period1)
print(period2)
print(period3)

periodAnalysis = {'06:00-14:00': len(period1),
                  '14:00-22:00': len(period2),
                  '22:00-06:00': len(period3)}
periodAnalysis 
# {'06:00-14:00': 3250, '14:00-22:00': 11244, '22:00-06:00': 1295}
sum(periodAnalysis.values()) # 15789, 請驗證正確性!
# end
