from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import keras as kp
import tensorflow as tf
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Conv1D, BatchNormalization
from tensorflow.keras.layers import MaxPooling1D
from sklearn import preprocessing


def prepare_dataset(list_dataframe, h, limit=-1):

    all_features_raw = []
    all_target = []

    for dataframe in list_dataframe:
        for i in range(1, 5):
            all_features_raw.append(dataframe[i])
        all_target.append([(lambda x, y: 1 if x < y else 0)(data[2], data[5]) for data in dataframe.itertuples()])

    all_features_raw = np.array(all_features_raw)
    all_target = np.array(all_target)

    all_features_raw = np.reshape(all_features_raw, (all_features_raw.shape[1], all_features_raw.shape[0]))
    all_target = np.reshape(all_target, (all_target.shape[1], all_target.shape[0]))

    # Division par jeu de données

    if limit == -1:
        limit = all_features_raw.shape[0]
        print(limit)

    all_features = []

    for i in range(h, limit-1):
        temp = preprocessing.scale(all_features_raw[i-h:i:])
        temp = preprocessing.normalize(temp)
        all_features.append(temp.tolist())

    all_features = np.array(all_features)
    all_target = all_target[h+1:limit]

    return all_features, all_target


def build_model_LSTM(train_x, train_y, batch_size, epochs):
    n_time_steps, n_features, n_outputs = train_x.shape[1], train_x.shape[2], train_y.shape[1]
    model = kp.Sequential()
    model.add(LSTM(units=256, input_shape=(n_time_steps, n_features)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(n_outputs))
    model.add(tf.keras.layers.ReLU(max_value=1, negative_slope=0, threshold=0))
    model.compile(loss='mse', optimizer="adam", metrics=['binary_accuracy'],)
    # fit network
    model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, verbose=1, validation_split=0.2)
    return model


def build_model_cnn(train_x, train_y, batch_size, epochs):
    n_time_steps, n_features, n_outputs = train_x.shape[1], train_x.shape[2], train_y.shape[1]

    model = kp.Sequential()
    model.add(Conv1D(filters=64, kernel_size=2, activation="relu", input_shape=(n_time_steps, n_features)))
    model.add(Dropout(0.2))
    model.add(MaxPooling1D(pool_size=2, strides=None))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(Flatten())
    model.add(Dense(50))
    model.add(Dense(n_outputs, activation="relu"))
    model.compile(loss='mse', optimizer="adam", metrics=['binary_accuracy'],)
    # fit network
    model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, verbose=1, validation_split=0.8)
    return model


def copie_carbone(value_before_value, value):
    return 1 if value_before_value < value else 0


def compile_copie_carbone(dataframe):
    pred = [copie_carbone(dataframe[1][x], dataframe[4][x]) for x in range(0, len(dataframe)-1)]
    gt = [(lambda x, y: 1 if x < y else 0)(dataframe[1][x], dataframe[4][x]) for x in range(1, len(dataframe))]
    accuracy = [(lambda x, y: 1 if x - y == 0 else 0)(pred[x], gt[x]) for x in range(len(pred))]
    print(sum(accuracy)/len(accuracy)*100)


if __name__ == "__main__":

    # # Question 1
    # _dataframe = pd.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", header=None)
    # print("READING COMPLET")
    # plt.plot(_dataframe[0], _dataframe[4])
    # plt.show()
    #
    # # Question 2
    # compile_copie_carbone(_dataframe)

    # Question 4
    _list_dataframe = [pd.read_excel("DAT_XLSX_EURUSD_M1_2019.xlsx", header=None)]
    print(_list_dataframe[0].dtypes)
    # _list_dataframe.append(pd.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", header=None))
    # une seul suffit

    _batch_size = 16
    _epochs = 3

    _all_features, _all_target = prepare_dataset(_list_dataframe, 120)
    _model_cnn = build_model_cnn(_all_features, _all_target, _batch_size, _epochs)
    _model_lstm = build_model_LSTM(_all_features, _all_target, _batch_size, _epochs)
