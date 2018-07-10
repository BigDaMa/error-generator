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



def implicit_missing_value_mean_median_mode(col_name,percentage):
    implicit_missing_value_history = []
    number = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)
    mean_value = dataset_dataframe_version[col_name].mean(axis=0)
    median_value = dataset_dataframe_version[col_name].median(axis=0)
    mod_value = dataset_dataframe_version[col_name].mode()


    print("---------Change according to implicit missing value(Mean/Median/Mode) method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in implicit_missing_value_history:
            random_value = random.randint(1, len(dataset) - 1)
        implicit_missing_value_history.append(random_value)
        temp = dataset[random_value][col]

        col_list=[float(mean_value),float(median_value),float(mod_value)]
        selected=min(col_list, key=lambda x: abs(x - float(temp)))

        while temp==selected:
            col_list=col_list.remove(selected)
            selected = min(col_list, key=lambda x: abs(x - float(temp)))
        if len(col_list)==0:
            selected=mean_value+1
        dataset[random_value][col] = selected
        print("row: {} col: {} : '{}' changed to {}  ".format(random_value, col, temp,selected))
    return dataset









if __name__=="__main__":

    dataset = read_csv_dataset("/home/milad/Desktop/error-generator/dataset/hosp_holoclean.csv")
    # implicit_missing_value_mean_median_mode("salary",50)
    mean_value = dataset_dataframe_version["zip"].mean(axis=0)
    print(mean_value)