// // Exercise 1 THIS HAS HTML AND STYLE TAG TOO
// // In your Javascript file, using setTimeout, call a function after 2 seconds.
// // The function will alert “Hello World”.

// myTimeOut = setTimeout(helloWorld,2000);
// function helloWorld(){
//     console.log('hello world!');
// }

// // In your Javascript file, using setTimeout, call a function after 2 seconds.
// // The function will add a new paragraph <p>Hello World</p> to the <div id="container">
// let container = document.querySelector('#container');

// myNewTimeOut = setTimeout(createNewPHelloWorld,2000);
// function createNewPHelloWorld(){
//     let newP      = document.createElement('p');
//     newP.textContent = 'hello World!';
//     container.append(newP);
// }

// // In your Javascript file, using setInterval, call a function every 2 seconds.
// // The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// // The interval will be cleared (ie. clearInterval), when the user will click on the button.
// // Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

// myInterval = setInterval(createNewPInterval,2000);
// function createNewPInterval(){
//    let newP      = document.createElement('p');
//    newP.classList.add('interval_p');
//     newP.textContent = 'hello World!';
//     let interval_pList = document.querySelectorAll('.interval_p');
//     console.log(interval_pList);
//     if (interval_pList.length === 5){
//         clearInterval(myInterval);
//         console.log("I've stopped the interval for you");
//     }else{
//         container.append(newP);
//     }
// }

// let clearButton = document.querySelector('#clear');
// clearButton.addEventListener('click',function(){
//     clearInterval(myInterval);
//     console.log("I've stopped the interval for you");
// });

// // END OF EXERCISE 1

// // EXERCISE 2
// let animate = document.querySelector('#animate');
// let container = document.querySelector('#container');
// let num = 0;
// let clearButton = document.querySelector('#clear');
// console.log(container.style);
// clearButton.addEventListener('click',function(){
//     clearInterval(animateInterval);
// })

// function toNum(urString){
//     return Number(urString.replace('px',''));
// }

// function myMove(){
//     animateInterval = setInterval(function(){
//         animate.style.left = num+"px";
//         num+=1;
//         let divs = document.querySelectorAll('div');
//         let containerWidth = document.styleSheets[0].cssRules[0].style.width;
//         let animateWidth   = document.styleSheets[0].cssRules[1].style.width;
//         if((toNum(animate.style.left) + toNum(animateWidth)) === toNum(containerWidth)){
//             console.log('true dat');
//             clearInterval(animateInterval);
//         }
//     },1)
// }

// // END OF EXERCISE 2

// EXERCISE 3
// add draggable property
function allowDrop() {
  event.preventDefault();
  console.log('works');
}

function drag() {
  event.dataTransfer.setData("text", event.target.id);
  console.log('dragged');
}

function drop() {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  event.target.appendChild(document.getElementById(data));
  console.log(dropped);
}

let dragBox = document.querySelector('#box');
dragBox.setAttribute('draggable','true');

let dropTarget = document.querySelector('#target');

dragBox.addEventListener('drag',function(){
    drag();
});

dragBox.addEventListener('ondrop',drop);
dropTarget.addEventListener('ondragover',allowDrop);