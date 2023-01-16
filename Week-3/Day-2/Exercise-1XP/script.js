// Exercise 1
// 1	
let favoriteFood = "Pizza";
// 2

let favoriteMeal = "Breakfast";
// 3

// Exercise 2
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

// Exercise 3
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
let c;
console.log(c);


