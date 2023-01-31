// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
let noun      = [document.querySelector('#noun'),'noun'];
let adjective = [document.querySelector('#adjective'),'adjective'];
let person    = [document.querySelector('#person'),'person'];
let verb      = [document.querySelector('#verb'),'verb'];
let place     = [document.querySelector('#place'),'place'];
let lib       = [document.querySelector('button'),'button'];
let story     = document.querySelector('#story');
let adlibList = [noun,adjective,person,verb,place];
let storyList = [];
// Make sure the values are not empty
function adLib(){
    event.preventDefault();
    for(let i of adlibList){
        if (i[0].value.length === 0 || !isNaN(Number(i[0].value))) {
           alert(`${i[1]} is empty or a number! please try again`);
            break;
        }else{
            storyList.push(i[0].value);
            }
        }
    story.textContent = storyList.toString().replaceAll(',',' ');
    for(let x of adlibList){
        x[0].value = ''; 
 } 
}          

lib[0].addEventListener('click',adLib);
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, 
//     when clicked the button should change the story currently displayed (but keep the values entered by the user).
//     The user could click the button at least three times and get a new story. Display the stories randomly.
 let shuffle = document.querySelector('#shuffle');
console.log(storyList);
shuffle.addEventListener('click',function(){
    event.preventDefault();
    newList = storyList.sort(() => Math.random() - 0.5);
    story.textContent = newList.toString().replaceAll(',',' '); 
});