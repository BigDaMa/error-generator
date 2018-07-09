# import API_error_generator
import numpy as np
import csv
import pandas
import random

dataset_dataframe_version=None
import chainer, chainer.links as L,chainer.functions as F
from chainer import Variable


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





def noise_gaussian(col_name,percentage,noise_rate):
    implicit_missing_value_history = []
    number = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)


    print("---------Change according to gaussian noise method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in implicit_missing_value_history:
            random_value = random.randint(1, len(dataset) - 1)
        implicit_missing_value_history.append(random_value)
        temp = dataset[random_value][col]
        temp_array = np.array([temp]).astype(np.float32)
        # batch,dim = v.data.shape[0],v.data.shape[1]
        batch=1
        ones = Variable(np.ones((batch), dtype=np.float32))
        new_value=F.gaussian(temp_array, noise_rate * ones)


        dataset[random_value][col] = new_value
        print("row: {} col: {} : '{}' changed to {}  ".format(random_value, col, temp,new_value))
    return dataset




if __name__=="__main__":

    dataset = read_csv_dataset("/home/milad/Desktop/error-generator/test.csv")
    noise_gaussian("salary",50,-10)
    print(dataset)


