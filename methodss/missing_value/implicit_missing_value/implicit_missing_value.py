from methodss.primary_function.value_selector import Value_Selector
import random
from collections import Counter
import statistics
import numpy as np
from methodss.primary_function.inst_checker import Similar_First

class Implicit_Missing_Value(object):
    def __init__(self,name="Implicit_Missing_Value"):
        self.name=name


    def run(self,row,col,selected_value,dataset):


        similar_first=Similar_First()
        similar_first.similar_first(dataset)

        mod_value=similar_first.mod_value
        median_value=similar_first.median_value

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
