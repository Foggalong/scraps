#!/usr/bin/env Rscript

data_location = "./data.csv"

# returns true of n is an integer, false otherwise
# isInt = function(n) { n%%1 == 0 }


addEntry = function() {
    # prompts the user to input a new set of pace data km by km
    # and writes this data to the CSV data file.

    data <- read.csv(file=data_location, header=TRUE, sep=',')

    # run date is used a column header
    date <- readline(prompt=cat("Enter date: "));
    # first row is distance
    dist <- readline(prompt=cat("Enter distance: "));

    cat("\nYou will now be prompted to enter the pace data for each\n")
    cat("kilometre in turn. Enter 0 minutes and 0 seconds to end\n")
    cat("this process.\n\n")

    paces = c()  # array for storing input paces
    km    = 0    # run kilometre count

    # continute prompting input until user enters (0,0)
    while (TRUE) {
        km = km + 1;
        min <- readline(prompt=cat("Enter km", km, "mins: "));
        sec <- readline(prompt=cat("Enter km", km, "secs: "));

        # check for ending input and if so reverse previous km increase
        if (identical(c(min,sec), c("0","0"))) { km = km - 1; break; }

        # TODO: implement input checking before calculations

        # calculates running pace in minutes per km, rounded to 2dp.
        new_pace = round(as.integer(min) + as.integer(sec)/60, 2)
        paces = c(paces, new_pace)
        cat("Added", new_pace, "\n\n")
    }

    # fills any missing pace entries with NA
    maxkm = 50  # TODO unhardcode this value
    if (km < maxkm) { paces = c(paces, rep(NA, maxkm-km)); }
    # TODO: handle the situation when km > maxkm

    # write new data to file
    data[date] <- c(dist, paces)
    write.table(data, file=data_location, row.names=FALSE, sep=',')
    # QUESTION: is it possible to avoid completely overwriting the table?

    cat("Saved", date, "pace data!\n")
}


plotBoxes = function() {
    # takes the pace data from a CSV file and creates boxplots
    data <- read.csv(file=data_location, header=TRUE, sep=',')
    boxplot(data[2:nrow(data),2:ncol(data)])
}

# addEntry()
