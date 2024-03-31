// Independent Variable (X)
const X = tf.tensor1d([1, 2, 3, 4, 5, 6]);

// Dependent Variable (y)
const y = tf.tensor1d([100, 200, 300, 400, 500, 600]);

// Weight (w)
const w = tf.variable(tf.scalar(Math.random()));

// Bias (b)
const b = tf.variable(tf.scalar(Math.random()));

// Getting the output as y_hat = wx + b
function predict(X, w, b) { 
	y_hat = w.mul(X).add(b);
	return y_hat;
}

// Creating our loss function as Mean Squared Error
// MSE = (Predicted Output - Actual Output)^2 / Number of data points
function loss(y_hat, y) { 
   error = y_hat.sub(y).square().mean(); 
   return error; 
}

// Creating a function for model training
function train(X, y, w, b) {

	// Initializing the optimizer as Stochastic Gradient Descent
	optimizer = tf.train.sgd(0.05);

	// Minimizing the loss
	optimizer.minimize(function() {
		y_hat = predict(X, w, b);
		stepLoss = loss(y_hat, y);
		return stepLoss;
	});
}

// Training for 2000 steps
for (i = 0; i < 10000; i++) {
	train(X, y, w, b);
}

// Getting a prediction before training
predict(X, w, b).print();