var hasClicked = false;
var oldX = null;
var oldY = null;

// retrieve canvas
var c = document.getElementById('playground');

// instantiate CanvasRenderingContext2D
var ctx = c.getContext("2d");

// clear button

var clear_button = document.getElementById('clear');

clear_button.addEventListener("click", function () {
  ctx.clearRect(0, 0, 600, 600);
  hasClicked = false;
  oldX = null;
  oldY = null;
  console.log("Cleared canvas!")
});

// draw

c.addEventListener("click", function (e) {
  console.log(e);

  // we use offsetX and offsetY to get the coords of the click relative to the upper-left of the canvas, rather than the upper-left of the window
  var x = e.offsetX;
  var y = e.offsetY;

  if (!hasClicked) {
    ctx.beginPath();
    hasClicked = true;
    ctx.moveTo(x, y);
    oldX = x;
    oldY = y;
  } else {
    ctx.beginPath();
    ctx.moveTo(oldX, oldY);
    ctx.lineTo(x, y);
    oldX = x;
    oldY = y;
    ctx.stroke();
  }
  drawDot(x, y, 5);

  // prevents default action upon clicking canvas
  e.preventDefault();
});

var drawDot = function (x, y, r) {
  ctx.beginPath();
  ctx.ellipse(x, y, r, r, 0, 0, Math.PI * 2);
  ctx.fill();
};
