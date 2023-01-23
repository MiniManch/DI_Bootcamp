//Exercise 1 Part 1
console.log('Exercise 1');

function infoAboutMe(){
	console.log('Im Emmanuel, I am 26 years old, I love football and gaming!');
}

infoAboutMe();

// Exercise 1 Part 2
function infoAboutPerson(personName, personAge, personFavoriteColor){
	console.log(`Your name is ${personName}, you are ${personAge} years old, if I had to guess, your favorite color is ${personFavoriteColor}`);	
}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

// Exercise 2 Part 1

function calculateTip(){
	let amount = Number(prompt('How much was the bill in $?'));
	// In the future I will also make sure its not NaN ,don't think it's needed here
	let tip;
	if(amount <= 50){
		tip = amount*0.2;
		console.log(`You should leave ${tip}$ as tip`);
		return tip;
	}else if (amount > 50 && amount <= 200){
		tip = amount*0.15;
		console.log(`You should leave ${tip}$ as tip`);
		return tip;
	}else if (amount > 200){
		tip = amount*0.1;
		console.log(`You should leave ${tip}$ as tip`);
		return tip;
	}
}

calculateTip();
// Doesn't make much sense since if the bill is 199 we should pay 29.85 tip but if its 200 we pay 20 tip :(

// Exercise 3
console.log('Exercise 3');

function isDivisible(divisor){
	let numberList = [];
	for(let i = 1 ;i <= 500; i++){
		if(i % divisor == 0){
			numberList.push(i);
		}
	}
	let sum = 0;
	for (let i of numberList){
		sum = sum + i;
	}
	numberListAsString = numberList.toString();
	console.log(`outcome: ${numberListAsString}`);
	console.log(`Sum: ${sum}`);
}

isDivisible(3);

// Exercise 4
console.log('Exercise 4');

const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = {
	'banana': 1,
	'apple':  1,
	'orange': 1
}

function myBill(){
	let sum = 0;
	for (let i in shoppingList){
		if (i in stock && stock[i] > 0) {
			sum = sum + prices[i];
			console.log(`${i} stock before ${stock[i]}`);
			stock[i] = stock[i] -1;
			console.log(`${i} stock after ${stock[i]}`);
		}
	}
	console.log(`the sum is ${sum}`);
	return sum;
}

myBill();

// Exercise 5
console.log('Exercise 5');

function changeEnough(itemPrice, amountOfChange){
	if (itemPrice <= (amountOfChange[0]*0.25 + amountOfChange[1]*0.1,amountOfChange[2]*0.05+amountOfChange[0]*0.01)) {
		return true;
	}else{
		return false;
	}
}

console.log(changeEnough(14.11, [2,100,0,0]));
console.log(changeEnough(0.75, [0,0,20,5]));

// Exercuse 6
console.log('Exercise 6');

// function hotelCost(){
// 	let sum = 0;
// 	let numOfNights = Number(prompt('How many nights are you planning to stay?'));
// 	while(isNaN(numOfNights) === true){
// 		numOfNights = Number(prompt('How many nights are you planning to stay? this time enter a number silly goose'));
// 	}
// 	if(numOfNights === 0 ){
// 			console.log(`I guess you dont wanna stay here...`);
// 			return false;
// 		}else{
// 			sum = numOfNights*140;
// 			console.log(`The amout you need to pay is ${sum}$ for staying ${numOfNights} here! `);
// 		}
	
// }
// hotelCost();

function hotelCost(num){
	let sum = 0;
	if(num === 0 ){
			console.log(`I guess you dont wanna stay here...`);
			return false;
		}else{
			sum = num*140;
			console.log(`The amout you need to pay is ${sum}$ for staying ${num} here! `);
			return sum;
		}
	
}
// Part 2

// function planeRideCost(){
// 	let location = prompt('Where you wanna go? London and Paris are on sale!').toLowerCase();
// 	let price = 0;
// 	if(location === 'london'){
// 		price = '183$';
// 	}else if(location === 'paris'){
// 		price = '220$';
// 	}else{
// 		price = '300$';
// 	}
// 	console.log(`The price for going to ${location} is ${price}`);
// }

// planeRideCost();

function planeRideCost(loc){
	
	let price = 0;
	if(loc === 'london'){
		price = 183;
	}else if(loc === 'paris'){
		price = 220;
	}else{
		price = 300;
	}
	console.log(`The price for going to ${loc} is ${price}`);
	return(price);
}

// Part 3

// function rentACar(){
// 	let sum = 0;
// 	let num = Number(prompt('How many days are you gonna rent the car for?'));
// 	while(isNaN(num) === true){
// 		num = Number(prompt('How many days are you gonna rent the car for? this time enter a number silly goose'));
// 	}
// 	if(num === 0 ){
// 			console.log(`I guess you dont wanna rent a car`);
// 			return false;
// 		}else if (num >= 10){
// 			sum = 40*(num*0.95);
// 			console.log(`The amout you need to pay is ${sum}$ for renting a car for ${num} days! `);
// 			return sum;
// 		}else{
// 			sum = 40*num;
// 			console.log(`The amout you need to pay is ${sum}$ for renting a car for ${num} days! `);
// 			return sum
// 	   }
	
// }

function rentACar(num){
	let sum = 0;
	if(num === 0 ){
			console.log(`I guess you dont wanna rent a car`);
			return false;
		}else if (num >= 10){
			sum = 40*(num*0.95);
			console.log(`The amout you need to pay is ${sum}$ for renting a car for ${num} days! `);
			return sum;
		}else{
			sum = 40*num;
			console.log(`The amout you need to pay is ${sum}$ for renting a car for ${num} days! `);
			return sum
	   }
	
}

// rentACar();

function totalVacationCost(){
	let daysOfHotel = Number(prompt('How many nights are you planning to stay?'));
	while(isNaN(daysOfHotel) === true){
		daysOfHotel = Number(prompt('How many nights are you planning to stay? this time enter a number silly goose'));
	}
	
	let location = prompt('Where you wanna go? London and Paris are on sale!').toLowerCase();

	let num = Number(prompt('How many days are you gonna rent the car for?'));
	while(isNaN(num) === true){
		num = Number(prompt('How many days are you gonna rent the car for? this time enter a number silly goose'));
	}
	
	let carPrice   = rentACar(num);
	let flightPrice = planeRideCost(location);
	let hotelPrice = hotelCost(daysOfHotel);
	let sum = carPrice + flightPrice + hotelPrice; 
	console.log(`price of car rental is ${carPrice}$, price of flight is ${flightPrice}$,and price of hotel is ${hotelPrice}$. total price of the vacation is: ${sum}$ `);
}

totalVacationCost();