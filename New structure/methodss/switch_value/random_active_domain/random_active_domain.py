from methodss.primary_function.value_selector import Value_Selector
import random
class Random_Active_Domain(object):
    def __init__(self):
        pass

    def random_active_domain(dataset, percentage):

        # create instance from value selector
        instance_value_selector = Value_Selector()

        # how many cell we should change
        number_change = instance_value_selector.number(dataset, percentage)

        # list of the value that picked [[row,col,value]]
        list_selected_value = instance_value_selector.select_value(dataset, number_change)

        print("---------Change according to Random Active domin method ---------------\n")

        for i in range(number_change):

            col = random.randint(0, len(dataset[0]) - 1)
            row = random.randint(1, len(dataset) - 1)

            while (row == list_selected_value[i][0] and col == list_selected_value[i][1]):
                row = random.randint(1, len(dataset) - 1)

            input_value_random_method = list_selected_value[i][2]
            temp_random_method = dataset[row][col]

            dataset[list_selected_value[i][0]][list_selected_value[i][1]]= temp_random_method

            print("row: {} col: {} : '{}' changed to '{}'  ".format(row, col, input_value_random_method,temp_random_method))

        return dataset
