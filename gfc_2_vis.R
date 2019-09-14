# title    : gfc 資料人集視覺化應用
# date     : 2019.9.14
# author   : Ming-Chang Lee
# email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# Encoding : UTF-8

gfc <- read.table("gfc-ansi.csv", header=TRUE, sep=",")
gfc

# plot 繪圖
plot(gfc$amount)
plot(gfc$amount, type="l")
str(gfc)
summary(gfc)

gfc.日亞 <- gfc[gfc$supplier == "日亞",] # ==表示條件式判斷
gfc.廣達 <- gfc[gfc$supplier == "廣達",]
gfc.科銳 <- gfc[gfc$supplier == "科銳",]

# case 1
plot(gfc.日亞$amount, type="l")
lines(gfc.廣達$amount)
lines(gfc.科銳$amount)

# case 2
plot(gfc.日亞$amount, type="l", ylim=c(50,350))
lines(gfc.廣達$amount)
lines(gfc.科銳$amount)

# case 3
plot(gfc.日亞$amount, type="l", ylim=c(50,350))
lines(gfc.廣達$amount, col="red")
lines(gfc.科銳$amount, col="blue")

# case 4
plot(gfc.日亞$amount, type="l", ylim=c(50,350), 
        xlab="時間", 
        ylab="訂購量", 
        main="XX公司2009年訂購量統計圖",
        axes=F,
        cex=0.5)
lines(gfc.廣達$amount, col="red", lty=2)
lines(gfc.科銳$amount, col="blue", lty=3)

ind <- round(seq(1, nrow(gfc.日亞), length.out=12))
axis(1, at=ind, labels=gfc.日亞 $orderdate[ind])
axis(2)
box()

legend("topright", legend = c("日亞", "廣達", "科銳"), lty=1:3, col=c(1,2,4), cex=0.8)
abline(h=mean(gfc.日亞$amount))
abline(h=mean(gfc.廣達$amount), col="red")
# 圖中有找到樣式 patterns?
# end
