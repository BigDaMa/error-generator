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
import math
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

def typoGenerator(percentage):
    """"
    The method add the typos
    row and colu  mn start from 0 (zero is the hedder)
    """
    typoGenerator_history = []
    number = int((percentage / 100.0) * (len(dataset) - 1))


    # col=dataset[0].index(col_name)
    print()

    print("---------Change according to typoGenrator method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in typoGenerator_history:
            random_value = random.randint(1, len(dataset) - 1)
        typoGenerator_history.append(random_value)
        col = random.randint(0, len(dataset[0]) - 1)

        input_value=dataset[random_value][col]

        while (len(input_value) == 0):
            random_value = random.randint(1, len(dataset) - 1)
            while random_value in typoGenerator_history:
                random_value = random.randint(1, len(dataset) - 1)
            typoGenerator_history.append(random_value)
            input_value = dataset[random_value][col]

        temp="".join(w([z]*0+[w(["",z*2]+[chr(o(w("DGRC FHTV GJYB UOK HKUN JLIM KO NK BMJ IPL O WA ETF ADWZ RYG YIJ CBG QES ZCD TUH XS SQ VNH XVF SFEX WRD".split()[(o(z)&31)-6]))|o(z)&32)]*z.isalpha())])for z in input_value)
        dataset[random_value][col]=temp
        print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value,col,input_value,temp))
    return dataset


def typoGenerator2(percentage):

    typoGenerator2_history = []
    number_row = int((percentage / 100.0) * (len(dataset) - 1))
    # col = random.randint(0, len(dataset[0]) - 1)
    # col = dataset[0].index(col_name)
    print("---------Change according to typoGenrator method(Butterfinger) ---------------\n")

    for i in range(number_row):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in typoGenerator2_history:
            random_value = random.randint(1, len(dataset) - 1)
        typoGenerator2_history.append(random_value)

        col = random.randint(0, len(dataset[0]) - 1)
        input_value = dataset[random_value][col]
        while (len(input_value) == 0):
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

def explicit_missing_value(percentage):
    """
    this method explicitly remove one value
    """
    explicit_missing_value_history = []
    number = int((percentage / 100.0) * (len(dataset) - 1))
    # col = random.randint(0, len(dataset[0]) - 1)
    # col = dataset[0].index(col_name)
    print("---------Change according to explicit missing value method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in explicit_missing_value_history:
            random_value = random.randint(1, len(dataset) - 1)
        explicit_missing_value_history.append(random_value)

        col = random.randint(0, len(dataset[0]) - 1)
        temp=dataset[random_value][col]
        while (len(temp) == 0):
            random_value = random.randint(1, len(dataset) - 1)
            while random_value in explicit_missing_value_history:
                random_value = random.randint(1, len(dataset) - 1)
            explicit_missing_value_history.append(random_value)
            temp = dataset[random_value][col]

        dataset[random_value][col]=""
        print("row: {} col: {} : '{}' changed to ' '  ".format(random_value, col,temp ))
    return dataset



def implicit_missing_value_mean_median_mode(percentage):
    implicit_missing_value_history = []
    number = int((percentage / 100.0) * (len(dataset) - 1))


    mod_value=[]
    median_value=[]
    for i in range(len(dataset[0])):

        col_name = dataset[0][i]
        mod_value.append( dataset_dataframe_version[col_name].mode()[0])
        sort_frame = dataset_dataframe_version.sort_values(col_name)
        size=dataset_dataframe_version.shape[0]
        index=int(size/2)+1
        median_value.append(sort_frame[col_name][index])

    print("---------Change according to implicit missing value(Median/Mode) method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in implicit_missing_value_history:
            random_value = random.randint(1, len(dataset) - 1)
        implicit_missing_value_history.append(random_value)
        col = random.randint(0, len(dataset[0]) - 1)

        temp = dataset[random_value][col]
        col_list=[median_value[col],mod_value[col]]

        rand=np.random.randint(0,2)
        selected=col_list[rand]

        while str(temp)==str(selected):
            col_list=col_list.remove(selected)
            if col_list is None:
                selected = median_value + median_value

        dataset[random_value][col] = selected
        print("row: {} col: {} : '{}' changed to {}  ".format(random_value, col, temp,selected))
    return dataset





#--------------------ACTIVE DOMAIN -----------------------------------


def random_active_domain(percentage):
    """"
    this method randomly change the value with active domain
    """
    random_active_domain_history = []
    number_row_random = int((percentage / 100.0) * (len(dataset) - 1))
    # col = random.randint(0, len(dataset[0]) - 1)
    # col = dataset[0].index(col_name)

    print("---------Change according to Random Active domin method ---------------\n")
    for i in range(number_row_random):
        random_values_row = random.randint(1, len(dataset) - 1)
        while random_values_row in random_active_domain_history:
            random_values_row = random.randint(1, len(dataset) - 1)
        random_active_domain_history.append(random_values_row)

        col = random.randint(0, len(dataset[0]) - 1)
        random_value = random.randint(1,len(dataset)-1)
        while (random_value ==random_values_row or dataset[random_values_row][col]== dataset[random_value][col]):
            random_value = random.randint(1, len(dataset) - 1)


        input_value_random_method=dataset[random_values_row][col]
        temp_random_method = dataset[random_value][col]

        dataset[random_values_row][col] = temp_random_method

        print("row: {} col: {} : '{}' changed to '{}'  ".format(random_values_row, col, input_value_random_method,temp_random_method))
    return dataset


def similar_based_active_domain(percentage):
    """
    this method change the value to most similar one in active domain
    """
    similar_based_active_domain_history = []
    number_similar_active_domain = int((percentage / 100.0) * (len(dataset) - 1))

    print("---------Change according to similar based active domin method ---------------\n")

    for i in range(number_similar_active_domain):
        col = random.randint(0, len(dataset[0])-1)


        random_value = random.randint(1, len(dataset) - 1)
        while random_value in similar_based_active_domain_history:
            random_value = random.randint(1, len(dataset) - 1)
        similar_based_active_domain_history.append(random_value)
        selected_value = dataset[random_value][col]

        while (len(selected_value) == 0):
            random_value = random.randint(1, len(dataset) - 1)
            while random_value in similar_based_active_domain_history:
                random_value = random.randint(1, len(dataset) - 1)
            similar_based_active_domain_history.append(random_value)
            selected_value = dataset[random_value][col]

        temp = []
        for i in range(len(dataset)):
            temp.append(dataset[i][col])


        similar = difflib.get_close_matches(selected_value, temp, n=5000, cutoff=0)
        while selected_value in similar: similar.remove(selected_value)
        if len(similar) == 0:
            print("there is no similar value to '{}' in your requested column".format(selected_value))
            print("please increase the n in the similar function")


        else:
            dataset[random_value][col] = similar[0]
            print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value, col, selected_value, similar[0]))
    return dataset




#--------------------------NOISE----------------------------------


def noise(percentage):
    """
    this method add the noise to one active domain(numeric only)
    """
    # for now we add
    mu, sigma = 0, 1 # mean and standard deviation
    noise = np.random.normal(mu, sigma, 1)
    noise_history = []
    number = int((percentage / 100.0) * (len(dataset) - 1))
    # col = random.randint(0, len(dataset[0]) - 1)

    # col = dataset[0].index(col_name)
    print("---------Change according to noise method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in noise_history:
            random_value = random.randint(1, len(dataset) - 1)
        noise_history.append(random_value)
        col = random.randint(0, len(dataset[0]) - 1)
        selected=dataset[random_value][col]

        while (len(selected) == 0):
            random_value = random.randint(1, len(dataset) - 1)
            while random_value in noise_history:
                random_value = random.randint(1, len(dataset) - 1)
            noise_history.append(random_value)
            selected = dataset[random_value][col]


        asci_number=""
        noisy_value=""
        if (isinstance(selected, str)):

            for ch in selected:
                code = ord(ch)
                digits = int(math.log10(code)) + 1
                if digits<=2:
                    code=str(code)
                    code=code.zfill(3)
                else:
                    code = str(code)
                asci_number=asci_number+code

            string_noise=int(int(asci_number)*noise[0])
            string_noise=string_noise+int(asci_number)
            string_noise=str(string_noise)
            three_number=int(len(string_noise)/3)
            if len(string_noise)%3 !=0:
                three_number=three_number+1
            for i in range(three_number):

                three=string_noise[-3:]
                noisy_value=noisy_value+chr(abs(int(three)))
                string_noise=string_noise.replace(three,'',1)
            noisy_value=noisy_value[::-1]
            dataset[random_value][col]=noisy_value
            print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value, col, selected,noisy_value))

        else:
            add_value=float(noise[0])*float(selected)
            if(isinstance(selected, float)):
                dataset[random_value][col] = float(selected) + add_value
            else:
                if (int(float(selected) + add_value))==selected:
                    dataset[random_value][col] = int(float(selected) + add_value)+1
                dataset[random_value][col] = int(float(selected) + add_value)


            print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value,col,selected,dataset[random_value][col]))
    return dataset




def noise_gaussian(percentage,noise_rate):
    implicit_missing_value_history = []
    number = int((percentage / 100.0) * (len(dataset) - 1))
    # col = random.randint(0, len(dataset[0]) - 1)
    # col = dataset[0].index(col_name)


    print("---------Change according to gaussian noise method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in implicit_missing_value_history:
            random_value = random.randint(1, len(dataset) - 1)
        implicit_missing_value_history.append(random_value)
        col = random.randint(0, len(dataset[0]) - 1)
        temp = dataset[random_value][col]

        while (len(temp) == 0):
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

    #---------------Example one ------------------------

    dataset = read_csv_dataset("dataset/hospital_10k.txt")
    # Function(column_name,percentage)

    random_active_domain(1)
    '''
    similar_based_active_domain(1)

    typoGenerator(1)
    typoGenerator2(1)

    explicit_missing_value(1)
    implicit_missing_value_mean_median_mode(1)

    noise(1)
    noise_gaussian(1,10) #percentage,noise_rate  #you can specify noise rate in this function
    '''

    write_csv_dataset("output/out.csv", dataset)




