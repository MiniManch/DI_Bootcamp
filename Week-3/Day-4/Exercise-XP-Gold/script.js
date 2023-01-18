// Exercise 1
console.log('Exercise 1');

let lang = prompt('What language do you speak?').toLowerCase();

switch (lang){
case 'english':
	console.log('Hello!');
	break;
case 'french':
	console.log('Bonjour!');
	break;
case 'hebrew':
	console.log('Shalom!');
	break;
default:
	console.log('01110011 01101111 01110010 01110010 01111001');
}

// Exercise 2
console.log('Exercise 2');
let grade = Number(prompt('how much did you get on your test mister?'));

if (grade > 90) {
	console.log('A');
}else if (grade <= 90 && grade > 80){
	console.log('B');
}else if (grade <= 80 &&  70 <= grade){
	console.log('C');
}else if (grade < 70){
	console.log('D');
}

// Exercise 3
console.log('Exercise 3');

let verb = prompt('Please enter a Verb');

if (verb.length >= 3 ) {
	if (verb.slice(-3) != 'ing') {
		verb = verb + 'ing';
		console.log(`the string is: ${verb}`);
	}else{
		verb = verb + 'ly';
		console.log(`the string is: ${verb}`);
	}
}else if ( verb.length < 3){
	console.log(`the string is: ${verb}`);
}