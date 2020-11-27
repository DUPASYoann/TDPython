import pandas as pd
import numpy as np
import keras as kp
import tensorflow as tf
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Conv1D
from keras.layers import MaxPooling1D
from keras.layers import LayerNormalization


def prepare_dataset(list_dataframe, h, limit=-1):

    all_features_raw = []
    all_target = []

    for dataframe in list_dataframe:
        for i in range(1, 5):
            all_features_raw.append(dataframe[i])
        all_target.append([(lambda x, y: 1 if x < y else 0)(data[2], data[5]) for data in dataframe.itertuples()])

    all_features_raw = np.array(all_features_raw)
    all_target = np.array(all_target)

    print(np.shape(all_features_raw))
    print(np.shape(all_target))

    all_features_raw = np.reshape(all_features_raw, (all_features_raw.shape[1], all_features_raw.shape[0]))
    all_target = np.reshape(all_target, (all_target.shape[1], all_target.shape[0]))

    # Division par jeu de données

    if limit == -1:
        limit = all_features_raw.shape[0]
        print(limit)

    all_features = []

    for i in range(h, limit-1):
        print(i)
        all_features.append(all_features_raw[i-h:i:].tolist())

    all_features = np.array(all_features)
    all_target = all_target[h+1:limit]
    print(np.shape(all_target))

    return all_features, all_target


def load_dataset(all_features, all_target, taille_val=0.2):
    index = int(taille_val*len(all_features))
    train_x = all_features[:-index]
    test_x = all_features[-index:]
    train_y = all_target[:-index]
    test_y = all_target[-index:]

    return train_x, train_y, test_x, test_y


def build_model(train_x, train_y, batch_size, epochs):
    n_time_steps, n_features, n_outputs = train_x.shape[1], train_x.shape[2], train_y.shape[1]
    print(np.shape(train_x))
    print(np.shape(train_y))
    model = kp.Sequential()
    model.add(LayerNormalization(axis=1, input_shape=(n_time_steps, n_features)))
    model.add(Conv1D(filters=64, kernel_size=4, activation='relu'))
    model.add(Conv1D(filters=64, kernel_size=4, activation='relu'))
    model.add(Dropout(0.2))
    model.add(MaxPooling1D(pool_size=2, strides=None))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(1, activation='relu'))
    model.compile(loss='mse', optimizer='adam', metrics=['binary_accuracy'])
    # fit network
    model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, verbose=1)
    return model


if __name__ == "__main__":

    _list_dataframe = [pd.read_excel("DAT_XLSX_EURUSD_M1_2019.xlsx", header=None)]
    print(_list_dataframe[0].dtypes)
    # _list_dataframe.append(pd.read_excel("DAT_XLSX_EURUSD_M1_2019.xlsx", header=None))

    _batch_size = 64
    _epochs = 10

    _all_features, _all_target = prepare_dataset(_list_dataframe, 120)
    _train_x, _train_y, _test_x, _test_y = load_dataset(_all_features, _all_target)
    _model = build_model(_train_x, _train_y, _batch_size, _epochs)
    _, accuracy = _model.evaluate(_test_x, _test_y, batch_size=_batch_size, verbose=1)
    _result = _model.predict(_test_x)
    print(_result)
    print(accuracy)
