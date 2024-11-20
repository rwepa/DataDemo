# file     : ai_03_gold_price.py
# title    : 3.AI與黃金價格深度學習預測應用(LSTM)
# author   : Ming-Chang Lee
# date     : 2023.12.28
# YouTube  : https://www.youtube.com/@alan9956
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Email    : alan9956@gmail.com

# 大綱
# 3.1 CRISP-DM 六大步驟
# 3.2 黃金價格深度學習預測應用(LSTM)
# 3.3 台灣股市,ETF下載

##############################
# 3.1 CRISP-DM 六大步驟
##############################

# 步驟 1：商業理解
# 步驟 2：資料理解 
# 步驟 3：資料準備
# 步驟 4：建立模型
# 步驟 5：模型評估與測試
# 步驟 6：佈署應用

##############################
# 3.2 黃金價格深度學習預測應用(LSTM)
##############################

# 步驟 1：商業理解

# 目標是使用 Yahoo 開放式財金資料, 建立深度學習預測應用(LSTM).

# 黃金常用投資方法

# 1.實體黃金(不建議)

# 2.黃金存摺

# 3.黃金ETF(指數股票型基金, Exchange-Traded Funds, ETF)-5種商品

# (1).黃金價格追蹤ETF: ETF主要目的是追蹤黃金價格變化, 該ETF通常會真正的持有實物黃金（如金塊或金條）來追蹤黃金價格.

# (2).黃金礦業ETF: 主要持有金礦公司的股票, 投資人投資的項目不是「實物黃金」, 而是購買挖礦業者的股票, 等於是通過黃金礦業的興衰來參與黃金市場.

# (3).國際和地區性ETF: 例: 購買美國、加拿大、澳大利亞或南非等地的黃金ETF, 是以「地區」、「國家」作為畫分區隔.

# ETF範例:
# 00635U(台股): 元大S&P黃金
# 00708L(台股): 元大S&P黃金正2
# GLD: SPDR黃金指數型基金, 全球最大的黃金指數型基金
# IAU: iShares黃金信託ETF
# SLV: iShares白銀信託ETF
# GC:  紐約商業交易所的黃金期貨ETF (New York Stock Exchange, NYMEX)
# MGC: 芝加哥期貨交易所的黃金期貨ETF (Chicago Board of Trade, CBOT)

# 黃金ETF期貨: 使用黃金期貨來達成投資黃金的策略, 該ETF不會真正的持有實物黃金, 是以國際黃金市場未來某時點的黃金價格為交易標的的期貨合約, 而這類ETF由於具有時間價值的意義並具有較高的波動性.

# 本研究資料集為黃金期貨代號為 GC.

# 【黃金期貨注意事項】
# 優點：進入門檻低, 且不需要保管成本.
# 缺點：期貨合約會到期, 需要不停更換新合約, 無法放著不理.

# 4.黃金CFD(差價合約, Contract For Difference, CFD)

# 5.黃金相關個股

# 黃金單位
# 1公克 = 0.26667台錢 = 0.02667台兩
# 1盎司(ounce, 簡寫為 oz, 英兩) = 31.1035公克 = 8.29437台錢 = 0.829437台兩
# 1盎司大約等於1台兩
# 雖然黃金的英文是gold，但其在國際金融市場的簡稱卻是XAU，其中X代表它不是任何一國家發行的貨幣，AU則是黃金的化學符號。

# 查詢財金價格
# https://tw.stock.yahoo.com/
# 左上角輸入 GC=F

# 參考資料 - Gold Price Prediction | LSTM | 96% Accuracy 
# https://www.kaggle.com/code/farzadnekouei/gold-price-prediction-lstm-96-accuracy

# 步驟 2：資料理解

# 安裝模組
# https://pypi.org/project/yfinance/

# pip install yfinance

# 載入模組

# Part 1. 擷取財務金融資料
# yfinance 會自動載入 pandas 模組

import yfinance as yf # yf.download 擷取財金資料

# Part 2. 資料處理
import numpy as np
# import pandas as pd

# Part 3. 資料視覺化
import plotly.express as px
import matplotlib.pyplot as plt

# Part 4. 深度學習
from sklearn.preprocessing import MinMaxScaler
from keras import Model
from keras.layers import Input, Dense, Dropout
from keras.layers import LSTM
from sklearn.metrics import mean_absolute_percentage_error

# 設定 plotly 繪圖結果顯示於瀏覽器
# 使用 Colab, Jupyter-notebook 不用設定此選項
import plotly.io as pio
pio.renderers.default='browser'

# matplotlib 中文字型 - 設定 matplotlib.rcParams 方法
# https://github.com/rwepa/ipas_bda/blob/main/ipas-python-program.py#L1488

from matplotlib import rcParams
rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 設定中文字型
rcParams['axes.unicode_minus'] = False # 設定負正確顯示

# 匯入資料

# 原參考資料使用 CSV檔案, 本例改為使用即時網路讀取黃金價格資料.
# 資料為紐約商業交易所黃金期貨ETF, 簡稱GC
# end參數為設定結束日期, 結果不包括參數日期, 本例結束日期不包括2023-12-15.

df = yf.download(tickers="GC=F", start="2013-01-01", end="2023-12-15")

# 理解財金指標使用的幣別
gold = yf.Ticker("GC=F") # Gold Futures on Yahoo Finance
gold.history_metadata # dict
print(gold.history_metadata['currency'])  # USD

# 資料檢視
# 2013-01-02 ~ 2023-12-14, 2756列*6行
df
"""
                   Open         High  ...    Adj Close  Volume
Date                                  ...                     
2013-01-02  1672.800049  1693.800049  ...  1687.900024      35
2013-01-03  1686.099976  1686.800049  ...  1673.699951     140
2013-01-04  1647.000000  1658.300049  ...  1648.099976     199
2013-01-07  1656.500000  1659.900024  ...  1645.500000      49
2013-01-08  1647.699951  1661.500000  ...  1661.500000      17
                ...          ...  ...          ...     ...
2023-12-08  2031.699951  2033.099976  ...  1998.300049     449
2023-12-11  2004.099976  2004.199951  ...  1978.000000     651
2023-12-12  1984.199951  1994.199951  ...  1977.800049      95
2023-12-13  1978.500000  2024.800049  ...  1982.300049    2252
2023-12-14  2024.699951  2040.099976  ...  2030.199951     236

[2756 rows x 6 columns]
"""

# 問題: 結果中顯示 ... 的資料值如何顯示?
# 分析:
# 方法1: 在 Spyder 右上角 [Variable Explorer] 中按滑鼠左鍵二下並顯示結果.
# 方法2: 參考RWEPA: https://github.com/rwepa/ipas_bda/blob/main/ipas-python-program.py#L588C18-L588C18

# pd.set_option('display.expand_frame_repr', False)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# 資料物件
# 使用 yfinance 模組
type(df)
# pandas.core.frame.DataFrame

# 行資料型態
df.dtypes
# Open         float64 開盤價
# High         float64 最高價
# Low          float64 最低價
# Close        float64 收盤價
# Adj Close    float64 調整後收盤價
# Volume         int64 總量
# dtype: object

# 索引值
df.index

# 欄位名稱
df.columns

# 資料值
df.values

# 資料訊息
df.info()

# 資料摘要
df.describe()
#               Open         High  ...    Adj Close         Volume
# count  2756.000000  2756.000000  ...  2756.000000    2756.000000
# mean   1481.493614  1488.631859  ...  1481.350580    5271.452467
# std     283.199025   284.775922  ...   283.265097   28908.758920
# min    1053.699951  1062.000000  ...  1050.800049       0.000000
# 25%    1251.000000  1255.800049  ...  1250.750031      46.000000
# 50%    1332.800049  1339.049988  ...  1332.400024     165.500000
# 75%    1777.925018  1787.024994  ...  1776.075012     523.500000
# max    2075.300049  2130.199951  ...  2071.000000  386334.000000

# count 個數
# mean  平均值
# std   標準差
# min   最小值
# 25%   25百分位數(Q1)
# 50%   50百分位數(Q2), 中位數
# 75%   75百分位數(Q3)
# max   最大值

# 資料處理

# 將 index 轉換為 Date 資料行
df['Date'] = df.index

# 將 Date 移至第1欄位置
df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

# 刪除 index 值
df = df.reset_index(drop=True)

# 檢查重複值
df.duplicated().sum()

# 檢查遺漏值
df.isnull().sum().sum()

# 匯出 Excel 檔案
df.to_excel("gold_price_2013_2023.xlsx", index=False)

# 圖1. GC價格走勢圖(2013-2013年)
# 以下程式一併選取並執行
fig = px.line(x=df['Date'], y=df['Close'])
fig.update_traces(line_color='black') 
fig.update_layout(xaxis_title="Date", 
                  yaxis_title="Close Price",
                  title={'text': "圖1. GC價格走勢圖(2013-2023年)", 'x':0.5, 'y':0.95,  'xanchor':'center', 'yanchor':'top'},
                  plot_bgcolor='rgba(255, 215, 0, 0.5)')

# 圖2. 黃金價格盒鬚圖

# 考量僅進行各種價格的盒鬚圖, 因此使用 drop 刪除沒有使用的日期, 成交量
# melt: 融化, 將寬資料轉換為長資料
# 使用 melt 目的為依照不同價格別繪製群組盒鬚圖

df_price = df.drop(['Date', 'Volume'], axis=1).melt(var_name="price_type")
df_price

fig = px.box(df_price, 
             y="value", 
             facet_col="price_type", 
             color="price_type",
             boxmode="overlay")
fig.update_layout(title={'text': "圖2. GC價格盒鬚圖(2013-2023年)", 'x':0.5, 'y':0.95,  'xanchor':'center', 'yanchor':'top'},
                  plot_bgcolor='rgba(255, 215, 0, 0.5)')

##############################
# 步驟 3：資料準備
##############################

# 將資料區分為訓練集與測試集
# 本例為時間序列資料, 資料不可以隨機抽取, 須保持原資料順序.
# 訓練集 train data: 2013-2022年
# 測試集  test data: 2023年

test_size = df[df.Date.dt.year==2023].shape[0]
test_size # 241
train_size = df.shape[0] - test_size
train_size # 2515

train_list = ['train']*train_size
test_list = ['test']*test_size
split_list = train_list + test_list

# 新增 split 欄位以區分資料為訓練集或測試集
df['split'] = split_list

df.head()
df.tail()

# 訓練集與測試集黃金價格統計圖
fig = px.line(df, x="Date", y="Close", color='split')
fig.update_layout(xaxis_title="Date", 
                  yaxis_title="Close Price",
                  title={'text': "圖3. GC價格走勢圖(2013-2013年)區分訓練集與測試集", 
                         'x':0.5, 
                         'y':0.95, 
                         'xanchor':'center', 
                         'yanchor':'top'},
                  plot_bgcolor='rgba(255, 215, 0, 0.5)')

# 使用 MinMaxScaler 來縮放價格以避免密集計算(intensive computations)
# MinMaxScaler 預設將資料轉換為 [0, 1]
scaler = MinMaxScaler()

# 
# reshape(-1,1) 表示將維度改為電腦自動排列列數(-1)與1行資料, 即 reshape(列, 行)
scaler.fit(df.Close.values.reshape(-1,1))

# 建立滑動視窗(sliding window)
# 滑動視窗表示使用先前的時間序列資料來預測下一期的時間序列資料.

# 滑動視窗範例
# 考慮連續讀取2週資料, 即{1,2週}, {2,3週}, {3,4週}...
# window width(視窗寬度) = 14, 其中 Stride(步伐) = 7.

# 本研究視窗寬度設為 60, X_train 和 X_test 將是包含 60 個時間戳的收盤價list.
window_size = 60

# 原始訓練集
train_data = df.Close[:-test_size]

# 原始訓練集-資料轉換至 [0, 1]
train_data = scaler.transform(train_data.values.reshape(-1,1))

# 建立空的串列 (list)
X_train = []
y_train = []

# 使用"滑動視窗"建立訓練集
for i in range(window_size, len(train_data)):
    X_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])

# 檢視指標為0資料
X_train[0]
y_train[0]

# 原始測試集
test_data = df.Close[-test_size-60:]

# 原始測試集-資料轉換至 [0, 1]
test_data = scaler.transform(test_data.values.reshape(-1,1))

# 建立空的串列 (list)
X_test = []
y_test = []

# 使用"滑動視窗"建立測試集
for i in range(window_size, len(test_data)):
    X_test.append(test_data[i-60:i, 0])
    y_test.append(test_data[i, 0])

X_test[0]
y_test[0]

# 將巢狀串列(nested lists) 轉換為 Numpy Arrays, 以利 tensorflow 操作.
X_train = np.array(X_train) 
X_test  = np.array(X_test)  
y_train = np.array(y_train)
y_test  = np.array(y_test)

# 轉換前維度
X_train.shape # (2455, 60)
y_train.shape # (2455,)
X_test.shape  # (241, 60)
y_test.shape  # (241,)

# 維度轉換
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test  = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
y_train = np.reshape(y_train, (-1,1))
y_test  = np.reshape(y_test, (-1,1))

# 轉換後維度
print('X_train Shape: ', X_train.shape) # (2455, 60, 1)
print('y_train Shape: ', y_train.shape) # (2455, 1)
print('X_test Shape:  ', X_test.shape)  # (241, 60, 1)
print('y_test Shape:  ', y_test.shape)  # (241, 1)

##############################
# 步驟 4：建立模型
##############################

# LSTM 定義
def define_model():
    input1 = Input(shape=(window_size,1))
    x = LSTM(units = 64, return_sequences=True)(input1)  
    x = Dropout(0.2)(x)
    x = LSTM(units = 64, return_sequences=True)(x)
    x = Dropout(0.2)(x)
    x = LSTM(units = 64)(x)
    x = Dropout(0.2)(x)
    x = Dense(32, activation='softmax')(x)
    dnn_output = Dense(1)(x)
    model = Model(inputs=input1, outputs=[dnn_output])
    model.compile(loss='mean_squared_error', optimizer='Nadam')  
    return model

# 建立LSTM模型
model = define_model()

# 模型摘要
model.summary()

# 模型訓練, 須一些時間...
history = model.fit(X_train, 
                    y_train, 
                    epochs=150, 
                    batch_size=32, 
                    validation_split=0.1, 
                    verbose=1)

##############################
# 步驟 5：建立評估與測試
##############################

# 模型評估
result = model.evaluate(X_test, y_test)

# 模型預測
y_pred = model.predict(X_test) 

# MAPE (Mean Absolute Percentage Error) 平均絕對百分比誤差率
MAPE = mean_absolute_percentage_error(y_test, y_pred)

# 正確率
Accuracy = 1 - MAPE

# 顯示評估結果
print("Test Loss:", result)
print("Test MAPE:", MAPE)         # 2.4%
print("Test Accuracy:", Accuracy) # 97.6%

# 測試集評估結果的視覺化

# 轉換原刻度單位
y_test_true = scaler.inverse_transform(y_test)
y_test_pred = scaler.inverse_transform(y_pred)

# 使用 matplotlib 繪圖

# 設定繪圖區域
plt.figure(figsize=(15, 6), dpi=150)

# 設定繪圖區域顏色
plt.rcParams['axes.facecolor'] = '#FFD700'

# train data
plt.plot(df['Date'].iloc[:-test_size], scaler.inverse_transform(train_data), color='black', lw=2)

# actual test data
plt.plot(df['Date'].iloc[-test_size:], y_test_true, color='blue', lw=2)

# predicted test data
plt.plot(df['Date'].iloc[-test_size:], y_test_pred, color='red', lw=2)

# 主標題
plt.title('圖4. Model Performance on Gold Price Prediction', fontsize=15)

# X軸標題
plt.xlabel('Date', fontsize=12)

# Y軸標題
plt.ylabel('Price', fontsize=12)

# 圖例
plt.legend(['Training Data', 'Actual Test Data', 'Predicted Test Data'], loc='upper left', prop={'size': 15})

# 格線顏色
plt.grid(color='white')

# 結論: 
# 本例使用 LSTM 模型進行黃金價格預測, 執行結果佳.
# 🏆 Loss: 0.001
# 🏆 Accuracy: 96%

##############################
# 步驟 6：佈署應用
##############################
# 儲存模型
# 使用 Streamlit 建立互動式視覺化
# 改善線上執行效能
# 將此模型套用至工作資料集

##############################
# 3.3 台灣股市,ETF下載
##############################

# 台灣ETF列表
# https://www.stockq.org/etf/

import yfinance as yf
import plotly.graph_objects as go

# 設定 plotly 繪圖結果顯示於瀏覽器
# 使用 Colab, Jupyter-notebook 不用設定此選項
import plotly.io as pio
pio.renderers.default='browser'

# https://pypi.org/project/mplfinance/

# 上市: 台積電 '2330.TW'
# 上櫃: 崇友 '4506.TWO'
# ETF: '0050.TW'
# ETF: '0056.TW'
# ETF: '00878.TW'

# 擷取 元大台灣50ETF, 開始/結束資料
df = yf.download('0050.TW', start = '2008-10-03', end = '2023-12-31')
df

# 擷取 元大台灣50 ETF, 最近期間/頻率資料, 近7天(包括系統日期), 每隔1分鐘資料
df = yf.download('0050.TW', period = '7d', interval = '1m')
df

# 建立財金資料擷取函數, 名稱為 getData
def getData(symbol, startDate, endDate):
    
    # 擷取財金資料
    data = yf.download(tickers = symbol, start = startDate, end = endDate)
    
    # 將 index 轉換為 Date 資料行
    data['Date'] = data.index

    # 將 Date 移至第1欄位置
    data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    # 刪除 index 值
    data = data.reset_index(drop=True)
    
    # 回傳財金資料
    return data

# 使用自訂函數 getData 擷取資料
df = getData('0050.TW', '2023-10-01', '2023-12-31')
df

# 使用 plotly 模組繪製 K 線圖, 預設值綠色表示上漲, 紅色表示下趺.
# K線圖採用歐美標準,  綠色表示上漲(收盤價高於開盤價), 紅色表示下趺(收盤價低於開盤價)
# 台灣等亞洲一般使用: 紅色表示上漲(收盤價高於開盤價), 綠色表示下趺(收盤價低於開盤價)

# K線（英語：Candlestick chart）又稱陰陽燭、蠟燭線.
# https://zh.wikipedia.org/wiki/K线

fig = go.Figure(data = [go.Candlestick(x=df['Date'],
                open = df['Open'],
                high = df['High'],
                low = df['Low'],
                close = df['Close'],
                increasing_line_color = '#FF4136', # 設定上漲為紅色
                decreasing_line_color = '#3D9970'  # 
                )])
# fig.update_layout(xaxis_rangeslider_visible=False)
fig.update_layout(xaxis_rangeslider_visible=False,  # 取消成交量繪圖
                  xaxis_title="日期",               # 設定X軸標題
                  yaxis_title="收盤價",             # 設定Y軸標題
                  title={'text':'○○○收盤價走勢圖', 'x':0.5, 'y':0.95,  'xanchor':'center', 'yanchor':'top'})


# 進出場流程
# 1. 選擇交易標的
# 2. 進場判斷
# 3. 出1場判斷

# 交易策略
# 1. 選擇交易標的: 考慮 0050
# 2. 進場判斷: 當天K線是紅K,並且下引線是實體紅K的2倍.
# 3. 出場判斷: 最少持有時間為3日, 3日過後只要當日紅K則出場.
# 參考資料: Python：股票×ETF量化交易實戰105個活用技巧, 劉承彥著, 博碩文化.
# end


