// Exercise 1
console.log('Exercise 1');

let sentence = "Messi is not that bad isn't he";
let wordNot  = sentence.indexOf('not');
let wordBad  = sentence.indexOf('bad');

// console.log(wordBad,wordNot);

if (wordBad > wordNot) {
	let newSentence = sentence.replace('bad ','').replace('that ','').replace('not','good');
	console.log(newSentence);
}else{
	console.log(sentence);
}

// I think I got it done but I wonder if there is a better function to replace
// the whole sequence between the start of wordBad to the end of wordNot.
