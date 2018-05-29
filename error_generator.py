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

import difflib



#-----------------Method----------------------------


def read_csv_dataset(dataset_path, header_exists=True):
    """
    The method reads a dataset from a csv file path.
    """
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



def typoGenerator(dataset,row,col):
    """"
    The method add the typos
    row and column start from 0 (zero is the hedder)
    """
    input_value=dataset[row][col]
    temp="".join(w([z]*1+[w(["",z*2]+[chr(o(w("DGRC FHTV GJYB UOK HKUN JLIM KO NK BMJ IPL O WA ETF ADWZ RYG YIJ CBG QES ZCD TUH XS SQ VNH XVF SFEX WRD".split()[(o(z)&31)-6]))|o(z)&32)]*z.isalpha())])for z in input_value)
    dataset[row][col]=temp
    return dataset

def explicit_missing_value(dataset,row,col):
    """
    this method explicitly remove one value
    """
    dataset[row][col]=""
    return dataset


def random_active_domain(dataset,row,col):
    """"
    this method randomly change the value with active domain
    """
    random_value = random.randint(1,len(dataset)-1)
    dataset[row][col]=dataset[random_value][col]
    return dataset

def simlar_based_active_domain(dataset,row,col):
    """
    this method change the value to most similar one in active domain
    """
    temp=[]
    for i in range(len(dataset)):
        temp.append(dataset[i][col])

    similar=difflib.get_close_matches(dataset[row][col], temp)
    while dataset[row][col] in similar: similar.remove(dataset[row][col])
    dataset[row][col]=similar[0]
    return dataset


def noise(dataset,row,col):
    """
    this method add the noise to one active domain
    """
    # for now we add
    mu, sigma = 0, 0.1 # mean and standard deviation
    noise = np.random.normal(mu, sigma, 1)
    dataset[row][col]=float(dataset[row][col])+noise[0]
    return dataset
#----------How to chouse value----------------------

def random_uniform(dataset,col,percentage):
    """
    :param dataset:
    :param col:
    :param percentage:
    :return: the (row,col) shoul be change
    """
    number= int((percentage/100)*(len(dataset)-1))
    print(number)
    selected = np.random.uniform(1,len(dataset)-1, number)
    #print(selected)
    ret=[]
    for i in range (len(selected)):
        ret.append((selected[i].astype(np.int64),col))
    return ret


def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

def Denial_constraint(dataset,rules,percentage):
    """
    :param dataset:
    :param ruls:
    :param percentage:
    :return: the (row,col) should chaneg
    """

    indices_sub=[]
    indices_obj = []
    pair = []
    sub=[]
    obj=[]
    number = int((percentage / 100) * (len(dataset) - 1))


    # devide the rule to sub and obj

    for j in range(len(rules)):
        sub.append(rules[j][0])
        obj.append(rules[j][1])

    #find the index of sub and obj

    for n in range(len(sub)):
        indices_sub.append(x[0].index(sub[n]))
        indices_obj.append(x[0].index(obj[n]))
        pair.append((indices_sub[n], indices_obj[n])) #indeces of the col

    # to understand how many rule we should violate from each rule
    choise_from_each_rule=int(number/len(indices_sub))

    #print(choise_from_each_rule)
    print(pair)
    candidate_for_change=[]
    history=[]
    dic={}


    for i in range(len(indices_sub)):
        number_choice = np.random.randint(1, len(x), choise_from_each_rule)
        dic[indices_sub[i]] = number_choice #for each rule we save the row number
        #print(number_choice)
        for j in range(choise_from_each_rule):


            candidate_for_change.append(x[number_choice[j]][indices_sub[i]])

    print(dic)
    #check for duplicate

    new_dic={}
    for key, values in dic.items():
        new_dic[key] = remove_duplicates(values)
    #print(candidate_for_change)

    #print(ready_for_change)
    for key, value in new_dic.items():
        for j in range(len(value)):
            history.append(( value[j],key))

    print(history)
    print(new_dic)
    return history #the list of cell should be changed








if __name__=="__main__":
    x=read_csv_dataset("/home/milad/Desktop/error-generator/test.csv")
    #print(x)

    #print(typoGenerator(x, 1, 2))
    #print(explicit_missing_value(x,1,2))
    #print(random_active_domain(x,1,2))
    #print(simlar_based_active_domain(x,1,2))
    #print(noise(x,1,2))
    #s=random_uniform(x,2,60)
    Denial_constraint(x,[["name","dept"],["manager","salary"]],70)
