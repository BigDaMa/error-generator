
from methodss.primary_function import input_output


 

class test(object):
    def __init__(self,name="test"):
        self.name=name
    
    
dataset = input_output.read_write.read_csv_dataset("/home/milad/Desktop/error-generator/dataset/address_10_ground_truth.csv")
input_output.read_write.write_csv_dataset("/home/milad/Desktop/error-generator/New structure/outputs/address_{}.csv".format(test().name),dataset)
print(dataset)
    
    