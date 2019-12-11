var foo = function(){
  console.log("foo");
}

var fact = function(n){
  if(n < 2){
    return 1;
  }
  return n * fact(n-1);
}

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
  min = Math.min(a,b);
  for(i = min; i > 0; i--){
    if(a%i == 0 && b%i == 0){
      return i;
    }
  }
}

listOfStudents = ["alice","bob","carl","dave"]
var randomStudent = function(students){
  return students[Math.floor(Math.random() * students.length)];
}
