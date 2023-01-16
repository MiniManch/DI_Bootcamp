// Exercise 1
console.log("Exercise 1");
// 1
const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

// Remove banana
fruits.shift();
console.log('Exercise 1 part 1 ',fruits);

// 2
fruits.sort();
console.log('Exercise 1 part 2 ', fruits);

// 3
fruits.push('Kiwi');
console.log('Exercise 1 part 3 ', fruits);

// 4
fruits.splice(0,1);
console.log('Exercise 1 part 4 ', fruits);

// 5
fruits.reverse();
console.log('Exercise 1 part 5 ', fruits);

// Exercise 2
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

let oranges =  moreFruits[1][1][0];
console.log('Exercise 1',oranges);