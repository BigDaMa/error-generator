from methodss.primary_function.input_output import Read_Write
from methodss.typos.typo_keyboard.typo_keyboard import Typo_Keyboard

class Test_Typo_Keyboard(object):
    def __init__(self, name="test_typo_keyboard"):
        self.name = name





# ------------------------------- this is your part ----------------------------------



#create instance of test
inst_test=Test_Typo_Keyboard()

#load data set
dataset,dataframe = Read_Write.read_csv_dataset("../datasets/test.csv")

#apply method
instance_typo=Typo_Keyboard()
new_dataset=instance_typo.typo_keyboard(dataset,20)




#write to output
Read_Write.write_csv_dataset("../outputs/{}.csv".format(inst_test.name), new_dataset)

