
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import random
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier



data = pd.read_csv("./EEG_data_Epileptic_Seizure_Recognition.csv")
data = data.drop(['Unnamed: 0'], axis=1)

y = data.y.values

del data["y"] # remove rings from data, so we can convert all the dataframe to a numpy 2D array.
X = data.values.astype(np.float)

#find the order of the feature according to information gain
model = ExtraTreesClassifier()
model.fit(data, y)


information_gain = {}
for i in range(len(model.feature_importances_)):
    information_gain.update({i: model.feature_importances_[i]})

col_sorted=sorted(information_gain.items(), key=lambda x:x[1],reverse=True)
select_col=[]
for i in col_sorted:
    select_col.append(i[0])

print('§§§§§§§§§§§§§§§§§§§§')
print(select_col)
print('§§§§§§§§§§§§§§§§§§§§')


from mlxtend.feature_selection import SequentialFeatureSelector as SFS

sfs1 = SFS(model,
           k_features=3,
           forward=True,
           floating=False,
           verbose=2,
           scoring='accuracy',
           cv=0)

sfs1 = sfs1.fit(data, y)


print('&&&&&&&&&&&&&&&&&&&&&&')
print(sfs1.k_feature_idx_)
print('&&&&&&&&&&&&&&&&&&&&&&')