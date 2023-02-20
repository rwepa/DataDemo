# File     : roc_r_example.R
# Title    : An example of R for ROC curve
# Author   : Ming-Chang Lee
# Date     : 2005.11.25
# YouTube  : https://www.youtube.com/@alan9956
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Email    : alan9956@gmail.com

library(ROCR)

# 線上說明
?ROCR.hiv

# 附加 ROCR.hiv 資料集
data(ROCR.hiv)
attach(ROCR.hiv)

# SVM - 建立 prediction 物件
pred.svm <- prediction(hiv.svm$predictions, hiv.svm$labels)

# SVM - 建立 performance 物件
perf.svm <- performance(pred.svm, 'tpr', 'fpr')

# NN - 建立 prediction 物件
pred.nn <- prediction(hiv.nn$predictions, hiv.svm$labels)

# NN - 建立 performance 物件
perf.nn <- performance(pred.nn, 'tpr', 'fpr')

# 繪圖 ROC curve
plot(perf.svm, lty=3, col="red", main="SVMs and NNs for prediction of HIV-1 coreceptor usage")

plot(perf.nn, lty=3, col="blue", add=TRUE)

plot(perf.svm, avg="vertical", lwd=3, col="red", spread.estimate="stderror", plotCI.lwd=2, add=TRUE)

plot(perf.nn, avg="vertical", lwd=3, col="blue", spread.estimate="stderror", plotCI.lwd=2, add=TRUE)

# 圖例
legend(0.7, 0.7, c('SVM','NN'), col=c('red','blue'), lwd=3)
# end
