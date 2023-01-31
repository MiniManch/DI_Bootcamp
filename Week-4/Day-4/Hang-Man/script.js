// Create the “Hangman” game. Your game will run in the console.
// You need to guess a hidden word. Each letter you guess will appear in the console. You have 10 chances before you lose the game.

// Prompt player 1 for a word. The word must have a minimum of 8 letters. Present the word in the console with stars (********).
// At this point continuously prompt player 2 for a letter.
// If the letter is in the word chosen by player 1, display the word in stars again but with the correct letter (*****t**).
// If the letter appears in the word multiple times, make sure it is seen in all the correct places when showing the stars with the correct guesses (***t**t*).
// If player 2 guesses incorrectly 10 times display a message in the console saying YOU LOSE.
// Show a list of all the guesses after each turn. In your code prevent player 2 from guessing the same letter twice.
// If player 1 wins, display a message that says CONGRATS YOU WIN.

let wordArray = ["researcher", 'shareholder', 'legislation','paralyzed','temptation', 'treasurer','basketball','introduce','mathematics','offensive'];
// Function from internet to  pull random word from the array
function getRandomWord(array) {
    return array[Math.floor(Math.random() * array.length)];
};

// Function to see if he even wants to play;
function wannaPlay(){
    let doYou = prompt('Do you wanna play? enter yes or no !');
    while (doYou.toLowerCase() != 'yes' && doYou.toLowerCase() != 'no'){
        doYou = prompt('Just enter yes or no, nothing else brudda');
         if (doYou.toLowerCase() === 'yes'){
            console.log("you're into it aren't you boy?");
             return true;
        }else if(doYou.toLowerCase() === 'no'){
            console.log('youre not into it arent you boy?');
             return false;
        }
    }
    
}

// Function to see if he wants to enter his own word or play with one of my randomized words!
function newOrRandom(){
    let question     = prompt("do you wanna enter your own word (minimum 8 letters) or choose a randomized word by the computer? enter 'random' or 'my own' respectfuly ");
    let findThatWord;
    if(question.toLowerCase() != 'random' && question.toLowerCase() != 'my own'){
       while (question.toLowerCase() != 'random' && question.toLowerCase() != 'my own'){
           question = prompt("Just enter 'random' or 'my own', nothing else brudda");
       } 
    }else if(question.toLowerCase() === 'random'){
        findThatWord = getRandomWord(wordArray);
    }else if(question.toLowerCase() === 'my own'){
        findThatWord = prompt('Please enter your word! remember it has to be minimum 8 letters!');
        while (isNaN(Number(findThatWord)) != true || findThatWord.length < 8 ) {
            findThatWord = prompt('try again! Please enter your word! remember it has to be minimum 8 letters!')
        }
    }
    return findThatWord;
}
// Function making sure that the guess is one letter and not a space or a number
function guessOfUser(){
    let guess = prompt('give me a letter, only one letter please!');
    while ( guess === null || guess === ' ' || guess.length === 0){
        guess = prompt('try again! either you entered a space,nothing, or more than 1 letter!');
    }
    if (isNaN(Number(guess)) === false) {
            guess = prompt('try again! my guess is you tried entering a number!');
        }else if (isNaN(Number(guess))) {
            console.log('inside if');
        while(guess.length > 1 || guess === ' ' || guess.length === 0){
            guess = prompt('try again! either you entered a space,nothing, or more than 1 letter!');
        }
    }
    return guess;
}

function guessingGame(word){
    let wordLength = word.length;
    let maxGuess = 10;
    let numOfGuesses = 0;
    let guessArray = []
    let starArray  = []
    
    console.log('Here is the amount of letters displayed with stars! start guessing!');
    console.log('*'.repeat(wordLength));
    let guess = guessOfUser();
    guessArray.push(guess);

}

guessingGame(newOrRandom());