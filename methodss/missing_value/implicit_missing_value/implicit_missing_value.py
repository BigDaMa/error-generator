from methodss.primary_function.value_selector import Value_Selector
import random
from collections import Counter
import statistics
import numpy as np


class Implicit_Missing_Value(object):
    def __init__(self,name="Implicit_Missing_Value"):
        self.name=name


    def run(self,row,col,selected_value,dataset):

        mod_value = []
        median_value = []

        for i in range(len(dataset[0])):
            for j in range(len(dataset) - 1):
                col_tmp = []
                col_tmp.append(dataset[j][i])

            data = Counter(col_tmp)
            uniqe = data.most_common()  # Returns all unique items and their counts
            mod = data.most_common(1)  # Returns the highest occurring item
            mod_value.append(mod[0][0])

            if (isinstance(dataset[1][i], str)):
                median_value.append(dataset[int(len(dataset) / 2)][i])
            else:
                median_value.append(statistics.median(col_tmp))


        col_list = [median_value[col], mod_value[col]]

        rand = np.random.randint(0, 2)
        selected = col_list[rand]

        while str(selected_value) == str(selected):
            col_list = col_list.remove(selected)
            if col_list is None:
                selected = median_value + median_value

        if (isinstance(selected, list)):
            if len(selected) > 1:
                selected = selected[0]

        return selected










    #
    #
    # def implicit_missing_value(dataset, percentage):
    #
    #     # create instance from value selector
    #     instance_value_selector = Value_Selector()
    #
    #     # how many cell we should change
    #     number_change = instance_value_selector.number(dataset, percentage)
    #
    #     # list of the value that picked [[row,col,value]]
    #     list_selected_value = instance_value_selector.select_value(dataset, number_change)
    #
    #     #find the median and mode of all column
    #
    #     mod_value = []
    #     median_value = []
    #
    #     for i in range(len(dataset[0])):
    #         for j in range(len(dataset)-1):
    #             col_tmp=[]
    #             col_tmp.append(dataset[j][i])
    #
    #         data = Counter(col_tmp)
    #         uniqe = data.most_common()  # Returns all unique items and their counts
    #         mod = data.most_common(1)  # Returns the highest occurring item
    #         mod_value.append(mod[0][0])
    #
    #         if (isinstance(dataset[1][i],str) ):
    #             median_value.append(dataset[int(len(dataset)/2)][i])
    #         else:
    #             median_value.append(statistics.median(col_tmp))
    #
    #
    #     print("---------Change according to implicit missing value(Median/Mode) method ---------------\n")
    #     for i in range(number_change):
    #
    #         col = list_selected_value[i][1]
    #         row = list_selected_value[i][0]
    #         selected_value = list_selected_value[i][2]
    #
    #         col_list = [median_value[col], mod_value[col]]
    #
    #
    #         rand = np.random.randint(0, 2)
    #         selected = col_list[rand]
    #
    #         while str(selected_value) == str(selected):
    #             col_list = col_list.remove(selected)
    #             if col_list is None:
    #                 selected = median_value + median_value
    #
    #         if (isinstance(selected, list)):
    #             if len(selected) > 1:
    #                 selected = selected[0]
    #         dataset[row][col] = selected
    #         print("row: {} col: {} : '{}' changed to {}  ".format(row, col,selected_value, selected))
    #     return dataset