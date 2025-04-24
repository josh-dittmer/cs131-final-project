import keras

class MultilayerPerceptronModel:
    def __init__(self, num_cols, width, depth, learning_rate):
        self.model = self.build_model(num_cols, width, depth)

        self.model.compile(
            optimizer=keras.optimizers.Adam(
                learning_rate=learning_rate
            ),
            loss='mse'
        )

    def build_model(self, num_cols, width, depth):
        model = keras.Sequential(layers=None, trainable=True, name='MLP')

        # input layer
        model.add(keras.layers.Input(shape=(num_cols,)))

        # hidden layer
        for _ in range(depth):
            model.add(keras.layers.Dense(units=width, activation='relu'))

        # output layer
        model.add(keras.layers.Dense(1, activation='linear'))

        return model
    
    def fit(self, x_train, y_train, batch_size, epochs):
        history = self.model.fit(
            x=x_train,
            y=y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_split=0.1
        )

        train_loss = history.history['loss'][-1]
        val_loss = history.history['val_loss'][-1]

        return (train_loss, val_loss)
    
    def test(self, x_test, y_test):
        return self.model.evaluate(x_test, y_test)