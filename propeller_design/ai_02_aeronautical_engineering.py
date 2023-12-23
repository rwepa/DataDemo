# file     : ai_02_aeronautical_engineering.py
# title    : 2.AI與螺旋槳性能最佳化應用
# author   : Ming-Chang Lee
# date     : 2023.12.28
# YouTube  : https://www.youtube.com/@alan9956
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Email    : alan9956@gmail.com

# 大綱
# 2.1 螺旋槳資料集簡介
# 2.2 螺旋槳資料集下載
# 2.3 安裝模組
# 2.4 載入模組
# 2.5 匯入螺旋槳資料集
# 2.6 計算 solidity
# 2.7 資料視覺化
# 2.8 Solidity 遺漏值, 使用 KNN 填補法

##############################
# 2.1 螺旋槳資料集簡介
##############################

# UIUC螺旋槳資料集: UIUC小型無人機和模型飛機上使用的螺旋槳的風洞測量
# UIUC: 伊利諾大學厄巴納－香檳分校（University of Illinois Urbana-Champaign）

##############################
# 2.2 螺旋槳資料集下載
##############################

# UIUC螺旋槳資料集下載(Kaggle)
# https://www.kaggle.com/datasets/heitornunes/uiuc-propeller-database/

# 參考資料 - CT Prediction | XGBoost
# https://www.kaggle.com/code/heitornunes/ct-prediction-xgboost

# 研究目標: 建立一個小型螺旋槳的性能模型, 了解其一些特性和飛行條件.

# 螺旋槳的性能可以透過三個參數來衡量：
# (1).推力係數(Thrust Coefficient)
# (2).功率係數(Power Coefficient)
# (3).效率(Efficiency)
 
# 參數取決於葉片幾何形狀(Blade Geometry)、雷諾數(Reynolds Number)和進距比(Advance Ratio)等，本篇文章以推力係數為主。
# 
# 資料集：包括實驗資料集、幾何資料集，每個資料集有3種不同版本的資料，合計檔案有6個。

# UIUC螺旋槳資料集下載(RWEPA GitHub)
# https://github.com/rwepa/DataDemo/tree/master/propeller_design
 
# 一、實驗資料集（Experiment Data Set Features）

# 11個變數
# PropName: Propeller's Name.    螺旋槳的名稱
# BladeName: Blade's Name.       葉片的名稱
# Family: Propeller's Brand.     螺旋槳品牌
# B: Number of Blades.           葉片數量
# D: Propeller's Diameter.       螺旋槳直徑
# P: Propeller's Pitch.          螺旋槳的螺距
# J: Advanced Ratio Input.       進階比率輸入
# N: RPM Rotation Input. RPM     旋轉輸入
# CT: Thrust Coefficient Output. 推力係數輸出 --> 反應變數
# CP: Power Coefficient Output.  輸出功率係數
# eta: Efficiency Output.        效率輸出

# 二、幾何資料集（Blade Geometry Data Set Features）
 
# PropName: Propeller's Name.       螺旋槳的名稱
# BladeName: Blade's Name.          葉片的名稱
# Family: Propeller's Brand.        螺旋槳品牌
# D: Propeller's Diameter.          螺旋槳直徑
# P: Propeller's Pitch.             螺旋槳的螺距
# r/R: Adimensional Radius.         維度半徑
# c/R: Adimensional Chord.          維度和弦
# beta: Angle Relative to Rotation. 相對於旋轉的角度

##############################
# 2.3 安裝模組
##############################

# The missingno provides a small toolset of flexible and easy-to-use missing data visualizations and utilities that allows you to get a quick visual summary of the completeness (or lack thereof) of your dataset.
# https://github.com/ResidentMario/missingno

# pip install missingno

# pandas, matplotlib, numpy scipy, seaborn, sklearn 已經內建於 Anaconda.

##############################
# 2.4 載入模組
##############################

import pandas as pd
import matplotlib.pyplot as plt
import missingno as msgno
import numpy as np
from scipy.integrate import trapz
import seaborn as sns
from sklearn.impute import KNNImputer

##############################
# 2.5 匯入螺旋槳資料集
##############################

exp1_url = 'https://raw.githubusercontent.com/rwepa/DataDemo/master/propeller_design/volume1_exp.csv'
exp2_url = 'https://raw.githubusercontent.com/rwepa/DataDemo/master/propeller_design/volume2_exp.csv'
exp3_url = 'https://raw.githubusercontent.com/rwepa/DataDemo/master/propeller_design/volume3_exp.csv'

geom1_url = 'https://raw.githubusercontent.com/rwepa/DataDemo/master/propeller_design/volume1_geom.csv'
geom2_url = 'https://raw.githubusercontent.com/rwepa/DataDemo/master/propeller_design/volume2_geom.csv'
geom3_url = 'https://raw.githubusercontent.com/rwepa/DataDemo/master/propeller_design/volume3_geom.csv'


exp1 = pd.read_csv(exp1_url)
exp2 = pd.read_csv(exp2_url)
exp3 = pd.read_csv(exp3_url)

geom1 = pd.read_csv(geom1_url)
geom2 = pd.read_csv(geom2_url)
geom3 = pd.read_csv(geom3_url)

# 合併為一個資料框
data = pd.concat([exp1, exp2, exp3], ignore_index=True) # 27495*11
geom = pd.concat([geom1, geom2, geom3], ignore_index=True) # 2316*7

data # [27495 rows x 11 columns]
geom # [2316 rows x 7 columns]

# 資料摘要
tmp = data.describe(include='all')
print(tmp)

tmp = geom.describe()
print(tmp)

# 資料型態
data.dtypes
geom.dtypes

##############################
# 2.6 計算 solidity
##############################

props = data['PropName'].value_counts().index

solidity = pd.DataFrame(columns=['PropName', 'Solidity']) # 建立空的 solidity 資料框

line = ['PropName', 'BladeName', 'Family', 'B', 'D', 'P']

for prop in props:
    
    # 篩選 PropName
    # prop = props[0]
    df_line = data.loc[data['PropName'] == prop, line].drop_duplicates()
    
    # 取出 BladeName 值
    bn = df_line.loc[:, 'BladeName'].item()
    
    # 取出 b 值
    b = df_line.loc[:, 'B'].item()
    
    # 取出 d 值
    d = df_line.loc[:, 'D'].item()
    
    # 從 geom 資料集找出對應 BladeName
    mask = geom['BladeName'] == bn
    
    if mask.sum() == 0:
        continue
    
    df_geom = geom.loc[mask, :]
    
    c = df_geom['c/R'].to_numpy() * d * 0.5
    r = df_geom['r/R'].to_numpy() * d * 0.5
    I = trapz(c, r) # 定積分梯形法則 numpy.trapz(y, x)
    
    sol = np.round(4 * b * I /(d ** 2 * np.pi), 5)
    
    # solidity = solidity.append({'PropName': prop, 'Solidity': sol}, ignore_index=True)
    # pandas.append 方法不再使用
    solidity = pd.concat([solidity, pd.DataFrame({'PropName': [prop], 'Solidity': [sol]})],  ignore_index=True)

# 疏密比(Solidity)
solidity

# 疏密比資料摘要
solidity.describe()

# 合併疏密比
data = data.merge(solidity, how = 'left', on = 'PropName')
data

# 欄位名稱
data.columns

# Solidity 有遺漏值
data.describe(include='all')

##############################
# 2.7 資料視覺化
##############################

# 白色表示NA
# 右側的迷你圖提供資料完整性的形狀，並指出了資料集具有非空值的最大行數和最小行數。
msgno.matrix(data)

# 建立新的變數"螺距比" pitch ratio (P/D)
data['P/D'] = np.round(data['P']/data['D'], 3)

# 匯出 Excel 檔案
data.to_excel("data_6_files.xlsx", index=False)

# 依據 P/D 和 Solidity 群組, 繪製 J vs. CT 散佈圖並理解資料特性.
for i, fam in enumerate(data['Family'].value_counts().index):
    
    # 先忽略 ancf 螺旋槳品牌
    if fam == 'ancf':
        continue
    
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    ax[0].set_title(fam + ' - P/D effect')
    ax[1].set_title(fam + ' - Solidity effect')
    mask1 = data['Family'] == fam
    data_aux = data.loc[mask1, :]
    sns.scatterplot(data=data_aux, x='J', y='CT', hue = 'P/D', ax=ax[0])
    sns.scatterplot(data=data_aux, x='J', y='CT', hue = 'Solidity', ax=ax[1])
    ax[0].grid(False)
    ax[1].grid(False)
    fig.tight_layout()
    myfile = str(i) + '_' + fam + '_scatter.png'
    plt.savefig(myfile) # 輸出繪圖結果
    
    # i值大於15時,停止繪圖
    if i > 15:
        break

# 相關係數圖-所有變數
data_corr = data[['B', 'D', 'P', 'P/D', 'Solidity', 'J', 'N', 'CT', 'CP', 'eta']]
data_corr

# 相關係數圖-所有變數-視覺化
# Solidity 與 D 和 P 具有高度負相關, 可以使用此關係建立插補遺漏值.
plt.figure(figsize=(12, 6))
sns.heatmap(data_corr.corr('spearman'), center=0, fmt='.2f', annot=True)

# 相關係數圖-篩選重要變數
props = data.drop(['PropName', 'BladeName', 'Family', 'J', 'N', 'CT', 'CP', 'eta'], axis=1).drop_duplicates().reset_index(drop=True)
props

# 相關係數圖-篩選重要變數-視覺化
sns.heatmap(props.corr(), center=0, fmt='.2f', annot=True)

##############################
# 2.8 Solidity 遺漏值, 使用 KNN 填補法
##############################

# Solidity 變數有遺漏值, 其他變數沒有遺漏值.
data.isnull().sum(axis = 0)

# B 欄位(葉片數量)只有 3個值 [2,3,4] 差異較少, 因此填補 Solidity 欄位先考慮 'D', 'P' 二個變數
data['B'].unique()

# 先取出已知欄位: D, P, 與填補欄位 Solidity
X_imp = data.loc[:, ['D', 'P', 'Solidity']]
X_imp

# 觀念說明: sklearn.impute.KNNImputer.fit vs. sklearn.impute.KNNImputer.fit_transform
# 將資料進行標準化, 使其轉換後之平均值為零且標準差為1, 計算式為 x′=(x−μ)/σ.
# 上述訓練集進行標準化後, 測試集亦須使用相同的μ與σ進行標準化.
# fit: 計算 μ, σ
# fit_transform: 先使用 fit 計算 μ, σ, 應用於 test dataset 時, 再使用 transform 進行資料轉換.

# 使用 KNNImputer 進行遺漏值填補法 (K近鄰法)
imp = KNNImputer(n_neighbors=5)

# 實際進行填補, 完成後將 array 轉換為 DataFrame, 須一些時間...
df = pd.DataFrame(imp.fit_transform(X_imp), columns = ['D', 'P', 'Solidity'])
df

# Solidity 變數已經沒有遺漏值
df.isnull().sum(axis = 0)

# 將填補完成的 Solidity 值填入原 dat.
data.loc[:,'Solidity'] = df['Solidity']
data

# 所有欄位皆無遺漏值
data.isnull().sum(axis = 0)

# 資料型態
data.dtypes

# 資料摘要
data.describe(include='all')

# 計算 B 群組個數
data.groupby(['B'])['B'].count()
# B
# 2    26615
# 3      501
# 4      379

# 計算 B 群組比例
data.groupby(['B'])['B'].count()/len(data.index)
# B
# 2    0.967994
# 3    0.018221
# 4    0.013784
# end
