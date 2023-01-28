// // Exercise 1
// // 1
// let firstDiv = document.getElementsByTagName('div');
// console.log(firstDiv);

// // 2
// let peteLi = document.querySelector('ul>li:last-child');

// peteLi.textContent = 'Richard';
// console.log(peteLi);

// // 3
// let firstName = document.querySelectorAll('ul>li:first-child');

// for (let i of firstName){
// 	i.textContent = 'Emmanuel';
// 	console.log(i);
// }

// 4
// let sarahParent = document.querySelectorAll('ul')[1];
// Ive added Id in the html to make this make sense
// let sarahLi = document.querySelector('#sarah');
// sarahLi.remove()

// bonus
// 1
// let uls = document.querySelectorAll('ul');
// for(let i of uls){
// 	i.classList.toggle("student_list");
// }

// console.log(uls);

// // 2
// let firstUl =  document.querySelector('ul');
// firstUl.classList.toggle('university');
// firstUl.classList.toggle('attendance');


// Exercise 2





// 1
// Add a “light blue” background color and some padding to the <div>.

// let usersDiv = document.querySelector('#users');
// usersDiv.style.backgroundColor = 'lightBlue';
// usersDiv.style.padding         = '20px';

// // 2
// Do not display the <li> that contains the text node “John”.

// let john = document.querySelectorAll('ul>li:first-child')[2];
// john.style.display = 'none';
	
// 3
// Change the font size of the whole body.

// let pete2 = document.querySelectorAll('ul>li:last-child')[2];
// pete2.style.border = '5px dotted red';

// 4 
// Add a border to the <li> that contains the text node “Pete”.

// let body = document.querySelector('body');
// body.style.fontSize = "25px";

// // bonus
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).

// console.log(usersDiv.style.backgroundColor);
// if(usersDiv.style.backgroundColor == 'lightblue'){
// 	console.log('inside for loop');
// 	let usersToAlert = '';
// 	for (let i of document.querySelectorAll('#users + ul>li')){
// 		usersToAlert = usersToAlert + i.textContent + ' ';
// 		console.log(i);
		
// 	}
// 	alert(usersToAlert);
// }

// Exercise 3
// 1
// In the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

// let linkDiv = document.querySelector('#navBar');
// linkDiv.setAttribute('id','socialNetworkNavigation');

// 2
// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

// let newLi = document.createElement('li');
// newLi.textContent = 'Log Out';this works too
// let textNode = document.createTextNode("Log Out"); newLi.appendChild(textNode); linkDiv.querySelector('ul').appendChild(newLi);

// Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve 
// the first and last <li> elements from their parent element (<ul>). 
// Display the text of each link. (Hint: use the textContent property).

// let firstLiOfBonus = linkDiv.querySelector('ul').firstElementChild;
// let lastLiOfBonus  = linkDiv.querySelector('ul').lastElementChild;

// console.log(firstLiOfBonus.textContent,lastLiOfBonus.textContent);

// Exercise 4
let allBooks = [];
let bookOne  = {'title':'Sir Alex Ferguson Autobiography',
                "author":'Sir Alex Ferguson',
                'image':'https://tinyurl.com/2p8a94ra',
                'alreadyRead':false};
let bookTwo  = {'title':"Harry Potter and the Sorcerer's Stone",
                "author":'J. K. Rowling',
                'image':'https://tinyurl.com/2p86w8j3',
                'alreadyRead':true};

allBooks.push(bookOne,bookTwo);

let htmlTable = document.createElement('table');
htmlTable.append(document.createElement('tr'),
                 document.createElement('tr'),
                 document.createElement('tr'));

// adding the table into the div so I can play around with attributes and shit

document.querySelector('.listBooks').appendChild(htmlTable);
let listBooksTrList = document.querySelectorAll('.listBooks > table >tr');

// creating table headers and rows, couldve also used switch
// Going through th tr and adding classes and elements inside.
let x = 0;
for (let i of listBooksTrList) {
    if (x === 0){
        i.classList.toggle('header');
        i.append(document.createElement('th'),
                 document.createElement('th'),
                 document.createElement('th'),
                 document.createElement('th'));
    }else if (x === 1  ){
        i.classList.toggle('bookOne');
        i.append(document.createElement('td'),
                 document.createElement('td'),
                 document.createElement('td'),
                 document.createElement('td'));
    }else if (x === 2){
         i.classList.toggle('bookTwo');
         i.append(document.createElement('td'),
                 document.createElement('td'),
                 document.createElement('td'),
                 document.createElement('td'));
    }
    i.classList.toggle('row');
    x+=1;
}

// selecting all the tds using document query querySelector
// also adding it into an array so it can be used logicaly and not only by knowing what to add

let tableHeaders = document.querySelectorAll('.header > th');
let bookOneTds   = document.querySelectorAll('.bookOne > td');
let bookTwoTds   = document.querySelectorAll('.bookTwo > td');
let allBooksKeys = Object.keys(allBooks[0]);
let tableArray   = [tableHeaders,bookOneTds,bookTwoTds];

// basicaly adding text or image tag with src and image link through the books array and the objects inside
for (let index = 0; index < (bookOneTds.length); index++) {
    if (allBooksKeys[index] === 'image') {
        bookOneTds[index].appendChild(document.createElement('img')).setAttribute('src',(allBooks[0][allBooksKeys[index]]));
        bookTwoTds[index].appendChild(document.createElement('img')).setAttribute('src',(allBooks[1][allBooksKeys[index]]));
    }else{
        bookOneTds[index].appendChild(document.createTextNode(allBooks[0][allBooksKeys[index]]));
        bookTwoTds[index].appendChild(document.createTextNode(allBooks[1][allBooksKeys[index]]));
        
    }
    tableHeaders[index].appendChild(document.createTextNode(allBooksKeys[index]));
}

// setting height and width of images

let imagesInsideTable = document.querySelectorAll('img');
console.log(imagesInsideTable)
for (let i of imagesInsideTable) {
    i.style.height = '100px';
    i.style.width = '100px';
}

// checking if true or false and then making it red.

let alreadyReadColumn = document.querySelectorAll('tr>td:last-child');
for (let index = 0; index < alreadyReadColumn.length; index++) {
    if(alreadyReadColumn[index].textContent === 'true'){
        for(i of tableArray[index+1]){
            i.style.color ='red';
        }
    }
}
