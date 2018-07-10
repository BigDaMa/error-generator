########################################
# Error Generator
# Milad Abbaszadeh
# Milad.abbaszadeh94@gmail.com
# July 2018
# Big Data Management Group
# TU Berlin
# All Rights Reserved
########################################

########################################
import os
import json
import re
import subprocess
import pandas
import numpy as np
import psycopg2
from random import *
import random
import butterfingers
import difflib
import sys
dataset_dataframe_version=None
import chainer, chainer.links as L,chainer.functions as F
from chainer import Variable
w=choice
o=ord
#######################################################


#----------------- read & write csv file ----------------------------

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


def write_csv_dataset(dataset_path, dataset_table):
    """
    The method writes a dataset to a csv file path.
    """
    dataset_dataframe = pandas.DataFrame(data=dataset_table[1:], columns=dataset_table[0])
    dataset_dataframe.to_csv(dataset_path, sep=",", header=True, index=False, encoding="utf-8")


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

def implicit_missing_value_mean_median_mode(col_name,percentage):
    implicit_missing_value_history = []
    number = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)

    mod_value = dataset_dataframe_version[col_name].mode()
    sort_frame = dataset_dataframe_version.sort_values(col_name)
    size=dataset_dataframe_version.shape[0]
    index=int(size/2)+1
    median_value=sort_frame[col_name][index]

    mod_value=list(mod_value.values)[0]



    print("---------Change according to implicit missing value(Median/Mode) method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in implicit_missing_value_history:
            random_value = random.randint(1, len(dataset) - 1)
        implicit_missing_value_history.append(random_value)
        temp = dataset[random_value][col]

        col_list=[median_value,mod_value]
        rand=np.random.randint(0,2)
        selected=col_list[rand]
        while str(temp)==str(selected):
            col_list=col_list.remove(selected)

        if len(col_list)==0:
            selected=median_value+median_value
        dataset[random_value][col] = selected
        print("row: {} col: {} : '{}' changed to {}  ".format(random_value, col, temp,selected))
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
        similar=difflib.get_close_matches(selected_value, temp,n=1000,cutoff=0)
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
    this method add the noise to one active domain(numeric only)
    """
    # for now we add
    mu, sigma = 0, 1 # mean and standard deviation
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
        add_value=float(noise[0])*float(selected)
        if(isinstance(selected, float)):
            dataset[random_value][col] = float(selected) + add_value
        else:
            if (int(float(selected) + add_value))==selected:
                dataset[random_value][col] = int(float(selected) + add_value)+1
            dataset[random_value][col] = int(float(selected) + add_value)


        print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value,col,selected,dataset[random_value][col]))
    return dataset

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
        # print(type(temp))
        if (isinstance(temp, str)):

            asci_str=0
            for ch in temp:
                code = ord(ch)
                asci_str=code+asci_str
            added_str=chr(asci_str)

            temp_array = np.array([asci_str]).astype(np.float32)
            # batch,dim = v.data.shape[0],v.data.shape[1]
            batch = 1
            ones = Variable(np.ones((batch), dtype=np.float32))
            new_value = F.gaussian(temp_array, noise_rate * ones)

            if int(new_value.data[0])==asci_str:
                print("your noise rate is not alot so the strings will reverse as noise")
                new_value = temp[::-1]
                replaced_value=new_value
                dataset[random_value][col] = replaced_value
            else:

                rand = np.random.randint(0, len(temp))
                replaced_value = temp[:rand] + added_str+ temp[rand:]
                dataset[random_value][col] = replaced_value

        else:
            temp_array = np.array([temp]).astype(np.float32)
            # batch,dim = v.data.shape[0],v.data.shape[1]
            batch=1
            ones = Variable(np.ones((batch), dtype=np.float32))
            new_value=F.gaussian(temp_array, noise_rate * ones)
            dataset[random_value][col] = new_value.data[0]
            replaced_value=new_value.data[0]


        print("row: {} col: {} : '{}' changed to {}  ".format(random_value, col, temp,replaced_value))
    return dataset






if __name__=="__main__":

    # dataset = read_csv_dataset("/home/milad/Desktop/error-generator/dataset/test.csv")
    # typoGenerator("dept",50)
    # typoGenerator2("dept",50)
    # explicit_missing_value("dept",50)
    # random_active_domain("dept",50)
    # similar_based_active_domain("dept",50)
    # noise("salary",50)
    # implicit_missing_value_mean_median_mode("salary",50)
    # noise_gaussian("salary", 50, -10)
    # write_csv_dataset("output/out.csv", dataset)

    dataset = read_csv_dataset("dataset/address_10_ground_truth.csv")
    typoGenerator("FirstName",1)
    typoGenerator2("City",1)
    explicit_missing_value("Address",1)
    implicit_missing_value_mean_median_mode("ZIP", 1)
    random_active_domain("ZIP",1)
    similar_based_active_domain("City",1)
    noise("ZIP",1)
    noise_gaussian("ZIP",1,10)

    write_csv_dataset("output/out.csv",dataset)




