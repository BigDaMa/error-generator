# from elasticsearch import helpers, Elasticsearch
# import csv
#
# es = Elasticsearch([{'host': 'localhost', 'port': 9201}])
#
# with open('./datasets/abalone.data') as f:
#     reader = csv.DictReader(f)
#     helpers.bulk(es, reader, index='my-index', doc_type='my-type')
#--------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn import datasets

# iris = datasets.load_iris()
# X = iris.data  # we only take the first two features for visualization
# y = iris.target
# print(X[48:52])
# print(y[48:52])
# model= SVC(probability=True)
# model.fit(X,y)
#
# y_pred = model.predict(X)
#
# print(accuracy_score(y,y_pred))
# probability = model.predict_proba(X[48:52])
#
# print(probability)


#
# import numpy as np
# from sklearn.naive_bayes import MultinomialNB
# from accuracy_drop_proj.utilities.load_dataset.digits_loader import Digits_Loader
# loader = Digits_Loader()
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import accuracy_score
#
# x_train, x_test, y_train, y_test = loader.load()
#
# print("train MNB")
# model = MultinomialNB()
#
# model.fit(x_train,y_train)
# y_pred = model.predict(x_test)
#
# print(accuracy_score(y_test,y_pred))
# print(confusion_matrix(y_test, y_pred))

###################################################3
from accuracy_drop_proj.utilities.save_dataset.save_pickle_obj import Save_Pickle_Obj
from accuracy_drop_proj.utilities.load_dataset.load_pickle_obj import Load_Pickle_Obj
from accuracy_drop_proj.utilities.load_dataset.iris_loader import Iris_Loader
from accuracy_drop_proj.utilities.load_dataset.abalone_loader import Abalone_loader
from accuracy_drop_proj.utilities.load_dataset.digits_loader import Digits_Loader
from accuracy_drop_proj.strategies.change_feature_one_by_one.change_feature_one_by_one import Change_Feature_One_By_One
from accuracy_drop_proj.strategies.change_feature_randomly.change_feature_randomly import Change_Feature_randomly
from accuracy_drop_proj.strategies.change_most_important_feature.change_most_important_feature import Change_Most_Important_Feature
from accuracy_drop_proj.strategies.change_combination.change_combination import Change_Combination
from accuracy_drop_proj.strategies.change_combination_min.change_combination_min import Change_Combination_Min
from accuracy_drop_proj.strategies.change_combination_feature_min.change_combination_feature_min import Change_Combination_Feature_Min
from accuracy_drop_proj.strategies.change_ranked_feature_informationgain.change_ranked_feature_informationgain import Change_Ranked_Feature_Informationgain
from accuracy_drop_proj.strategies.change_uncertaint_rankfeatures.change_uncertainty_rankfeatures import Change_Uncertainty_Rankfeatures
from accuracy_drop_proj.strategies.change_probabilitydistance_rankfeature.change_probabilitydistance_rankfeature import Change_ProbabilityDistance_RankFeature
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import time


# def reject_outliers(data, m=3):
#
#     if data[abs(data - np.mean(data)) < m * np.std(data)] :
#         pass
#     else:
#         print(data)
#
# def reject_outliers_2(data, m=2.):
#     d = np.abs(data - np.median(data))
#     mdev = np.median(d)
#     s = d / (mdev if mdev else 1.)
#     return data[s > m]
#
#
# #---------------------- load data set -----------------------
loader=Iris_Loader()
x_train, x_test, y_train, y_test = loader.load()
#
# print(len(x_train[:,1]))
#
# new_train=reject_outliers(x_train[:,1])
#
# print(len(new_train))
# print(new_train)

# mean = np.mean(x_train[:,[0,1,2,3]])
#
# print(mean)
# print("lllll")
# sd = np.std(x_train[:,1])
#
# for x in x_train[:,1]:
#     if x > (mean + 2 * sd):
#         print(x)





#
# import numpy
#
# arr = [10, 386, 479, 627, 20, 523, 482, 483, 542, 699, 535, 617, 577, 471, 615, 583, 441, 562, 563, 527, 453, 530, 433, 541, 585, 704, 443, 569, 430, 637, 331, 511, 552, 496, 484, 566, 554, 472, 335, 440, 579, 341, 545, 615, 548, 604, 439, 556, 442, 461, 624, 611, 444, 578, 405, 487, 490, 496, 398, 512, 422, 455, 449, 432, 607, 679, 434, 597, 639, 565, 415, 486, 668, 414, 665, 763, 557, 304, 404, 454, 689, 610, 483, 441, 657, 590, 492, 476, 437, 483, 529, 363, 711, 543]
#
# elements = numpy.array(arr)
#
# mean = numpy.mean(elements, axis=0)
# sd = numpy.std(elements, axis=0)
#
# final_list = [x for x in arr if (x > mean - 2 * sd)]
# final_list2 = [x for x in final_list if (x < mean + 2 * sd)]
# print(final_list)
# print(final_list2)
x=[]
for i in range(6):
    for j in range(6):
        if i and j != 0 and i !=j:
            x.append([i,j])
print(x)