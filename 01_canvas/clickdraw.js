var draw_state = "dot";

// retrieve canvas
var c = document.getElementById('slate');

// instantiate CanvasRenderingContext2D
var ctx = c.getContext("2d");

// clear button

var clear_button = document.getElementById('clear');

clear_button.addEventListener("click", function () {
  ctx.clearRect(0, 0, 600, 600);
  console.log("Cleared canvas!")
});

// change draw mode button

var draw_mode_button = document.getElementById('switch_mode');

draw_mode_button.addEventListener('click', function () {
  if (draw_state === "dot") {
    draw_state = "rect"
  } else {
    draw_state = "dot";
  }
  update_state_message();
});

// draw state message

var update_state_message = function () {
  document.getElementById('mode').innerHTML = draw_state;
};

// draw

c.addEventListener("click", function (e) {
  console.log(e);

  var r = c.getBoundingClientRect();

  // we use offsetX and offsetY to get the coords of the click relative to the upper-left of the canvas, rather than the upper-left of the window
  var x = e.offsetX;
  var y = e.offsetY;
  if (draw_state === "rect") {
    console.log("drawing rect at (" + x + ", " + y + ")");
    ctx.fillRect(x, y, 50, 50);
  } else {
    console.log("drawing ellipse at (" + x + ", " + y + ")");
    // starts a drawing path, which can later be filled using ctx.fill()
    ctx.beginPath();
    ctx.arc(x, y, 25, 0, 2 * Math.PI);
    ctx.fill();
  }
  // prevents default action upon clicking canvas
  e.preventDefault();
});
