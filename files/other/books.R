# This file performs all the analysis on the book data which
# should be stored in a CSV file with these headers:
#    - Year (YYYY)
#    - Start (DD/MM/YY)
#    - End (DD/MM/YY)
#    - Title
#    - Authors (seperated by "and")
#    - Length (pages)
#    - Speed (pages per day)


# load data into memory
data = read.csv("../data/books.csv", header = TRUE)


# comparative boxplots of book lengths
png(filename='book-lengths.png', width=500, height=500, res=90)
boxplot(Length ~ Year, data=data,
        main="Boxplot of Book Lengths by Year",
        xlab="Year",
        ylab="Length in Pages")


# refine to information about the current year
year = as.numeric(tail(data$Year, n=1))
yearDat = subset(data, Year == year)

# book data analysis
cat("Total books", dim(yearDat)[1], "\n")
cat("Total pages", sum(yearDat$Length), "\n")
cat("Mean pages", mean(yearDat$Length), "\n")

# author data analysis
authors = unique(yearDat$Authors)
cat("Total authors", length(authors), "\n")
authFreq = tabulate(match(yearDat$Authors, authors))
mra = toString(authors[which.max(authFreq)])
cat("Most read author is", mra, "\n")
