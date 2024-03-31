// Scalar
console.log("Scalar");
tf.scalar(3).print();

// 1D Tensor
console.log("1D Tensor");
tf.tensor1d([1, 2, 3, 4]).print();

// 2D Tensor
console.log("2D Tensor");
tf.tensor2d([[1, 2], [3, 4]]).print();

// 3D Tensor
console.log("3D Tensor");
tf.tensor3d([[[1], [2]], [[3], [4]]]).print();

// nD Tensor
console.log("nD Tensor");
tf.tensor([[1, 2], [3, 4]]).print();