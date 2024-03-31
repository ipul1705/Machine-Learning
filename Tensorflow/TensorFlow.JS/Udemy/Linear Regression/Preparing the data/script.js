// Independent Variable (X)
const X = tf.tensor1d([1, 2, 3, 4, 5, 6]);

// Dependent Variable (y)
const y = tf.tensor1d([100, 200, 300, 400, 500, 600]);

// Weight (w)
const w = tf.variable(tf.scalar(Math.random()));

// Bias (b)
const b = tf.variable(tf.scalar(Math.random()));

// Looking at the tensors
X.print();
y.print();
w.print();
b.print();