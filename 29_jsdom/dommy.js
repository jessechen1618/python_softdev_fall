var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e.target.innerHTML;
};

var removeItem = function(e) {
  e.target.remove();
}

var lis = document.getElementsByTagName("li");

for (var i=0; i<lis.length;i++){
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', function(){
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!";
  });
  lis[i].addEventListener('click', removeItem);
}

var addItem = function(e){
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  item.addEventListener('mouseover', changeHeading);
  item.addEventListener('mouseout', function(){
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!";
  });
  item.addEventListener('click', removeItem);
  list.appendChild(item);
}

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n){
  if(n<2) return 1;
  return fib(n-1) + fib(n-2);
};

var addFib = function(e){
  var fiblist = document.getElementById("fiblist");
  var item = document.createElement("li");
  var children = fiblist.children;
  //console.log(children.length)
  item.innerHTML = fib(children.length);
  //console.log(item.innerHTML)
  fiblist.appendChild(item);
};

var addFib2 = function(e){
  var fiblist = document.getElementById("fiblist");
  var item = document.createElement("li");
  var children = fiblist.children;
  if (children.length < 2) item.innerHTML = "1";
  else{
    item.innerHTML = parseInt(children[children.length-2].innerHTML) + parseInt(children[children.length-1].innerHTML);
  }
  fiblist.appendChild(item)
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib2)
