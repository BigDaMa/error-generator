from methodss.primary_function.input_output import Read_Write
from methodss.switch_value.random_active_domain.random_active_domain import Random_Active_Domain

class Test_Random_Active_domain(object):
    def __init__(self,name="test_random_active_domain"):
        self.name=name


# ------------------------------- this is your part ----------------------------------



#create instance of test
inst_test=Test_Random_Active_domain()

#load data set
dataset,dataframe = Read_Write.read_csv_dataset("../datasets/test.csv")

#apply method
instance_active_domain=Random_Active_Domain
new_dataset=instance_active_domain.random_active_domain(dataset=dataset,percentage=20)

#write to output
Read_Write.write_csv_dataset("../outputs/{}.csv".format(inst_test.name), new_dataset)
