from methodss.primary_function.value_selector import Value_Selector
import random
import difflib

class Similar_Based_Active_Domain(object):
    def __init__(self):
        pass
    def similar_based_active_domain(dataset,percentage):

        # create instance from value selector
        instance_value_selector = Value_Selector()

        # how many cell we should change
        number_change = instance_value_selector.number(dataset, percentage)

        # list of the value that picked [[row,col,value]]
        list_selected_value = instance_value_selector.select_value(dataset, number_change)

        print("---------Change according to similar based active domin method ---------------\n")

        for i in range(number_change):
            col = list_selected_value[i][1]
            row = list_selected_value[i][0]
            selected_value = list_selected_value[i][2]

            temp = []
            for j in range(len(dataset)):
                temp.append(dataset[j][col])


            similar = difflib.get_close_matches(selected_value, temp, n=1000, cutoff=0)
            while selected_value in similar: similar.remove(selected_value)
            if len(similar) == 0:
                # here we need to pic the value that is not similar to selected value because
                # the value that picked was uniqe
                similar = difflib.get_close_matches(selected_value, temp, n=len(dataset), cutoff=0)
                while selected_value in similar: similar.remove(selected_value)

                dataset[row][col]=similar[0]
                print("row: {} col: {} : '{}' changed to '{}'  ".format(row, col, selected_value, similar[0]))

            else:
                dataset[row][col] = similar[0]
                print("row: {} col: {} : '{}' changed to '{}'  ".format(row, col, selected_value, similar[0]))

        return dataset
