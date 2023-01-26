// number(num)
let userNumber = '';
let equation   = [];
let finalEquation = '';
function number(num){
	userNumber = userNumber + num;
	console.log(userNumber);
}
// operatior(oper)
function operator(oper){
	equation.push(userNumber);
	userNumber = '';
	equation.push(oper);
}
// equal()

function equal(){
	equation.push(userNumber);
	console.log(equation);
	for (i of equation){
		finalEquation = finalEquation + i;
	}
	console.log(finalEquation);
	console.log(eval(finalEquation));
	clearNum();
}

// clear()
// for some reason it doesnt work... 
// the function should work, yet something about the button wont even do anything
function clearNum(){
	userNumber = '';
	equation   = [];
	finalEquation = '';
	console.log('cleared');
}