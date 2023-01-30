// // *********Exercise 1*******
// // 1.Using a DOM property, retrieve the h1 and console.log it.
// let h1 = document.querySelector('h1');
// console.log(h1);

// // 2.Using DOM methods, remove the last paragraph in the <article> tag.
// let lastP = document.querySelector('article>p:last-child');
// console.log(lastP);

// // 3.Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
// let h2 = document.querySelector('h2');
// h2.addEventListener('click',function(e){
//    this.style.backgroundColor = 'red';
// });

// // 4.Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
// let h3 = document.querySelector('h3');
// h3.addEventListener('click',function(e){
//    this.style.display = 'none'; 
// });

// // 5.Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
// function addBtn(){
//     let newBtn = document.createElement('button');
//     newBtn.textContent = 'Click to bold!';
//     newBtn.addEventListener('click',function(e) {
//        document.body.style.fontWeight = 'bold'; 
//     });
//    document.body.append(newBtn);
// }

// addBtn();

// // BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
// // Wasn't clear to which element to change fontsize of so I chose body.
// h1.addEventListener('mouseover',function(e){
//    h1.style.fontSize = `${Math.random()}em`;
// });

// // BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
// let secondP = document.querySelector('p+p');
// secondP.addEventListener('mouseover',function(e){
//    secondP.style.opacity = `${Math.random()}`;
// });
// // *********End of Exercise 1*******

// // ***********Exercise 2***********
// // 1.Retrieve the form and console.log it.
// let form = document.forms[0];
// console.log(form);

// // 2.Retrieve the inputs by their id and console.log them.
// let fname = document.querySelector('#fname');
// let lname = document.querySelector('#lname');
// console.log('fname:',fname,'lname:',lname);

// // 3.Retrieve the inputs by their name attribute and console.log them.
// let fnameAtt = document.querySelector("input[name='fname']");
// let lnameAtt = document.querySelector("input[name='lname']");
// console.log('fname:',fnameAtt,'lname:',lnameAtt);

// // 4.When the user submits the form (ie. submit event listener)
// // use event.preventDefault(), why ?
// // get the values of the input tags,
// // make sure that they are not empty,
// // create an li per input value,
// // then append them to a the <ul class="usersAnswer"></ul>, below the form.
// // The output should be :

// // <ul class="usersAnswer">
// //     <li>first name of the user</li>
// //     <li>last name of the user</li>
// // </ul>
// let theUl = document.querySelector('.usersAnswer');

// function createNames(e){
//    e.preventDefault();
//     if (lname.value.length > 0 && fname.value.length > 0 ) {
//       let firstLi  = document.createElement('li');
//       let secondLi = document.createElement('li');

//       firstLi.textContent = `${fname.value} is the first name of the user`;
//       secondLi.textContent = `${lname.value} is the last name of the user`;

//       theUl.append(firstLi,secondLi);
//    }
//    lname.value = '';
//    fname.value = '';
// }
// form.addEventListener('submit',createNames);
// fname.addEventListener('keypress',createNamesButWithEnter);
// // *********End of Exercise 2*******

// // *********Exercise 3*******


// // 1.Declare a global variable named allBoldItems.
// let allBoldItems = [];
// // 2.Create a function called getBold_items() that takes no parameter.
// // This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
// function getBold_items(){
//    for(let i of document.querySelectorAll('*')){
//       if (i.tagName === 'STRONG'){
//          allBoldItems.push(i);
//       }
//    }
//    return allBoldItems;
// }

// // 3.Create a function called highlight() that changes the color of all the bold text to blue.
// function highlight(){
//    for (let i of allBoldItems){
//       i.style.color = 'blue';
//    }
// }
// highlight(getBold_items());

// // Create a function called return_normal() that changes the color of all the bold text back to black.
// function return_normal(){
//    for(let i of allBoldItems){
//       i.style.color = 'black';
//    }
// }

// // Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example
// let para = document.querySelector('p');
// console.log(para);
// para.addEventListener('mouseover',highlight);
// para.addEventListener('mouseout',return_normal);

// *****END OF Exercise 3****

// **********EXERCISE 4*********

// Write a JavaScript program to calculate the volume of a spher
// let radius = document.querySelector('input[name="radius"]');
// let volume = document.querySelector('input[name="volume"]');
// let button =document.querySelector('input[type="submit"]');

// function calculateVolume(){
//    volume.value= '';
//    event.preventDefault();
//    if(radius.value.length > 0 && isNaN(Number(radius.value)) === false){
//       volume.value = Math.pow(Number(radius.value),3)*Math.PI*4/3;
//       console.log(Math.PI);
//       // *(3/4)*Math.PI;
//       radius.value = '';
//    }else if(isNaN(Number(radius.value)) === true){
//       radius.value = '';
//       alert('please enter a number only');
//    }
//    console.log(radius.value, typeof radius.value);
// }
// button.addEventListener('click',calculateVolume);

// **********End of exercise 4********

// ***********Exercise 5***********

// Add many events listeners to one element on your webpage.
//    Use the click, mouseover, mouseout and dblclick events.
// Each listener should do a different thing
// let PsList = document.querySelectorAll('p');
// let lastPFinal = PsList[(PsList.length-1)];

// lastPFinal.addEventListener('mouseover',function(){
//    this.style.backgroundColor = 'purple';
//    this.style.padding = '10px 20px';
//    this.style.margin = '10px';

// });

// lastPFinal.addEventListener('mouseout',function(){
//    this.style.backgroundColor = 'white';
//    this.style.margin = '0px';

//    console.log(this.backgroundColor)
// });

// lastPFinal.addEventListener('dblclick',function(){
//    this.style.position = 'absolute';
//    this.style.right     = '10px';
//    console.log(this.backgroundColor)
// });