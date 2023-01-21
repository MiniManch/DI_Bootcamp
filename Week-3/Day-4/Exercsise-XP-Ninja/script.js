// Exercise 1
console.log('Exercise 1');

let age1 = Number(prompt('Hey first peron! Please enter your age in YYYY format!'));
let age2 = Number(prompt('Hey second peron! Please enter your age in YYYY format!'));

if ((2023 -age1) > (2023 - age2)) {
	let halfAge  = (2023 - age1)/2;
	let solution =  age2 + halfAge;
	console.log(`the second person was half the age of the first person in ${solution}`);
}

// Exercise 2
console.log('Exercise 2');

// without regex
let zipCode = Number(prompt('Please give me your zipcode pleaseeeee').split(" ").join(""));
console.log(zipCode,zipCode.length);
if (isNaN(zipCode)) {
	console.log('This aint a number you stupid fuck');
}else if (zipCode.toString().length === 5 ) {
	console.log('Nice zipcode mate');
}else if (zipCode.toString().length < 5 || zipCode.toString().length > 5){
	console.log('are you sure this is a correct zipcode mate?');
}

