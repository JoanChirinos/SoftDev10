var clear_button = document.getElementById('but_clear');

var pic = document.getElementById('vimage');

var oldX = null;
var oldY = null;

var draw_circle = function (p, x, y, r, color) {
  var t = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  t.setAttribute('cx', x);
  t.setAttribute('cy', y);
  t.setAttribute('r', r);
  t.setAttribute('fill', color);
  t.setAttribute('stroke', 'black');
  p.appendChild(t);
}

var draw_line = function (p, x0, y0, x1, y1, color) {
  var t = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  t.setAttribute('x1', x0);
  t.setAttribute('y1', y0);
  t.setAttribute('x2', x1);
  t.setAttribute('y2', y1);
  t.setAttribute('stroke', color);
  p.appendChild(t);
};

pic.addEventListener('click', function (e) {
  console.log(e);
  var x = e.offsetX;
  var y = e.offsetY;
  if (oldX != null && oldY != null) {
    draw_line(pic, oldX, oldY, x, y, 'green');
  }
  oldX = x;
  oldY = y;
  draw_circle(pic, x, y, 25, 'red');
});

clear_button.addEventListener('click', function () {
  while (pic.firstChild) {
    pic.removeChild(pic.firstChild);
    oldX = null;
    oldY = null;
  }
});
