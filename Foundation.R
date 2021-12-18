# Topic:  Using R - Foundation
# Author: MING-CHANG LEE, Department of Information Management, Yu Da University
# Date:   September 18, 2010
# Email:  alan9956@ydu.edu.tw
# Web:    http://web.ydu.edu.tw/~alan9956/

# p.8
# Simple examples: hist, plot
x <- c(1:100)
y <- rnorm(100)*100
hist(y)
test.model <- lm(y ~ x)
test.model
plot(x,y)
library(help="graphics")
# On-line help
? rnorm
? plot
# Information on package 'base'
library(help="base")
# model and length function

# p.10
x <- c(1:2)
mode (x)
length(x)

# p.11
# Name of object
A <- 'WEPA'; compar <- TRUE; z <- 3+4i
mode(A); mode(compar); mode(z)

# p.12
# non-finite numeric values
x <- 5/0
x
exp(x)
exp(-x)
x - x

# p.15
# Joining (concatenating) vectors - c
x <- c(2,3,5,2,7,1)
x
y <- c(10,15,12)
y
z <- c(x, y)
z

# p.16
# Specify the numbers of the elements that are to be extracted:
x <- c(3,11,8,15,12) # Assign to x the values 3, 11, 8, 15, 12
x[c(2,4)] # Extract elements (rows) 2 and 4
# Use negative numbers to omit elements:
x[-c(2,3)]
x>10 # This generates a vector of logical (T or F)
x[x>10]
# vectors have named elements:
c(ALAN=100, SERENA=2000, ANDY=300, ALPHA=400)[c("ALAN","ANDY")]

# p.17
# Regular sequences: seq, scan
x1 <- 1:100
x2 <- 100:1
x3 <- seq(1,10, 0.5)
x4 <- seq(length=9, from=1, to=5)
x5 <- c(1,2,2.5,6,10)
x6 <- scan()

# p.18
# Regular sequences : rep, sequence
rep(1,30)
sequence(5)
sequence(c(5,2))
sequence(c(5,9))

# p.20
# Generate levels (factors): gl
gl(3, 5)
gl(3, 5, length=30)
gl(2, 6, label=c("Male", "Female"))
# TRY !
x <- gl(3, 3, label=c("Àu¨}", "´¶³q", "¥[ªo"), length=27)
x
class(x)

# p.22
# Generate data frame: expand.grid
x <- expand.grid(h=c(160, 165, 170), w=c(50, 60), sex=c("M", "F"))
print(x)
class(x)

# p.23
# Constants
x <- LETTERS
y <- x[-c(2:10)]
length(x)
length(y)
z <- month.name
z

# p.24
# Missing values - NA
x <- c(pi, 1, 2)
x
x[2] <- NA
x
is.na(x[2])
is.na(x[1])
# To replace all NAs by 0
x[is.na(x)] <- 0
x

# p.26
# Creating objects: list
data()  # list all available data sets
cars
pts <- list(x=cars[,1], y=cars[,2])
plot(pts)

# p.27
# Creating objects: vector
x <- vector(mode="numeric", length=1000000)
is.vector(x)
x <- c("Taiwan", "China", "USA")
is.vector(x)

# p.29
# Creating objects: factor
factor(1:3)
factor(1:3, levels=1:5)
factor(1:3, labels=c("A", "B", "C"))
x <- factor(letters[1:6], label="YDU")
x
class(x)

# p.30
# Creating objects: arrary
x <- array(letters)
class(x)
dim(x)

# p.31
x <- array(letters)
class(x)
dim(x)
x <- array(1:3, c(2,4))
x
dim(x)
length(x)
x[1, ] # select row 1

# p.33
# Creating objects: matrix
matrix.data <- matrix(c(1,2,3,4,5,6), nrow=2,	ncol=3,	byrow=TRUE,	dimnames=
list(c("row1", "row2"), c("C1", "C2",	"C3")))
matrix.data

# p.35
# Creating objects: data.frame
x <- 1:4; n <- 10; M <- c(10, 35); y <- 2:4
data.frame(x, n)
data.frame(x, M)

# TRY !
data.frame(x, y) # Error !!!

z <- data.frame(var1= rnorm(5), var2=LETTERS[1:5])
z

# p.36
data(cars)
help(cars)
class(cars)

# TRY ! How to add row names (e.g., Row1, Row2,¡K) 
# Answer: x <- data.frame(cars, row.names=factor(c(1:nrow(cars)), label="Row"))

# p.37
# Import/Export Data
# Create a file: r_input.txt
# Create a data directory C:\Program Files\R\R-2.3.1\data
# Set working directory
workpath <- "C:/Program Files/R/R-2.3.1/data"
setwd(workpath)
# Get working directory
getwd()
# Create a text file C:\Program Files\R\R-2.3.1\data\r_input.txt
# Import dataset
score1 <- read.table(file="r_input.txt", header= TRUE)
score1
# Add new column data for mid_term
mid_term <- matrix(c(60,80,65,85,80,90,99), nrow=7, ncol=1, byrow=FALSE, 
dimnames= list(c(),c("mid_term")))
mid_term
# Merge two data.frame( score1 and mid_term)
score2 <- data.frame(score1, mid_term)
score2
# Export dataset
write.table(score2 , file= "r_output.txt", sep = "\t", append=FALSE, row.names= 
FALSE, col.names = TRUE, quote= FALSE)

# p.43
# Descriptive Statistics
summary(score2)
score2[2]
score2$Quiz1
quiz1 <- score2$Quiz1
mean(quiz1)
max(quiz1)
min(quiz1)
std(quiz1) # error function
# solution 1
sqrt( sum( (quiz1 - mean(quiz1))^2 /(length(quiz1)-1))) # std=10.80123
# solution 2
std = function(x) sqrt(var(x))
std(quiz1) # same as solution 1 # TRY sd(quiz1)

# p.44
# Demo for plot
# demo(graphics)

# p.49
# Example: plot
data()
data(cars) #Speed and Stopping Distances of Cars
plot(cars) # x-axis:speed; y-axis: dist
plot(cars$dist, cars$speed)
plot(cars, type="b")
# p.50
plot(cars, type="b",pch=5,col="red",xlab="Speed(mph)", ylab="Stop distance(ft)", 
main="Speed and Stopping Distances of Cars",sub= "Figure 1: Plotting demonstration")

# p.51
# Bar charts ¡Vbarplot()
CarArrived <- table(NumberOfCar <- rpois(100, lambda=5))
CarArrived
barplot(CarArrived)
barplot(CarArrived, col=rainbow(14))

# p.52
# Pie charts ¡Vpie()
pie.sales <- c(0.14, 0.30, 0.26, 0.15, 0.10, 0.05) # Sales ratio
names(pie.sales) <- c("Taipei1", "Taipei2", "Taipei3", "Taichung", 
"Kao", "Other") # Sales area
pie(pie.sales) # default colours
pie(pie.sales, col = c("purple", "violetred1", "green3", "cornsilk", 	"cyan", "white")) # set colour
pie(pie.sales, density = 10, clockwise=TRUE) # The density of shading lines

# p.53
# Box-and-whisker Plot ¡Vboxplot()
mat <- cbind(Uni05 = (1:100)/21, Norm = rnorm(100), T5 = rt(100, df 	= 5), Gam2 = rgamma(100, shape = 2))
boxplot(data.frame(mat), main = "boxplot")

# p.54
# Stem-and-Leaf Plot ¡Vstem()
mat = scan()
# 2 3 16 23 14 12 4 13 2 0 0 0 6 28 31 14 4 8 2 5
stem(mat)
# End of file
