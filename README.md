## error-generator

this project trying to add several type of error to database.
in the following you can find the list of way that you can inject your data

- typos base on keyboards
    - Duplicate the character
    - Delete the character
    - Shift the character one keyboard space

- typos base on [butter-fingers](https://github.com/Decagon/butter-fingers)
    - A python library to generate highly realistic typos (fuzz-testing)
- explicit missing value
- Random Active domain
- Similar based Active domain(two record maybe equal and change based that)
- White noise (for numeric values) gaussian min=0 var=1  
- Denial_constraint
- error_duplicate


this project is a python program that should run it over your dataset for injecting your data 

