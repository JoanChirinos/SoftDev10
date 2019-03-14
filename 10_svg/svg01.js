// Clyde "Thluffy" Sinclair
// SoftDev pd0
// K09 -- basic SVG work
// 2019-03-13w


var pic = document.getElementById("vimage");
var wipe = document.getElementById("but_clear");


var onDot = function (x, y) {

  var children = pic.children;
  //  console.log(children);
  var i;
  for (i = 0; i < children.length; i++) {
    var child = children.item(i);
    console.log(child);
    let cx = child.getAttribute("cx");
    let cy = child.getAttribute("cy");
    //    console.log('x: ' +x);
    //    console.log('y: ' + y);
    //    console.log('cx: ' + cx);
    //    console.log('cy: ' + cy);
    //    console.log(Math.pow(cx - x, 2) + Math.pow(cy - y, 2));
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

pic.addEventListener("click", createDot);


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
    lastX = null;
    lastY = null;
  });
