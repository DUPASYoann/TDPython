import pandas as pd
from matplotlib import pyplot as plt
from TP9.question3 import *


def copie_carbone(value_before_value, value):
    return 1 if value_before_value < value else 0


def compile_copie_carbone(dataframe):
    pred = [copie_carbone(dataframe[1][x], dataframe[4][x]) for x in range(0, len(dataframe)-1)]
    gt = [(lambda x, y: 1 if x < y else 0)(dataframe[1][x], dataframe[4][x]) for x in range(1, len(dataframe))]
    accuracy = [(lambda x, y: 1 if x - y == 0 else 0)(pred[x], gt[x]) for x in range(len(pred))]
    print(sum(accuracy)/len(accuracy)*100)


if __name__ == "__main__":

    # Question 1
    _dataframe = pd.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", header=None)
    print("READING COMPLET")
    plt.plot(_dataframe[0], _dataframe[4])
    plt.show()

    # Question 2
    compile_copie_carbone(_dataframe)
