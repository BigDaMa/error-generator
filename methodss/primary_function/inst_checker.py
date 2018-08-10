import os
import zipfile
import requests
from __future__ import print_function
from gensim.models import KeyedVectors


class Inst_checker(object):
    def factory(type):
        if type == "download":
            return Download
        if type== "load":
            return

#fix the addresses

class Download(object):

    def download(self):
        if (os.path.isfile('../../../datasets/wiki-news-300d-1M.vec')==False):

            print("The pre-trained file is not available so we automatically downloaded it\n please be patient!")

            url="https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki-news-300d-1M.vec.zip"
            target_path="../../../datasets/"

            response = requests.get(url, stream=True)
            handle = open(target_path, "wb")
            for chunk in response.iter_content(chunk_size=512):
                if chunk:  # filter out keep-alive new chunks
                    handle.write(chunk)


            zip_ref = zipfile.ZipFile("../../../datasets/wiki-news-300d-1M.vec.zip", 'r')
            zip_ref.extractall("./")
            zip_ref.close()

class Load(object):
    def load(self):
        # Creating the model
        self.en_model = KeyedVectors.load_word2vec_format('wiki-news-300d-1M.vec')