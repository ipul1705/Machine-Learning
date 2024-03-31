// Creating two 1D tensors
const t1 = tf.tensor1d([10, 11, 12, 13]);
const t2 = tf.tensor1d([1, 2, 3, 4]);

// Adding two tensors t2 + t1
t2.add(t1).print();

// Subtracting two tensors t2 - t1
t2.sub(t1).print();

// Multiplying two tensors t1 x t2
t1.mul(t2).print();

// Dividing one tensor by another t1 / t2
t1.div(t2).print();

// Squaring each element of a tensor
t2.square().print();

// Finding the mean of a tensor
t2.mean().print();


coba = t1.add(t2.mean());
coba.sub(t2).print();

// Concatenating operations
t1.add(t2.mean()).sub(t2).print();

