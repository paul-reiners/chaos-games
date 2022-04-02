function setup() {
  createCanvas(400, 400);
}

function ifsp(attractors, n) {
    function w(x, attractor) {
        compression_ratio = attractor['compression_ratio'];
        return [compression_ratio * x[0] + (1.0 - compression_ratio) * attractor['point'][0], 
                compression_ratio * x[0] + (1.0 - compression_ratio) * attractor['point'][0]];
      }

    xs = [0.0] * n;
    ys = [0.0] * n;
    x = attractors[0]['point'];
    m = len(attractors);
    for (i = 0; i < n; i++) {
        xs[i] = x[0];
        ys[i] = x[1];
        prob_sum = 0.0;
        attractor_index = None;
        r = random.random();
        for i in range(m) {
            prob_sum += attractors[i]['probability'];
            if (prob_sum >= r) {
                if (prob_sum > r) {
                    attractor_index = i - 1
                } else {
                    attractor_index = i
                }

                break;
            }
        }
        x = w(x, attractors[attractor_index]);
      }
     return [xs[20:], ys[20:]];
  }


function draw() {
  v_1 = [-1.0, 0.0];
  v_2 = [1.0, 0.0];
  v_3 = [0.0, Math.sqrt(3.0)];
  vs = [v_1, v_2, v_3];

    let attractors = 
      [{'point': vs[0], 'compression_ratio': 0.5, 'probability': 1.0 / 3.0}, 
       {'point': vs[1], 'compression_ratio': 0.5, 'probability': 1.0 / 3.0}, 
       {'point': vs[2], 'compression_ratio': 0.5, 'probability': 1.0 / 3.0}];
    ifsp(attractors, 1000);
}