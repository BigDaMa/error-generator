from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import random
import numpy as np


class EEG_Loader(object):
    def __init__(self):
        pass

    def load(self):
        data = pd.read_csv("./datasets/EEG_data_Epileptic_Seizure_Recognition.csv")
        y = data.y.values
        data = data.drop(['Unnamed: 0'], axis=1)

        del data["y"]  # remove rings from data, so we can convert all the dataframe to a numpy 2D array.
        data2=data.iloc[:, [9, 52, 168, 33, 157, 107, 159, 1, 54, 166]]
        X = data2.values.astype(np.float)


        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=4)

        return x_train, x_test, y_train, y_test
