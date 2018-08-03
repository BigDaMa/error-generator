from methodss.primary_function.input_output import Read_Write
from methodss.switch_value.Similar_based_active_domain.similar_based_active_domain import Similar_Based_Active_Domain

class Test_Similar_Based_Active_Domain(object):
    def __init__(self,name="similar_based_active_domain"):
        self.name=name


# ------------------------------- this is your part ----------------------------------



#create instance of test
inst_test=Test_Similar_Based_Active_Domain()

#load data set
dataset,dataframe = Read_Write.read_csv_dataset("../datasets/test.csv")

#apply method
instance_active_domain=Similar_Based_Active_Domain
new_dataset=instance_active_domain.similar_based_active_domain(dataset=dataset,percentage=20)

#write to output
Read_Write.write_csv_dataset("../outputs/{}.csv".format(inst_test.name), new_dataset)



