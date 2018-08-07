from methodss.primary_function.value_selector import Value_Selector
import random
import difflib

class Similar_Based_Active_Domain(object):
    def __init__(self,name="similar_based_active_domain"):
        self.name=name

    
        
    def run(self,row,col,selected_value,dataset):
        
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

            
        return similar[0]
        
