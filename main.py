import pandas as pd
from sklearn.model_selection import train_test_split

from models.multilayer_perceptron import MultilayerPerceptronModel

def load_data():
    df = pd.read_csv('data/winequality-processed.csv', delimiter=';')
    
    x_df = df.drop('quality', axis=1)
    y_df = df['quality']

    x_train, x_test, y_train, y_test = train_test_split(
        x_df,
        y_df,
        test_size=0.1,
        shuffle=True,
        random_state=77
    )

    return (x_train, x_test, y_train, y_test)

def main():
    x_train, x_test, y_train, y_test = load_data()

    # train mlp
    mlp = MultilayerPerceptronModel(x_train.shape[1], 32, 2, 0.0000001)

    train_loss, val_loss = mlp.fit(x_train, y_train, 4, 50)
    test_loss = mlp.test(x_test, y_test)

    print(f"RESULTS FOR MLP: TRN {train_loss} / VAL {val_loss} / TEST {test_loss}")

    # TODO: plot mlp results

    # TODO: train mlr

    # TODO: plot mlr results

    # TODO: train random forest

    # TODO: plot random forest results

if __name__ == '__main__':
    main()