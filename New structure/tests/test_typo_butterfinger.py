from methodss.primary_function.input_output import Read_Write
from methodss.typos.typo_butterfingers.typo_butterfingers import Typo_Butterfingers

class Test_Typo_Butterfingers(object):
    def __init__(self, name="test_typobutterfingers"):
        self.name = name

# ------------------------------- this is your part ----------------------------------



#create instance of test
inst_test=Test_Typo_Butterfingers()

#load data set
dataset,dataframe = Read_Write.read_csv_dataset("../datasets/test.csv")

#apply method
instance_typo=Typo_Butterfingers
new_dataset=instance_typo.typo_butterfingers(dataset=dataset,percentage=20)

#write to output
Read_Write.write_csv_dataset("../outputs/{}.csv".format(inst_test.name), new_dataset)

