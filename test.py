import numpy as np
import random
import pandas
import error_generator

dataset=error_generator.read_csv_dataset("/home/milad/Desktop/error-generator/test.csv")
# print(dataset)

dic={0:[6, 6, 2, 2], 3:[5, 3, 4]}
new_dic={0: [6, 2], 3: [5, 3 ,4]}


if dic.values()!=new_dic.values():
    for k in dic:
        if dic[k]!=new_dic[k]:
            while(len(dic[k])>len(new_dic[k])):
                new_num=np.random.randint(1, len(dataset),1)
                if new_num not in new_dic[k]:
                    new_dic[k].append(new_num[0])
            print(new_dic[k])