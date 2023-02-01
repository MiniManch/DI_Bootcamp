
let taskInput = document.querySelector("input[type='text']");
let submitBtn = document.querySelector("input[type='submit']");
let taskDiv   = document.querySelector('div');

function deleteTask(){
	this.parentNode.remove();
}

function addTask(){
	event.preventDefault();
	if(taskInput.value === ''){
		alert('your task is empty! thats not gonna work');
		return false;
	}else{
		// creating elements
		let newTaskP   = document.createElement('p');
		let newTaskDiv = document.createElement('div');
		let deleteBtn  = document.createElement("span");
		let fontX      = document.createElement('i');
		// adding text value
		newTaskP.textContent = taskInput.value;
		// adding classes
		newTaskDiv.classList.add('taskObject');
		deleteBtn.classList.add('delete');
		fontX.classList.add('fa-solid','fa-rectangle-xmark','fa-lg');
		// appending
		deleteBtn.append(fontX);
		newTaskDiv.append(newTaskP,deleteBtn);
		taskDiv.append(newTaskDiv);
		// setting input to empty again
		taskInput.value = '';
		// adding delete functionality
		deleteBtn.addEventListener('click',deleteTask);
	}
}


submitBtn.addEventListener('click',addTask);