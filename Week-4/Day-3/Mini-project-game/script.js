// Function to get an  integer and , otherwise it would probably always be 0.
function getRandomIntInclusive(min, max) {
 	min = Math.ceil(min);
  	max = Math.floor(max);
 	return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
}
// Function to get a new number  instead of writing the same lines again and again
function enterANum(){
	var num = Number(prompt('Please select a number between 0-10'));
	while(isNaN(num) == true || num > 10){
		num = Number(prompt('either you entered a text, or your number is bigger than 10, try again!'));
	}
	return num;
}

// Comparing the numbers
function compareNumbers(userNum,pcNum){
	let number;
	while(userNum != pcNum ){
		if(userNum > pcNum ){
			alert("Your number was bigger than the computer's, try again!");
			userNum = enterANum();
			console.log(userNum);
		}else if(userNum < pcNum ){
			alert("Your number was smaller than the computer's, try again!");
			userNum = enterANum();
			console.log(userNum);
		}else if(userNum === pcNum ){
			break;
		}
	}
	return true;
}

// Final function
function playTheGame(){
	let userConf = confirm('*Triple H voice* Do you wanna play the game?');
	if(userConf == false){
		alert('no problem boo');
		return false;
	}else{
		var num = enterANum();
		var computerNumber = getRandomIntInclusive(0,10);
		console.log(computerNumber);
	}
	if (compareNumbers(num,computerNumber)) {
		alert("WINNER! your number matches the computer's randomized number!");
	}
}
