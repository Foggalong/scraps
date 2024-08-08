# R code which demonstrated filtering a dataframe
# based on some bound criteria using dummy data.

# GENERATING DUMMY DATA
# dummy data of length
n = 40;
# write to this file
sink("data.csv")
# add the headers you have
cat("id,frame,x,y,uncert_xy\n")
# create the data rows of the CSV fiel
for (i in 1:n) {
    # random integer from 1 to n/10 for col 2
    c2 = ceiling(runif(1,0,n/10));
    # uniform(0,1) randoms for cols 1, 3, 4, and 5
    cat(runif(1),c2,runif(1),runif(1),runif(1), sep=",")
    # makes sure a newline is started
    cat("\n")
}
# finish writing to file
sink()

# FILTERING DESIRED VALUES
# read data from CSV
dat = read.csv("data.csv", header=TRUE)
# filter data frame to ones with 2nd col value 1 or 2
dat[((dat$frame > 0) & (dat$frame <= 2)),]
