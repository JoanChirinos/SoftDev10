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

  var x = e.clientX - r.left;
  var y = e.clientY - r.top;
  if (draw_state === "rect") {
    console.log("drawing rect at (" + x + ", " + y + ")");
    ctx.fillRect(x - 25, y - 25, 50, 50);
  } else {
    console.log("drawing ellipse at (" + x + ", " + y + ")");
    ctx.beginPath();
    ctx.arc(x, y, 25, 0, 2 * Math.PI);
    ctx.fill();
  }
});
