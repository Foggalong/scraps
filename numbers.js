// Javascript script which takes numbers as words and converts them into an integer. Takes numbers of the form "three hundred and fifty seven thousand, one hundred and ninty five" (357,195). Currently supports numbers up to 999,999. 


// Definitions

// Counts length of array
function length(array) {
    var count = 0;
    for (n in array) ++count;
    return count;
}

// Counts occurances of string in array
function occur(item, array) {
    for (n in array) {
        if (array[n] == item) {
            return true;
        }
    }
    return false;
}

// Units List
var units = {
    "zero"       : 0,
    "one"        : 1,
    "two"        : 2,
    "three"      : 3,
    "four"       : 4,
    "five"       : 5,
    "six"        : 6,
    "seven"      : 7,
    "eight"      : 8,
    "nine"       : 9,
    "ten"        : 10,
    "eleven"     : 11,
    "twelve"     : 12,
    "thirteen"   : 13,
    "fourteen"   : 14,
    "fifteen"    : 15,
    "sixteen"    : 16,
    "seventeen"  : 17,
	"eighteen"   : 18,
	"ninteen"    : 19,
	"twenty"     : 20,
	"thirty"     : 30,
	"fourty"     : 40,
	"fifty"      : 50,
	"sixty"      : 60,
	"seventy"    : 70,
	"eighty"     : 80,
	"ninty"      : 90,
    "hundred"    : 100,
};



// Main Program

// Program Input
console.log("Number:"); 
console.read(function(input) {

// Splits into list
var in_list = input.toLowerCase().split(" ");
var out_list = [];

// Turns into numbers
if (occur("thousand", in_list) === true) {
    // Numbers > 999
    error();
}
else if (occur("hundred", in_list) === true) {
    // 100 < Numbers < 999
    if (length(in_list) == 2) {
        out_list [0] = units[in_list[0]]*100;
    }
    else if (occur("and", in_list) === true ) {
        for (x in in_list) 
    }
}
else {
    // Numbers < 99
    for (n in in_list) {
        out_list [n] = units [ in_list[n] ];
    }
}

// Adds numbers together
var total = 0;
for (n in out_list) {
    total = total + out_list[n];
}
// Output
console.log("\nAs digits: " + total);

});
