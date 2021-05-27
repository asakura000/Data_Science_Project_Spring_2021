// this code not actually linked to html, but its twin exists within the index.html file

const guageElement = document.querySelector(".guage");

function setGuageValue(guage, value){
	if(value < 0 || value > 1){
		return;
	}

	guage.querySelector(".guage__fill").style.transform = `rotate(${value / 2}turn)`;
	guage.querySelector(".guage__cover").textContent = `${Math.round(value * 100)}%`;
}

function findValue(){
	// this is where I need something like this:
	// value_1 = the number that goes into guage
	// then another function to find the value for the second guage
	value = Math.random();  // generate a random number between 0 and 1
	return value;
}

function displayMessage(){

	if(value < 0.25){
		document.getElementById("message").innerHTML = "Engagement level is high.";
	}
	else if(value >= 0.25 && value <= 0.75){
		document.getElementById("message").innerHTML = "Moderate level of boredom.";
	}
	else{
		document.getElementById("message").innerHTML = "CAUTION: Boredom level is off the charts!";
	}

}

// the value from abusive language percentage needs to be passed in this function
setGuageValue(guageElement, findValue());
displayMessage();

