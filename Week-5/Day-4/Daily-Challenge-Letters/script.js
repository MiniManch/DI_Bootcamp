let input = document.querySelector('input');

console.log('input');

input.addEventListener('keyup',function(){
	if (event.keyCode < 65 || event.keycode > 90 || event.keycode === undefined){
		input.value = input.value.replace(event.key,'');
	}
});