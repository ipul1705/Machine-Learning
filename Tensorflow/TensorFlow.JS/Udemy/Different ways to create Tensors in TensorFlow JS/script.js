// Creates a Tensor with all elements as 1.
tf.ones([2, 2]).print();

// Creates a Tensor with all elements as 0.
tf.zeros([2, 2]).print();

// Creates an identity matrix.
tf.eye(3,3).print();

// Creates a tf.Tensor filled with a scalar value.
tf.fill([2, 2], 4).print();

// Return an evenly spaced sequence of numbers.
tf.linspace(0, 9, 5).print();

// Creates a new tf.Tensor1D filled with the numbers 
// in the range provided.
tf.range(0, 9, 2).print();

// Creates a new variable with the provided initial value.
const x = tf.variable(tf.tensor1d([1, 2, 3]));

x.print();

x.assign(tf.tensor1d([4, 5, 6]));

x.print();
