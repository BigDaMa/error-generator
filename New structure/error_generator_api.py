from methodss.typos.typo_keyboard.typo_keyboard import Typo_Keyboard
from methodss.primary_function.input_output import Read_Write

def error_generator(method,selector,percentage,dataset):
    """
    selector is a list that user should specify the type of that for example [full_selector] or [col,1,3]

    now it only work with full selector

    """
    if method == "typo_keyboard":
        Typo_Keyboard.typo_keyboard(dataset,percentage)


#-------------------------------------------------------------------------it can be seprate file or class

dataset,dataframe = Read_Write.read_csv_dataset("./datasets/test.csv")

error_generator(method="typo_keyboard",selector="Not important now",percentage=20,dataset=dataset)