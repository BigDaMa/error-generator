# Error Generator
A python library to generate highly realistic errors
# Roadmap
this project trying to add several types of error to the dataset.
in the following, you can find the list of the ways that you can inject your dataset

- typos base on keyboards
    - Duplicate the character
    - Delete the character
    - Shift the character one keyboard space

- typos base on [butter-fingers](https://github.com/Decagon/butter-fingers)
    - A python library to generate highly realistic typos (fuzz-testing)
- explicit missing value
   - randomly one value will remove
- implicit missing value:
   - one of median or mode of the active domain, randomly pick and replace with the selected value
- Random Active domain
   - randomly one value from active domain replace with the selected value
- Similar based Active domain
    - the most similar value from the active domain will pick and replace with the selected value 
- White noise (for numeric values) min=0 var=1 
    - white noise added to the selected value
- gaussian noise:
    - the Gaussian noise added to the selected value (for string value the noise add to asci code of them)
    
# Installation
this project is a python program that should run it over your dataset for injecting your data.
All of the methods have their own function that you should call them and give the function (column_name, percentage) you wish for injection.

# Example
the list of functions and examples can find under API_error_generator.py


# output 
the dirty dataset will create in out folder
