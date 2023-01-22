let list = ['*','*','*','*','*','*','*','*','*','*','*','*','*','*'];

for (let i in list){
	console.log(list[i].repeat(i));
	if (i==6){
	break;
	}	
}
let x = 0;
for(let i in list){
	while (i < 7){
		console.log(list[i].repeat(Number(i)+1));
		x++;
		i++;	
		if(x==6){
		break
		}
	}
	if(x==6){
		break
	}
}

// Not sure if this is the cleanest way to do this!