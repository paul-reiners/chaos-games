function setup() {
  createCanvas(600, 600);
}


function draw() {
    let attractors = get_sierpinski_attractors();
    result = ifsp(attractors, 1000);
    for (i = 0; i < result[0].length; i++) {
      x = Math.round(200 * (result[0][i] + 1.0))
      y = Math.round(200 * (result[1][i] + 0.5))
      point(x, y);
    }
}
