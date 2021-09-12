# Topic  : Data mining - association rules and apriori algorithm
# Author : Ming-Chang Lee
# Date   : 2009.03.29

# table 5.1, Transactional data, Han and Kamber (2006) p.236
# items   : I1 I2 I3 I4 I5
# dataset: total data = 9
# Transaction ID  Items
# T100            {I1,I2,I5), 
# T200            {I2,I4}, 
# T300            {I2,I3}, 
# T400            {I1,I2,I4}, 
# T500            {I1,I3}, 
# T600            {I2,I3}, 
# T700            {I1,I3}, 
# T800            {I1,I2,I3,I5}, 
# T900            {I1,I2,I3}

# step 1.
# load "arules" package
library(arules)

# step 2.
# prepare data
a_list <- list(
      c("I1","I2","I5"),
      c("I2","I4"),
      c("I2","I3"),
      c("I1","I2","I4"),
      c("I1","I3"),
      c("I2","I3"),
      c("I1","I3"),
      c("I1","I2","I3","I5"),
      c("I1","I2","I3")
      )

# set transaction names
names(a_list) <- paste("T",c(1:9), "00", sep = "")
a_list

# force data into transactions
table5_1 <- as(a_list, "transactions") # Force an Object to Belong to a Class >as (Object, Class)
table5_1

# step 3.
# analyze data
# generate level plots to visually inspect binary incidence matrices
image(table5_1) # result- Figure 1 Level plot
summary(table5_1)

# step 4.
# find 1-items (L1)
# provides the generic function itemFrequency and the frequency/support for all single items in an objects based on itemMatrix.
itemFrequency(table5_1, type = "relative") # default: "relative"
itemFrequency(table5_1, type = "absolute") # same as the textbook

# step 5.
# create an item frequency bar plot for inspecting the item frequency distribution for objects based on itemMatrix
itemFrequencyPlot(table5_1) # result- Figure 2 Item frequency bar plot

# step 6.
# mine association rules
# rules <- apriori(table5_1, parameter = list(supp = 0.5, conf = 0.9, target = "rules"))
rules<- apriori(table5_1) # Mine frequent itemsets, association rules or association hyperedges using the Apriori algorithm

# step7.
# display results
inspect(table5_1) # display transactions
inspect(rules) # display association

# reference:
# Han, J. and Kamber, M., Data Mining: Concepts and Techniques, Second Edition, Morgan Kaufmann, (2006).
# http://r-forge.r-project.org/projects/arules
# end
