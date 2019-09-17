# title: R connect to MySQL
# date: 2012.12.21
# author: Ming-Chang Lee

library(RMySQL)
con <- dbConnect(MySQL(), user="root", password="123456", dbname="school", host="localhost")
dbListTables(con)
dbListFields(con, "stdscore")
data.all <- dbReadTable(con, "stdscore")
class(data.all)
data.all
data.select <- dbGetQuery(con, "select * from stdscore where courseno='MS1038'")
data.select
summary(MySQL(), verbose = TRUE)
summary(con, verbose = TRUE)
summary(data.all, verbose = TRUE)
dbListConnections(MySQL())
dbDisconnect(con)
# end
