import os
import requests
import zipfile

from __future__ import print_function
from gensim.models import KeyedVectors

from methodss.primary_function.inst_checker import Inst_checker


class Word2vec_Nearest_Neighbor():
    def __init__(self):
        pass


    def run(self,row,col,selected_value,dataset):

        while (flag==True):
            Inst_checker.factory("first-run")
            flag=False

        Inst_checker.factory("load")

        
