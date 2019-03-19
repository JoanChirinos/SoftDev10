//Joan Chirinos
//SoftDev pd08
//K10 -- Ask Circles [Change || Die] …While On The Go
//2019-03-18


var pic = document.getElementById("vimage");
var wipe = document.getElementById("but_clear");
var move = document.getElementById("but_move");

var moving = false;
var requestID;

var onDot = function (x, y) {

  var children = pic.children;
  //  console.log(children);
  var i;
  for (i = 0; i < children.length; i++) {
    var child = children.item(i);
    console.log(child);
    let cx = child.getAttribute("cx");
    let cy = child.getAttribute("cy");
    if (Math.pow(cx - x, 2) + Math.pow(cy - y, 2) <= 400) {
      return true;
    }
  }
  return false;
}

var createDot = function (e) {
  console.log("running . . .");
  e.stopPropagation();
  e.preventDefault();

  //store click location, relative to "canvas"
  var x = e.offsetX;
  var y = e.offsetY;

  if (onDot(x, y)) {
    console.log('yeeting');
  } else {
    var newdot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    newdot.setAttribute("fill", "red");
    newdot.setAttribute("cx", x);
    newdot.setAttribute("cy", y);
    newdot.setAttribute("r", 20)
    newdot.setAttribute("dx", 1)
    newdot.setAttribute("dy", -1)

    pic.appendChild(newdot);
    newdot.addEventListener('click', dotchange)
  }
}

var dotchange = function (e) {
  console.log('DOT');
  console.log(e);
  var circle = e.target;
  if (circle.getAttribute("fill") == "red") {
    circle.setAttribute("fill", "green");
  } else {
    circle.setAttribute("fill", "red");
    circle.setAttribute("cx", Math.floor(Math.random() * 460) + 20);
    circle.setAttribute("cy", Math.floor(Math.random() * 460) + 20);
    e.stopImmediatePropagation();
  }
};

var movehelper = function (n) {
  if (n.getAttribute('cx') >= 480 || n.getAttribute('cx') <= 20) {
    n.setAttribute('dx', n.getAttribute('dx') * -1);
  }
  if (n.getAttribute('cy') >= 480 || n.getAttribute('cy') <= 20) {
    n.setAttribute('dy', n.getAttribute('dy') * -1);
  }
  n.setAttribute('cy', n.getAttribute('cy') + n.getAttribute('dy'));
  n.setAttribute('cx', n.getAttribute('cx') + n.getAttribute('dx'));
};

var dotmove = function (e) {
  var children = pic.children;
  var i;
  for (i = 0; i < children.length; i++) {
    var child = children.item(i);
    movehelper(child);
  }
  requestID = requestAnimationFrame('dotmove');
};

pic.addEventListener("click", createDot);
move.addEventListener('click', dotmove);


//sequentially remove all dots and lines from "canvas"
wipe.addEventListener(
  "click",
  function () {
    var fc = pic.firstChild;
    while (fc) {
      console.log("removing " + fc + "...");
      pic.removeChild(fc);
      fc = pic.firstChild;
    }
    moving = false;
  });
