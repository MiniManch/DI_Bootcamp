// Exercise 1
console.log("Exercise 1");
// 1
let favoriteFood = "Pizza";
// 2

let favoriteMeal = "Breakfast";
// 3

// Exercise 2
console.log("Exercise 2 Part 1");
// Part1
let printMeal = `I eat ${favoriteFood} at every ${favoriteMeal}`
console.log(printMeal);

// 1
 const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;

// 2
let myWatchedSeriesSentence = myWatchedSeries[0]+', ' + myWatchedSeries[1] + ', ' + myWatchedSeries[2];

// 3
console.log('I watched 3 series : '+ myWatchedSeriesSentence);

// Exercise 2
console.log("Exercise 2 part 2");

// Part 2
// 1
myWatchedSeries[myWatchedSeries.indexOf("the big bang theory")] ='friends'
console.log(myWatchedSeries[2])

// 2
myWatchedSeries.push('Seinfeld');
console.log('adding Seinfeld at the end', myWatchedSeries);

// 3
myWatchedSeries.unshift('Archer');
console.log('adding Archer at the start ',myWatchedSeries);

// 4
delete myWatchedSeries[myWatchedSeries.indexOf('black mirror')];
console.log('deleting black mirror ',myWatchedSeries);

// 5
console.log('Printing 3rd letter of Money Heist',`${myWatchedSeries[2]}`.substr(2,1));

// 6
console.log(myWatchedSeries);

// Exercise 3
console.log("Exercise 3");

let tempCelsius = 30;
let tempFarenheit = tempCelsius * 1.8 + 32;
console.log('Printing temperatures.',`${tempCelsius}°C is ${tempFarenheit} `);

// Exercise 4
// What will be the outcome of a + b in the first expression ?
// Prediction: 34 + 21 = 55.

// What will be the outcome of a + b in the second expression ?
// Prediction: 2 + 21 = 23.

// What is the value of c?
// Prediction: undefined.

// Analyse the code below, what will be the outcome?
// console.log(3 + 4 + '5');
// Prediction: JS knows that we're trying to add numbers with strings so it will be 7+5 so 75. because 5 is a string.

// Exercise 5
console.log("Exercise 5");

console.log(typeof(15));
// Prediction: number
// Actual: number

console.log(typeof(5.5));
// Prediction: number, i thought it might be like python or other languages where there's a difference between whole and decimal numbers, but I'm pretty confident.
// Actual: number

console.log(typeof(NaN));
// Prediction: NaN? undefined maybe
// Actual: number

console.log(typeof("hello"));
// Prediction: String
// Actual: string

console.log(typeof(true));
// Prediction: Boolean, pretty self explanatory
// Actual: boolean

console.log(typeof(1 != 2));
// Prediction:Boolean, i think the outcome will be false and that is a boolean value
// Actual: boolean

console.log("hamburger" + "s");
// Prediction: "hamburgers"
// Actual: "hamburgers"

console.log("hamburgers" - "s");
// Prediction: "hamburger"
// Actual:NaN - I'm guessing you cant do any subtraction with strings :(

console.log("1" + "3",typeof("1"+"3"));
// Prediction: "13", because they're both strings its like combining both strings.
// Actual: "13"

console.log("1" - "3");
// Prediction: undefined? I dont think there is any way to do that.
// Actual:NaN

console.log("johnny" + 5);
// Prediction: perhaps "johnny5"? just guessing, either that or an error.
// Actual:"johnny5"

console.log("johnny" - 5);
// Prediction: probably undefined or error.
// Actual:NaN

console.log(99 * "hello");
// Prediction: probably 99times "hello" in a continuous string.
// Actual:NaN

console.log(1 != 1);
// Prediction: boolean? probably false.
// Actual:false

console.log(1 == "1");
// Prediction: True and boolean. because == checks if they have the same value not the same type.
// Actual: true

console.log(1 === "1");
// Prediction:False. === checks for both value and same type.
// Actual:false

// Exercise 6
console.log("Exercise 6");

console.log(5 + "34");
// Prediction: 534, number type - Because we're adding up a number and a string, it will add them together but weirdly.
// Actual:534

console.log(5 - "4");
// Prediction: NaN, i think substracting a string will always result in NaN as seen in the previous exercise.
// Actual:1 , i guess it can do that with 'number strings?'

console.log(10 % 5);
// Prediction:0, 10%5 means the remainder of dividing 10 by 5 which is 0.
// Actual: 0

console.log(5 % 10);
// Prediction: 5, it isnt divisible in whole therefore its 5.
// Actual: 5

console.log("Java" + "Script");
// Prediction:"JavaScript" its just adding up strings
// Actual:"JavaScript"

console.log(" " + " ");
// Prediction:"  " its just adding up strings
// Actual: "  "

console.log(" " + 0,typeof(" "+ 0));
// Prediction:" 0" or NaN.
// Actual:" 0"

console.log(true + true);
// Prediction: 2 i think True =1 and False = 0 right? it is boolean after all.
// Actual:2

console.log(true + false);
// Prediction: 1
// Actual:1

console.log(false + true);
// Prediction: 1
// Actual:1

console.log(false - true);
// Prediction: - 1
// Actual:-1

console.log(!true);
// Prediction: false, not-true is False isnt it?
// Actual:false

console.log(3 - 4);
// Prediction: -1 its just mathematics
// Actual:-1

console.log("Bob" - "bill");
// Prediction:NaN, can't  subtract a string, it will be NaN.
// Actual:NaN


