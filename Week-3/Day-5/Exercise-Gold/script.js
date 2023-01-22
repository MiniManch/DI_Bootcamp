// Exercise 1
console.log('Exercise 1');

let numbers = [123, 8409, 100053, 333333333, 7]

for(let i of numbers){
	if(i % 3 === 0){
		console.log(i,true);
	}else{
		console.log(i,false);
	}
}

// Exercise 2
console.log('Exercise 2');
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let name = prompt('What is your name?').toLowerCase();

if (name in guestList){
	console.log(`My name is ${name} and Im from ${guestList[name]}`);
}else{
	console.log('Hi there guest!');
}

// Exercise 3
console.log('Exercise 3');

let age = [20,5,12,43,98,55];

let sum = 0;

for (let i of age){
	sum = sum + i;
	console.log(sum);
}

let heighest = 0;

for (let i of age){
	if (i > heighest){
		heighest = i;
	}else{
		continue;
	}
}
console.log(heighest);