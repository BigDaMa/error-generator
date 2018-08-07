from methodss.primary_function.input_output import Read_Write
from methodss.switch_value.Similar_based_active_domain.similar_based_active_domain import Similar_Based_Active_Domain
from error_generator_api import Error_Generator
from methodss.primary_function.list_selected import List_selected


class Test_Similar_Based_Active_Domain(object):
    def __init__(self, name="similar_based_active_domain"):
        self.name = name





# ------------------------------- this is test part ----------------------------------


dataset,dataframe = Read_Write.read_csv_dataset("../datasets/test.csv")

mymethod=Similar_Based_Active_Domain()


myselector=List_selected()


mygen=Error_Generator()
new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=20,dataset=dataset)


# #create instance of test
inst_test=Test_Similar_Based_Active_Domain()


#write to output
Read_Write.write_csv_dataset("../outputs/{}.csv".format(inst_test.name), new_dataset)



