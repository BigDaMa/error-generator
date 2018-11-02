from accuracy_drop_proj.utilities.load_dataset.iris_loader import Iris_Loader
from accuracy_drop_proj.utilities.load_dataset.abalone_loader import Abalone_loader
from accuracy_drop_proj.utilities.load_dataset.digits_loader import Digits_Loader
from accuracy_drop_proj.strategies.change_feature_one_by_one.change_feature_one_by_one import Change_Feature_One_By_One
from accuracy_drop_proj.strategies.change_feature_randomly.change_feature_randomly import Change_Feature_randomly
from accuracy_drop_proj.strategies.change_most_important_feature.change_most_important_feature import Change_Most_Important_Feature
from accuracy_drop_proj.strategies.change_combination.change_combination import Change_Combination
from accuracy_drop_proj.strategies.change_combination_min.change_combination_min import Change_Combination_Min
from accuracy_drop_proj.strategies.change_combination_feature_min.change_combination_feature_min import Change_Combination_Feature_Min
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import time

#---------------------- load data set -----------------------
# loader=Iris_Loader()
# loader=Abalone_loader()
loader=Digits_Loader()

x_train, x_test, y_train, y_test = loader.load()


#---------------------train model -----------------------------

#----------------------MNB-------------------------------------
print("train MNB")
mnb = MultinomialNB()
mnb.fit(x_train,y_train)
print('Accuracy of MNB classifier on test set: {:.2f}'.format(mnb.score(x_test, y_test)))
#----------------------SVM--------------------------------------
# print("train SVM")
# svm = SVC()
# svm.fit(x_train, y_train)
# print('Accuracy of SVM classifier on test set: {:.2f}'.format(svm.score(x_test, y_test)))

#--------------------choose your method--------------------------------------------

# mymethod = Change_Feature_One_By_One()
# mymethod= Change_Feature_randomly()
# mymethod=Change_Most_Important_Feature()
# mymethod= Change_Combination()
mymethod =Change_Combination_Min()
# mymethod=Change_Combination_Feature_Min()

start = time.time()

change_plan={"key":[[9,7],[8,7],[10,7]],"number":[71,69,69]}
out=mymethod.change(x_test,y_test,20,mnb,change_plan)

end = time.time()

#--------------------------- evaluation ---------------------------------------------

y_pred=mnb.predict(out)

print("your execuation time is {} (s)".format(end - start))
print ("\n Accuracy  is {} \n".format(accuracy_score(y_test, y_pred)))
