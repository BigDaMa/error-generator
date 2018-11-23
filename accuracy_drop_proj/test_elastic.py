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



import numpy as np


x = {1:2}
print (x)


x.update({1:5})
print (x)
