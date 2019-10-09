// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
// - { { {    0. COMMENTS    } } } - 
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// single-line comment :  this is a comment, so it is not read by the computer
/* multi-line ocmment : these are also comments
a
b
c
	d
		e
	f
g
*/

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
// - { { {    1. PRINTING    } } } - 
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
console.log("Hello World!"); // console
document.write("Hello World Again!"); // HTML body

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
// - { { {    2. VARIABLES    } } } - 
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
var name = "Michael Leung";
var age = 19;
var bool = true;

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
// - { { {    3. IF STATEMENTS    } } } - 
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if (age === "19"){
	console.log("You're my age!")
}
else if (age > 19){
	console.log("You're older than me!");
} 
else{
	console.log("You're younger than me!");
}

var age_comparison = ( age == 19 ? "same age" : "different age"); // ternary operator
console.log(age_comparison);

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
// - { { {    4. LOOPS    } } } - 
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
for (var i = 0; i < 5; i++){
	console.log("i = " + i);
}

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
// - { { {    5. ARRAYS    } } } - 
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
var names 	= ["Agatha", 	"Gertrude", 	"Pearl"];
var heights = [124.6,		148.4, 			165.7];

document.write("<br/><br/>");
for (var i = 0; i < heights.length; i++){
	document.write("Name  : " + names[i] + "<br/>");
	document.write("Height : " + heights[i] + " cm<br/><br/>");
}


// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
// - { { {    6. FUNCTIONS    } } } - 
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
function isHomeworkDone (mood, urgent){
	return (mood == "good" && urgent);
}
console.log("isHomeworkDone : " + isHomeworkDone ("Good", true));

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
// - { { {    7. OBJECTS    } } } - 
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
function Pet(age){ // prototype object constructor
	this.animal = "doggo";
	this.breed = "puggerino";
	this.pet_name ="Sir Puggington";
	this.age = age;
	this.address = {
		street: "Bone Street",
		city: "Snack City"
	}
	this.info = function(){ // class functions
		return(	"Animal : " + this.animal + "<br/>"
					 +	"Breed : " + this.breed + "<br/>"
					 +	"Pet Name : " + this.pet_name + "<br/>"
					 +	"Age : " + this.age + "<br/>"
					 +	"Street : " + this.address.street + "<br/>"
					 +	"City : " + this.address.city + "<br/>");
	}
}

var myPet = new Pet( 10 );
document.write( myPet.info() );
