from methodss.typos.typo_keyboard.typo_keyboard_cell import Typo_Keyboard_Cell


class Apply_Function(object):
    def __init__(self):
        pass
    def apply_function(number_change,list_selected_value,method,dataset):

        for i in range(number_change):
            if method == "typo_keyboard":
                result = Typo_Keyboard_Cell.typo_keyboard_cell(list_selected_value[i][2])
                dataset[list_selected_value[i][0]][list_selected_value[i][1]] = result
                print("row: {} col: {} : '{}' changed to '{}'  ".format(list_selected_value[i][0],list_selected_value[i][1],list_selected_value[i][2], result))





        return dataset