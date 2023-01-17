// Exercise 1
console.log('Exercise 1');

console.log('1: ',5 >= 1);
// Prediction:True - 5 does equal or is bigger than 1
// Actual:true
console.log('2: ',0 === 1);
// Prediction:False- === checks if the value and the type is the same, the type is, the value aint
// Actual:false
console.log('3: ',4 <= 1);
// Prediction:False - 4 is bigger than 1, therfore this is False.
// Actual:false
console.log('4: ',1 != 1);
// Prediction:False - 1 does equal to 1.
// Actual:false
console.log('5: ',"A" > "B");
// Prediction:False - I think Alphabetical order is in play here.
// Actual:true
console.log('6: ',"B" < "C");
// Prediction:True -  I think Alphabetical order is in play here.
// Actual:true
console.log('7: ',"a" > "A");
// Prediction:False - Most likely Capital letters "worth more" than smaller caps?
// Actual:false
console.log('8: ',"b" < "A");
// Prediction:True Most likely Capital letters "worth more" than smaller caps?
// Actual: false X mistake
console.log('9: ',true === false);
// Prediction:False - === checks value and type, same type, not same value.
// Actual:false
console.log('10: ',true != true);
// Prediction:False, true does equal to true.
// Actual: false

// Exercise 2
console.log('Exercise 2');

let myList = [prompt('Please add a list of numbers seperated by commas!').split(',')];
console.log(myList);

// Exercise 3
// This works but gives the index by letter in a string.
// let sentence = prompt('please enter a sentence which has the word Nemo in it ! make sure to seperate each word with a single space');
// if (sentence.includes('Nemo')) {
// 	console.log(sentence.indexOf('Nemo'));

// } else{
// 	console.log(sentence,'this aint working');
// }

let my_list = prompt('please enter a sentence which has the word Nemo in it ! make sure to seperate each word with a single space').split(' ');
console.log('Exercise 3: ',my_list,my_list[0],`I found Nemo at ${my_list.lastIndexOf('Nemo')}`);
// Will ask Gaston cause this shit should work!!

// Exercise 4
let var_2 = Number(prompt('Boom me please'));
let boom  = 'Boom'
if (var_2 == 2) {
	console.log(boom);
}else if ((var_2) > 2) {
	if (var_2 % 5 === 0 && var_2 % 2 === 0) {
		console.log(boom.toUpperCase()+'!');
	}else if (var_2 % 2 === 0) {
		console.log(boom + '!');
	}else if (var_2 % 5 === 0) {
		console.log(boom.toUpperCase());
	}else{
		console.log('B'+'o'.repeat(var_2)+'m');
	}	
}
