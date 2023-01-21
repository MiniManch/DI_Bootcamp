// Exercise 1
// Part 1
console.log('Exercise 1');

const people = ["Greg", "Mary", "Devon", "James"];
// 1
for (let element in people){
// 1
	if (people[element] === 'Greg') {
		people.splice(element,1);
		console.log(people,element);
	}
}

// 2
for (let element in people){
	if (people[element] === 'James') {
		people[element] = 'Jason';
		console.log(people,element);
	}
}

// 3
people.push('Emmanuel');
console.log(people);

// 4
for(let element in people){
	if (people[element] === 'Mary') {
		console.log(`${people[element]} index is ${element}`);
	}
}

//5
// Sturggled alittle with slice but found the solution
// using for of loop too.
// let newArray = [];
// for(let element of people){
// 	if (element === 'Mary' || element === 'Emmanuel') {
// 		continue;
// 	}else{
// 		newArray.push(element);
// 	}
// }

const newArray = people.slice(people.indexOf('Mary')+1,people.indexOf('Emmanuel'));
console.log(newArray);

// 6
console.log(newArray.indexOf('Foo'));
// returns -1 because foo is not in the array

// 7
let last = newArray[newArray.length -1];
console.log(last);

// Part 2
// 1
for(element of people){
	console.log(element);
	if (element === 'Jason') {
		break
	}
}

// Exercise 2
let colors = ['Red','White','Black','Blue','Purple'];
let suffixArray = ['st','nd','rd','th'];

for(let i in colors){
	if(i>2){
		console.log(`My ${Number(i)+1}${suffixArray[3]} choice is ${colors[i]}`);
	}else{
		console.log(`My ${Number(i)+1}${suffixArray[i]} choice is ${colors[i]}`);
	}
}


// Exercise 3
let userNumber = Number(prompt('give me a number mafaka'));

while(userNumber < 10){
	userNumber = Number(prompt('That aint good enough give me a new number'));
}

// Exercise 4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

// 2
console.log(building.numberOfFloors);
// 3
console.log(building.numberOfAptByFloor.firstFloor,building.numberOfAptByFloor.thirdFloor);
// 4
console.log(building.nameOfTenants[1],building.numberOfRoomsAndRent.dan[0]);
// 5

let dansRent   = building.numberOfRoomsAndRent.dan[1];
let davidsRent = building.numberOfRoomsAndRent.david[1];
let sarahsRent = building.numberOfRoomsAndRent.sarah[1];

if ((davidsRent + sarahsRent)> dansRent) {
	console.log('Dans rent before',building.numberOfRoomsAndRent.dan[1]);
	building.numberOfRoomsAndRent.dan[1] = Number(dansRent) + 1200;
	console.log('Dans rent after',building.numberOfRoomsAndRent.dan[1]);
}

// Exercise 5

const family = {
	dad: 'David',
	mother: 'Dominique',
	brother: 'Yosef',
	dogOne: 'Falola',
	dogTwo: 'Lea',
	girlfriend: 'Adi'
}

for(let i in family){
	// 1
	console.log(i);
	// 2
	console.log(family[i]);
}

// Exercise 6

const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

for(let i in details){
	console.log(i,details[i]);
}
// I  tried to console.log details.i but that didn't work, I thought that's how you use keys and value objects?
// Exercise 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let orderedNames = names.sort();
let secretSocietyName = '';

for(let i in orderedNames){
	secretSocietyName = secretSocietyName + orderedNames[i][0];
}
console.log(secretSocietyName);