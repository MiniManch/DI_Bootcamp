// Create an array which value is the planets of the solar system.
// Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune;

let planetsArrayAndMoons ={'Mercury':0,'Venus':0,'Earth':1, 'Mars':2, 'Jupiter':57, 'Saturn':63, 'Uranus':27,'Neptune':14};

// For each planet in the array, create a <div> using createElement. This div should have a class named "planet"
// Each planet should have a different background color. 
// (Hint: you could add a new class to each planet - each class containing a different background-color).

let planetDivArray = [];
for (let index = 0; index < Object.keys(planetsArrayAndMoons).length; index++) {
    planetDivArray.push(document.createElement('div'));
}
let colorList = {'Mercury': 'grey',
                'Venus' : '#764359',
                'Earth' : 'Blue',
                'Mars' :'Red',
                'Jupiter' : 'Brown',
                'Saturn' : 'gold',
                'Uranus' : 'green',
                'Neptune' : 'purple'}

// going through a loop inorder to add the planet class and the style
// Finally append each div to the <section> in the HTML (presented below).
// Bonus- add the moon.
// NOTE: couldve probably used just one object with a an array of values. 

let x = 0;
for (let i of planetDivArray){
    i.textContent = Object.keys(planetsArrayAndMoons)[x]
    i.classList.toggle('planet');
    console.log(i.textContent);
    if (i.textContent === Object.keys(colorList)[x]){
        i.style.backgroundColor = Object.values(colorList)[x];
        i.setAttribute('id',`${Object.keys(colorList)[x]}`);
        i.style.color = 'white';
        i.append(document.createElement('div'));
        document.querySelector('section').append(planetDivArray[x]);
        document.querySelector(`#${Object.keys(colorList)[x]} > div`).classList.add('moon');
        document.querySelectorAll('.moon')[x].textContent = Object.values(planetsArrayAndMoons)[x];
        document.querySelectorAll('.moon')[x].style.color = 'black';
        console.log(document.querySelectorAll('.moon')[x])
    }
    x=x+1;
}


