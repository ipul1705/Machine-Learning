// Independent Variable (X)
const X = tf.tensor1d([1, 2, 3, 4, 5, 6]);

// Dependent Variable (y)
const y = tf.tensor1d([100, 200, 300, 400, 500, 600]);

async function LinearRegressionModel(X, y){

    // Using the sequential model for stacking up layers
    linearModel = tf.sequential({
            layers: [
                tf.layers.dense({inputShape: [1], units: 1, useBias: 'True'}),
            ]
    });

    // Defining the loss and optimizer
    lossAndOptimizer = {
      loss: "meanSquaredError",
      optimizer: tf.train.sgd(0.005)
    };

    // Compiling the model
    linearModel.compile(lossAndOptimizer);

    // Start the model training!
    await linearModel.fit(X, y, 
        {epochs: 2000, 
        callbacks: {
            onEpochEnd: async (epoch, logs) => {
                console.log("Epoch:" + epoch + " Loss:" + logs.loss);
                await tf.nextFrame();
            }
        }
    });

    // Printing the prediction
    linearModel.predict(X).print();
}

LinearRegressionModel(X, y);



