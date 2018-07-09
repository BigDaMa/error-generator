import os
import json
import re
import subprocess
import pandas
import numpy as np
import psycopg2
from random import *
w=choice
o=ord
import random
import butterfingers
import difflib
import sys
dataset_dataframe_version=None


#----------------- read csv file ----------------------------

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
#-----------------TYPOYS--------------------------------

def typoGenerator(col_name,percentage):
    """"
    The method add the typos
    row and colu  mn start from 0 (zero is the hedder)
    """
    typoGenerator_history = []
    number = int((percentage / 100) * (len(dataset) - 1))

    col=dataset[0].index(col_name)

    print("---------Change according to typoGenrator method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in typoGenerator_history:
            random_value = random.randint(1, len(dataset) - 1)
        typoGenerator_history.append(random_value)

        input_value=dataset[random_value][col]
        temp="".join(w([z]*0+[w(["",z*2]+[chr(o(w("DGRC FHTV GJYB UOK HKUN JLIM KO NK BMJ IPL O WA ETF ADWZ RYG YIJ CBG QES ZCD TUH XS SQ VNH XVF SFEX WRD".split()[(o(z)&31)-6]))|o(z)&32)]*z.isalpha())])for z in input_value)
        dataset[random_value][col]=temp
        print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value,col,input_value,temp))
    return dataset


def typoGenerator2(col_name,percentage):

    typoGenerator2_history = []
    number_row = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)
    print("---------Change according to typoGenrator method(Butterfinger) ---------------\n")

    for i in range(number_row):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in typoGenerator2_history:
            random_value = random.randint(1, len(dataset) - 1)
        typoGenerator2_history.append(random_value)


        input_value = dataset[random_value][col]
        temp=butterfingers.butterfinger(input_value)
        dataset[random_value][col] = temp
        print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value, col, input_value, temp))
    return dataset


#-------------------- MISSING VALUE----------------------------------

def explicit_missing_value(col_name,percentage):
    """
    this method explicitly remove one value
    """
    explicit_missing_value_history = []
    number = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)
    print("---------Change according to explicit missing value method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in explicit_missing_value_history:
            random_value = random.randint(1, len(dataset) - 1)
        explicit_missing_value_history.append(random_value)
        temp=dataset[random_value][col]
        dataset[random_value][col]=""
        print("row: {} col: {} : '{}' changed to ' '  ".format(random_value, col,temp ))
    return dataset


def implicit_missing_value_mean(col_name,percentage):
    implicit_missing_value_history = []
    number = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)
    mean_value = dataset_dataframe_version[col_name].mean(axis=0)

    print(mean_value)
    print("---------Change according to implicit missing value(Mean) method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in implicit_missing_value_history:
            random_value = random.randint(1, len(dataset) - 1)
        implicit_missing_value_history.append(random_value)
        temp = dataset[random_value][col]
        if temp==mean_value:
            mean_value=mean_value+1
        dataset[random_value][col] = mean_value
        print("row: {} col: {} : '{}' changed to {}  ".format(random_value, col, temp,mean_value))
    return dataset




#--------------------ACTIVE DOMAIN -----------------------------------


def random_active_domain(col_name,percentage):
    """"
    this method randomly change the value with active domain
    """
    random_active_domain_history = []
    number_row_random = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)

    print("---------Change according to Random Active domin method ---------------\n")
    for i in range(number_row_random):
        random_values_row = random.randint(1, len(dataset) - 1)
        while random_values_row in random_active_domain_history:
            random_values_row = random.randint(1, len(dataset) - 1)
        random_active_domain_history.append(random_values_row)


        random_value = random.randint(1,len(dataset)-1)
        while (random_value ==random_values_row or dataset[random_values_row][col]== dataset[random_value][col]):
            random_value = random.randint(1, len(dataset) - 1)


        input_value_random_method=dataset[random_values_row][col]
        temp_random_method = dataset[random_value][col]

        dataset[random_values_row][col] = temp_random_method

        print("row: {} col: {} : '{}' changed to '{}'  ".format(random_values_row, col, input_value_random_method,temp_random_method))
    return dataset


def similar_based_active_domain(col_name,percentage):
    """
    this method change the value to most similar one in active domain
    """
    similar_based_active_domain_history = []
    number_similar_active_domain = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)
    print("---------Change according to similar based active domin method ---------------\n")

    temp = []
    for i in range(len(dataset)):
        temp.append(dataset[i][col])

    for i in range(number_similar_active_domain):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in similar_based_active_domain_history:
            random_value = random.randint(1, len(dataset) - 1)
        similar_based_active_domain_history.append(random_value)

        selected_value=dataset[random_value][col]
        similar=difflib.get_close_matches(selected_value, temp,n=10,cutoff=0)
        while selected_value in similar: similar.remove(selected_value)
        if len(similar)==0:
            print("there is no similar value to '{}' in your requested column".format(selected_value))

        else:
            dataset[random_value][col]=similar[0]
            print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value,col,selected_value,similar[0]))
    return dataset


#--------------------------NOISE----------------------------------

def noise(col_name,percentage):
    """
    this method add the noise to one active domain
    """
    # for now we add
    mu, sigma = 0, 0.1 # mean and standard deviation
    noise = np.random.normal(mu, sigma, 1)

    noise_history = []
    number = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)
    print("---------Change according to noise method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in noise_history:
            random_value = random.randint(1, len(dataset) - 1)
        noise_history.append(random_value)
        selected=dataset[random_value][col]
        dataset[random_value][col]=float(selected)+noise[0]

        print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value,col,selected,dataset[random_value][col]))
    return dataset


if __name__=="__main__":
    dataset = read_csv_dataset("/home/milad/Desktop/error-generator/test.csv")

    typoGenerator("dept",50)
    typoGenerator2("dept",50)
    explicit_missing_value("dept",50)
    random_active_domain("dept",50)
    similar_based_active_domain("dept",50)
    noise("salary",50)
    implicit_missing_value_mean("salary",50)







