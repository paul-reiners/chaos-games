function setup() {
  createCanvas(600, 600);
}


function w(x, attractor) {
    let compression_ratio = attractor.compression_ratio;
    return [compression_ratio * x[0] + (1.0 - compression_ratio) * attractor['point'][0], 
            compression_ratio * x[1] + (1.0 - compression_ratio) * attractor['point'][1]];
}



function ifsp(attractors, n) {
    xs = new Array(n).fill(0);
    ys = new Array(n).fill(0);
    x = attractors[0]['point'];
    m = attractors.length;
    for (i = 0; i < n; i++) {
        xs[i] = x[0];
        ys[i] = x[1];
        prob_sum = 0.0;
        attractor_index = null;
        r = Math.random();
        for (j = 0; j < m; j++) {
            prob_sum += attractors[j]['probability'];
            if (prob_sum >= r) {
                attractor_index = j

                break;
            }
        }
        x = w(x, attractors[attractor_index]);
      }
     
     return [xs.slice(20), ys.slice(20)];
  }


function draw() {
  v_1 = [-1.0, 0.0];
  v_2 = [1.0, 0.0];
  v_3 = [0.0, Math.sqrt(3.0)];
  vs = [v_1, v_2, v_3];

    let attractors = 
      [{"point": vs[0], "compression_ratio": 0.5, "probability": 1.0 / 3.0}, 
       {"point": vs[1], "compression_ratio": 0.5, "probability": 1.0 / 3.0}, 
       {"point": vs[2], "compression_ratio": 0.5, "probability": 1.0 / 3.0}];
    result = ifsp(attractors, 1000);
    for (i = 0; i < result[0].length; i++) {
      x = Math.round(200 * (result[0][i] + 1.0))
      y = Math.round(200 * (result[1][i] + 0.5))
      point(x, y);
    }
}