var foo = function(){
  console.log("foo");
}

var fact = function(n){
  if(n < 2){
    return 1;
  }
  return n * fact(n-1);
}

var fact2 = function(){
  console.log(fact());
}
//fact button stuff:
fact_button = document.getElementById("fact");
fact_arg = document.getElementById("fact_arg");

fact_button.addEventListener("click", fact2);

var fib = function(n){
  if(n == 0){
    return 0;
  }
  if(n <= 2){
    return 1;
  }
  return fib(n-1) + fib(n-2)
}

var gcd = function(a,b){
  if(a%b == 0) {
    return b;
  }
  return gcd2(b,a%b);
}

listOfStudents = ["alice","bob","carl","dave"]
var randomStudent = function(students){
  return students[Math.floor(Math.random() * students.length)];
}
