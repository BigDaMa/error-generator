from methodss.primary_function.value_selector import value_selector
from methodss.primary_function import input_output
from random import *
w=choice
o=ord
class typo_keyboard:
    def __init__(self):
        pass
    

    
    def typo_keyboard(self,dataset,percentage):
        
        # create instance from value selector
        instance_value_selector = value_selector()
        
        #how many cell we should change     
        number_change=instance_value_selector.number(dataset,percentage)

        #list of the value that picked [[row,col,value]]        
        list_selected_value=instance_value_selector.select_value(dataset,number_change)
        
        
        print("---------Change according to typoGenrator method ---------------\n")
        for i in range(number_change):
            input_value=list_selected_value[i][2]
            temp = "".join(w([z] * 0 + [w(["", z * 2] + [chr(o(w(
                "DGRC FHTV GJYB UOK HKUN JLIM KO NK BMJ IPL O WA ETF ADWZ RYG YIJ CBG QES ZCD TUH XS SQ VNH XVF SFEX WRD".split()[
                    (o(z) & 31) - 6])) | o(z) & 32)] * z.isalpha())]) for z in input_value)
            dataset[list_selected_value[i][0]][list_selected_value[i][1]] = temp
            print("row: {} col: {} : '{}' changed to '{}'  ".format(list_selected_value[i][0],list_selected_value[i][1], input_value, temp))
        return dataset