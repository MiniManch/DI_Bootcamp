function writtenInTheStars(){
	let num = prompt('Give me a sentence pleaseeeee');
	let wordArray = num.split(' ');
	let longest = 0;
	for(let i in wordArray){
		if(wordArray[i].length > longest){
			longest = wordArray[i].length;
		}
	}
	console.log('*'.repeat(longest + 4));
	for(let i in wordArray){
		if ((longest)-(wordArray[i].length) == 0){
			console.log(`* ${wordArray[i]}`+ ' *');
		}else{
			console.log(`* ${wordArray[i]}`+ ' '.repeat((longest+1)-(wordArray[i].length))+ '*');
		}
	}
	console.log('*'.repeat(longest + 4));
}

writtenInTheStars();