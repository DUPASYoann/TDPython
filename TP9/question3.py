from TP9.main import *

if __name__ == "__main__":
    # Question 4
    _list_dataframe = [pd.read_excel("DAT_XLSX_EURUSD_M1_2019.xlsx", header=None)]
    print(_list_dataframe[0].dtypes)
    # _list_dataframe.append(pd.read_excel("DAT_XLSX_EURUSD_M1_2019.xlsx", header=None))

    _batch_size = 512
    _epochs = 3

    _all_features, _all_target = prepare_dataset(_list_dataframe, 120)
    _model = build_model(_all_features, _all_target, _batch_size, _epochs)
    _result = _model.predict(_all_features[::10000])
    print(_result)