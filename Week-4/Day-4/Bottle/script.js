// // In the song, everytime a bottle drops,
// the subtracted number should go up by 1.
// For example,

//     We start the song at 99 bottles
//     -> Take _1_ down, pass it around
//     -> we have now 98 bottles

//     -> then, Take _2_ down, pass them around
//     -> we have now 96 bottles
*
//     -> then, Take _3_ down, pass them around
//     -> we have now 93 bottles

//     ... ect


// 3. The song should end with “0 bottle of beer on the wall” or “no bottle of beer on the wall”.


// 4. Note : Make sure you get the grammar correct.

// For 1 bottle, you pass “it” around.
// For more than one bottle, you pass “them” around.
// function checking the prompt
function enterANum(){
	var num = Number(prompt('Please select a number between 0-1000'));
	while(isNaN(num) == true || num <= 0 || num > 1000){
		if( num > 1000 ){
    		num = Number(prompt('your number is bigger than 1000!! choose a lower number bruh'));
    	}else if(num < 0 ){
    		num = Number(prompt('your number is smaller than or equal to 0, we cant count down from that! cant have negative number of bottles i guess'));
    	}else if(isNaN(num) === true ){
    		num = Number(prompt('you entered a text dummy enter a number'));
    	}else if(num === 0){
            num = Number(prompt('you literally entered a blank. dont try and skip me '));
        }
	}
	return num;
}


function bottleOnTheWall() {
    let num = enterANum();
    let bottleNumber = num;
    let numberSubstract = 1;
    console.log(`We shall tell the tale about the ${num} bottles on the wall!`);
    for (let index = 0; bottleNumber > 0; index++) {
        if(bottleNumber === 1 || (bottleNumber - index) < 0){
            console.log(`0 bottles on the wall if we try to take ${index} down,  and pass it around`);
            bottleNumber -= index;
            console.log(` no more bottles left on the wall!`);
        }else{
            console.log(`${bottleNumber} bottles on the wall, take ${index} down, pass them around`);
            bottleNumber -= index;
            console.log(`${bottleNumber} left on the wall!`);
        }        
    }
}

bottleOnTheWall();