# import data
gfc <- read.table("gfc.csv", header=TRUE, sep=",")
gfc
str(gfc)
summary(gfc)
plot(gfc$amount, type="l")
# end
