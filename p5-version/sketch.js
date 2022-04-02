function setup() {
  createCanvas(600, 600);

  textAlign(CENTER);
  background(200);
  sel = createSelect();
  sel.position(10, 10);
  sel.option('Sierpiński triangle');
  sel.option('Sierpiński hexagon');
  sel.selected('Sierpiński triangle');
  sel.changed(mySelectEvent);
}

var attractors = get_sierpinski_triangle_attractors();
var y_offset = 0.5;

function mySelectEvent() {
  let item = sel.value();
  background(200);
  if (item == 'Sierpiński triangle') {
    attractors = get_sierpinski_triangle_attractors();
    y_offset = 0.5;
  } else {
    attractors = get_sierpinski_hexagon_attractors();
    y_offset = 1.0;
  }
}

function draw() {
    result = ifsp(attractors, 1000);
    for (i = 0; i < result[0].length; i++) {
      x = Math.round(200 * (result[0][i] + 1.0))
      y = Math.round(200 * (result[1][i] + y_offset))
      point(x, y);
    }
}
