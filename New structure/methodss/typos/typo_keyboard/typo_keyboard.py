from methodss.primary_function.list_selected import List_selected
from methodss.primary_function.apply_function import Apply_Function

class Typo_Keyboard:
    def __init__(self):
        pass

    def typo_keyboard(dataset,percentage):


        list_selected_value,number_change=List_selected.list_selected(dataset,percentage)

        print("---------Change according to typoGenrator method ---------------\n")
        dataset=Apply_Function.apply_function(number_change=number_change,list_selected_value=list_selected_value,method="typo_keyboard",dataset=dataset)
        return dataset
