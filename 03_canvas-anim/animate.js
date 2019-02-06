// state vars
var requestID;
var radius = 0;
var growing = 0;

// canvasbois
var c = document.getElementById('playground');
var ctx = c.getContext('2d');

// buttons
var dotButton = document.getElementById('circle');
var stopButton = document.getElementById('stop');

var clear = function () {
  ctx.clearRect(0, 0, c.width, c.height);
};

var drawDot = function (id) {
  
  clear();
  
  if (growing == 0) {
    growing = 1;
  }
  if (radius >= c.width / 2) {
    growing = -1;
  }
  else if (radius <= 0) {
    growing = 1;
  }
  if (growing == 1) {
    radius += 1;
  }
  else if (growing == -1) {
    radius -= 1;
  }
  
  // draw the dot
  ctx.beginPath();
  ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  
  requestID = window.requestAnimationFrame(drawDot);
};

var stopIt = function () {
  console.log(requestID);
  window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener('click', drawDot);

stopButton.addEventListener('click', stopIt);