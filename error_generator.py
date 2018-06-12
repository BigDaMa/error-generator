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

def typoGenerator2(dataset,row,col):
    input_value = dataset[row][col]
    dataset[row][col] = butterfingers.butterfinger(input_value)
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

def similar_based_active_domain(dataset,row,col):
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
    #we can use this library insted our method
    # import ordered_set
    # from ordered_set import OrderedSet
    # c = [1, 3, 4, 2, 1]
    # c = OrderedSet(c)
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
    this method add fuctional dependency for now
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
    candidate_for_change=[]
    candidate_for_change_dic = {}
    history=[]
    temp=[]
    dic={}
    new_dic = {}
    new_dic_values = {}




    # devide the rule to sub and obj or left and right side

    for j in range(len(rules)):
        if len(rules[j])>2:#subject be 2 item

            sub.append([rules[j][0],rules[j][1]])
            obj.append(rules[j][2])
        else:
            sub.append(rules[j][0])
            obj.append(rules[j][1])


    #find the index of sub and obj

    for n in range(len(sub)):
        if type(sub[n])==list:#subject be 2 item
            indices_sub.append([dataset[0].index(sub[n][0]),dataset[0].index(sub[n][1])])
            indices_obj.append(dataset[0].index(obj[n]))
            pair.append((indices_sub[n], indices_obj[n]))  # indeces of the col



        else:
            indices_sub.append(dataset[0].index(sub[n]))
            indices_obj.append(dataset[0].index(obj[n]))
            pair.append((indices_sub[n], indices_obj[n])) #indeces of the col

    #if  we have only one percentage for all functional dependecy or we have list

    if type(percentage)!= list:
        print("percentage is a int")
        number = int((percentage / 100) * (len(dataset) - 1))

        # to understand how many rule we should violate from each rule

        choise_from_each_rule=int(number/len(indices_sub))

        for i in range(len(indices_sub)): #number of the function that we have
            number_choice = np.random.randint(1, len(dataset), choise_from_each_rule)
            dic[indices_sub[i]] = number_choice #for each rule we save the row number
            temp=[]
            for j in range(choise_from_each_rule):
                candidate_for_change.append(dataset[number_choice[j]][indices_sub[i]])
                temp.append(dataset[number_choice[j]][indices_sub[i]])
                candidate_for_change_dic[indices_sub[i]] = temp

    #for each function dependecy we have seprate percentage

    else:

        for i in range(len(indices_sub)):  # number of the function dependency that we have
            number_choice = np.random.randint(1, len(dataset), (int((percentage[i] / 100) * (len(dataset) - 1))))

            if type(indices_sub[i])==list:
                dic[indices_sub[i]] = number_choice


            else:
                dic[indices_sub[i]] = number_choice  # for each rule we save the row number

            temp=[]
            for j in range(int((percentage[i] / 100) * (len(dataset) - 1))):

                candidate_for_change.append(dataset[number_choice[j]][indices_sub[i]])
                temp.append(dataset[number_choice[j]][indices_sub[i]])
                candidate_for_change_dic[indices_sub[i]]=temp

    #check for duplicate in each list(values)

    for key, values in dic.items():
        new_dic[key] = remove_duplicates(values)

    #check if duplicate remove chose new values

    if dic.values() != new_dic.values():
        for k in dic:
            while (len(dic[k]) > len(new_dic[k])):
                new_num = np.random.randint(1, len(dataset), 1)
                if new_num not in new_dic[k]:
                    new_dic[k].append(new_num[0])




    for key, values in candidate_for_change_dic.items():
        new_dic_values[key] = remove_duplicates(values)

    #history is a list of all value that we want to change them
    for key, value in new_dic.items():
        for j in range(len(value)):
            history.append(( value[j],key))

    #change the candidate value in data base

    for key, value in new_dic.items():
        print("-----change for rule on col "+str(key)+" ------- ")
        for j in range(len(value)):

            temp_rand = random.randint(1, len(dataset) - 1)
            while temp_rand in value:
                temp_rand = random.randint(1, len(dataset) - 1)
            print(dataset[value[j]][key] + " change to " + dataset[temp_rand][key])
            dataset[value[j]][key] = dataset[temp_rand][key]

    return dataset

def similiarity(L_1, L_2):
    """
    this method compute the similarity between 2 list that used in error duplicate
    """
    L_1 = set(sys.intern(w) for w in L_1)
    L_2 = set(sys.intern(w) for w in L_2)
    to_match = L_1.difference( L_2)
    against = L_2.difference(L_1)
    for w in to_match:
        res = difflib.get_close_matches(w, against)
        if len(res):
            against.remove( res[0] )
    return (len(L_2)-len(against)) / (len(L_1))



def error_duplicate(dataset,percentage):
    """
    this method find similar row and add error to that rows
    :param dataset:
    :return:
    """
    duplicate = []
    for i, line1 in enumerate(dataset):
        for j, line2 in enumerate(dataset):
            if (similiarity(line1, line2) > 0.9):
                if i != j:
                    if [j, i] not in duplicate:
                        duplicate.append([i, j])
    #the rows that are duplicate are in duplicate
    print(duplicate)

    #pic column 0 and for row duplicate we change some thing
    # I pic the column 0 for now
    temp=[]
    for i in range(len(dataset)):
        temp.append(dataset[i][0])

    #the number that we should voilate
    number = int((percentage / 100) * (len(dataset) - 1))

    if number>len(duplicate):
        print("The maximum error would be genrate but it is less  than your request. decrease your percentage")

    for q in range(number):
        similar = difflib.get_close_matches(dataset[duplicate[q][0]][0], temp)
        while dataset[duplicate[q][0]][0] in similar: similar.remove(dataset[duplicate[q][0]][0])
    print("---------change according to duplicate---------------")
    print(dataset[duplicate[q][0]][0]+" change to "+similar[0])
    dataset[duplicate[q][0]][0]=similar[0]
    print(similar)



    # print(dataset[duplicate[0][0]][0])
    return dataset





if __name__=="__main__":
    x=read_csv_dataset("/home/milad/Desktop/error-generator/test.csv")
    print(x)

    #print(typoGenerator(x, 1, 2))
    #print(explicit_missing_value(x,1,2))
    #print(random_active_domain(x,1,2))
    #print(simlar_based_active_domain(x,1,2))
    #print(noise(x,1,2))
    #s=random_uniform(x,2,60)
    #print(typoGenerator2(x,1,0))

    # s=Denial_constraint(x,[["name","dept"],["manager","salary"]],[30,50])
    # print(s)
    print(error_duplicate(x,30))