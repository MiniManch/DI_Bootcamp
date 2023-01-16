// Exercise 1 : Favorite Color
console.log('Exercise 1');
let sentence = ["my","favorite","color","is","blue"];
let sentenceNew = [];
sentenceNew[0] = sentence[0] + sentence[1] + sentence[2] + sentence[3] +sentence[4];
// I tried using .values() but seems like it needs loops or ifs statments and that aint it yet.
console.log(sentenceNew);

// Exercise 2 : Mixup
// 1
console.log('Exercise 2');
let str1 = "mix";
let str2 = "pod";
// 2
let str1New = str1.replace(str1[0],str2[0]);
let str2New = str2.replace(str2[0],str1[0]);
// I would like to know how  to change the string itself! not save to a new var
console.log(`this is the new str1: ${str1New}`);
console.log(`this is the new str2: ${str2New}`);
// 3
let str1And2 = str1.concat(' '+str2);
// 4
console.log(str1And2);

// Exercise 3 : Calculator
console.log('Exercise 3');
// 1+2
let num1 = Number(prompt());
console.log(typeof(num1),num1);
// 3+4
let num2 = Number(prompt());
alert(`This is the some of num1 and num2: ${num1+num2}`);

// I thought about making a function that allows user interaction to decide what function 
// (+ - * % /) he wants to do, and then enter numbers,and post the result, but this will
// have too many ifs and stuff i thought its too advance.
