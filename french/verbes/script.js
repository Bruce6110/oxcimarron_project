
function toggleIrregulars() {

	var irregs = document.getElementsByClassName("irreg");
	var i;
	for (i = 0; i < irregs.length; i++) {
		var x = irregs[i];

		if (x.classList) {

			x.classList.toggle("highlighted");
			console.log(x.classList);
		} else {
			// For IE9
			console.log("ie9");
			var classes = x.className.split(" ");
			var i = classes.indexOf("highlighted");

			if (i >= 0)
				classes.splice(i, 1);
			else
				classes.push("highlighted");
			x.className = classes.join(" ");
		}
	}
}

highlighter.addEventListener("click", toggleIrregulars);//adds listener to input event for highlighter object


//tip: define functions as constants:
/*
	const myFunc=()==>{
		alert("hello");
	}
*/
//Closures:  when a function runs only once, but the child scope always has access to the parent scope. Not vice-versa*/

// Currying:
const multiply = (a, b) => a * b;
const curriedMultiply = (a) => (b) => a * b;
const multiplyBy5 = curriedMultiply(5);

curriedMultiply(3)(4); //this returns 3*4.   (?)
//currying takes the process of calling a mult-argument function, one argument at a time

//Compose: the act of putting two functions together such that the output of the 

const compose = (f, g) => (a) => (f(g(a)));

const sum = (num) => num + 1;
compose(sum, sum)(5);   //this returns 7

//functional purity: avoid side effects and always doing a return.  Creates determinism. ie, given inputs always produce same values.