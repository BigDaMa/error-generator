import os
import requests
import zipfile
from gensim.models import KeyedVectors
from methodss.primary_function.inst_checker import Factory,Download,Load
from operator import itemgetter


class Word2vec_Nearest_Neighbor():
    def __init__(self,name="Word2vec_Nearest_Neighbor"):
        self.name=name
        self.called = False

    def run(self,row,col,selected_value,dataset):
        similar=[]

        if self.called == False:
            ins_download = Download()
            f = Factory()
            f.get_class(ins_download, dataset)
            l=Load()
            l.load()
            self.called = True

        # Pick a word
        find_similar_to = selected_value

        # Finding out similar words [default= top 10]
        for similar_word in l.en_model.similar_by_word(find_similar_to):
            print("Word: {0}, Similarity: {1:.2f}".format(similar_word[0], similar_word[1]))
            similar.append([similar_word[0], similar_word[1]])
        list_similar = sorted(similar, key=itemgetter(1), reverse=True)
        print(similar)
        return list_similar[0][0]