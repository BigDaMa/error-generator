this project trying to add several types of error to the database.
in the following, you can find the list of the way that you can inject your data

- typos base on keyboards
    - Duplicate the character
    - Delete the character
    - Shift the character one keyboard space

- typos base on [butter-fingers](https://github.com/Decagon/butter-fingers)
    - A python library to generate highly realistic typos (fuzz-testing)
- explicit missing value
   - randomly one value will remove
- Random Active domain
  -randomly one value will change will active domain
- Similar based Active domain
    - the most similar active domain will pick from active domain and replace with the selected value 
- White noise (for numeric values) gaussian min=0 var=1  
- Denial_constraint
   - function dependency: list of the columns that have functional dependency will be asked from user and base on that dataset will inject 
- error_duplicatethe
    - duplicate will find in the dataset and according to duplicate, errors will add to dataset.


this project is a python program that should run it over your dataset for injecting your data.
All of the methods have their own function that you should call them and give the function (dataset, column, percentage) you wish for injection.
