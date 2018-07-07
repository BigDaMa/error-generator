from normalise import normalise

import API_error_generator
import difflib
import sys
import random
import numpy as np

dataset = API_error_generator.read_csv_dataset("/home/milad/Desktop/error-generator/test.csv")



def noise(col_name,percentage):
    """
    this method add the noise to one active domain
    """
    # for now we add
    mu, sigma = 0, 0.1 # mean and standard deviation
    noise = np.random.normal(mu, sigma, 1)

    noise_history = []
    number = int((percentage / 100) * (len(dataset) - 1))
    col = dataset[0].index(col_name)
    print("---------Change according to noise method ---------------\n")
    for i in range(number):
        random_value = random.randint(1, len(dataset) - 1)
        while random_value in noise_history:
            random_value = random.randint(1, len(dataset) - 1)
        noise_history.append(random_value)
        selected=dataset[random_value][col]

        dataset[random_value][col]=float(selected)+noise[0]

        print("row: {} col: {} : '{}' changed to '{}'  ".format(random_value,col,selected,dataset[random_value][col]))
    return dataset

#noise("salary",50)
import numpy as np
def genSine(f0, fs, dur):
    t = np.arange(dur)
    sinusoid = np.sin(2*np.pi*t*(f0/fs))
    sinusoid = normalise(sinusoid)
    return sinusoid


