from methodss.primary_function.input_output import Read_Write
from methodss.missing_value.implicit_missing_value.implicit_missing_value import Implicit_Missing_Value

class Test_Implicit_Missing_Value(object):
    def __init__(self,name="implicit_missing_value"):
        self.name=name



# ------------------------------- this is your part ----------------------------------



#create instance of test
inst_test=Test_Implicit_Missing_Value()

#load data set
dataset,dataframe = Read_Write.read_csv_dataset("../datasets/test.csv")

#apply method
instance_active_domain=Implicit_Missing_Value
new_dataset=instance_active_domain.implicit_missing_value(dataset=dataset,percentage=20)

#write to output
Read_Write.write_csv_dataset("../outputs/{}.csv".format(inst_test.name), new_dataset)

