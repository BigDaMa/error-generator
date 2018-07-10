# import API_error_generator
import numpy as np
import csv
import pandas
import random
dataset_dataframe_version=None
import chainer, chainer.links as L,chainer.functions as F
from chainer import Variable
import difflib


def read_csv_dataset(dataset_path, header_exists=True):
    """
    The method reads a dataset from a csv file path.
    """
    global dataset_dataframe_version
    dataset_dataframe_version = pandas.read_csv(dataset_path)
    if header_exists:
        dataset_dataframe = pandas.read_csv(dataset_path, sep=",", header="infer", encoding="utf-8", dtype=str,
                                            keep_default_na=False, low_memory=False)

        dataset_dataframe = dataset_dataframe.apply(lambda x: x.str.strip())
        return [dataset_dataframe.columns.get_values().tolist()] + dataset_dataframe.get_values().tolist()
    else:
        dataset_dataframe = pandas.read_csv(dataset_path, sep=",", header=None, encoding="utf-8", dtype=str,
                                            keep_default_na=False)


        dataset_dataframe = dataset_dataframe.apply(lambda x: x.str.strip())
        return dataset_dataframe.get_values().tolist()





if __name__=="__main__":

    dataset = read_csv_dataset("dataset/address_10_ground_truth.csv")


