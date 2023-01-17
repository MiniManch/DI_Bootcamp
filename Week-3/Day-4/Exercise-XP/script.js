// Exercise 1
console.log('Exercise 1');
let x = 2;
let y = 18;

if (x > y) {
	console.log('x is bigger, duh!');
}else if (x < y) {
	console.log('y is bigger,dahoyyyy!');
}else{
	console.log('they are equal you dummy');
}

// Exercise 2
console.log('Exercise 2');
let newDog = "Chihuahua";

console.log(newDog.length);
console.log(newDog.toUpperCase(),newDog.toLowerCase());

if (newDog === 'Chihuahua') {
	console.log('I love Chihuahuas, it’s my favorite dog breed')
}else {
	console.log('I dont care, I prefer cats');
}


// Exercise 3
console.log('Exercise 3');

let userNum = Number(prompt('Please give me a number, any number!'));

if (userNum % 2 === 0) {
	console.log('Your number is Even!');
}else{
	console.log('Your number is Odd Dog!');
}

// Exercise 4
console.log('Exercise 4');
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
console.log(users.length)
switch(users.length) {
  case 0:
    console.log('no one is online!');
    break;
  case 1:
    console.log(`user ${users[0]} is online!`);
    break;
  case 2:
  	console.log(`user ${users[0]} and ${users[1]} are online!`);
  	break
  case users.length:
  	console.log(`user ${users[0]} and ${users[1]} and ${users.length - 2} others are online!`);
  default:
    console.log('this is a switch')
} 