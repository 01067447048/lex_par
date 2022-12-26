from lexer import Embedder
import os
from .word2vec import W2V
from gensim.models import Word2Vec
from numpy import dot
from numpy.linalg import norm
import chardet


def cos_sim(a, b):
    return dot(a, b) / (norm(a) * norm(b))

class PreCheck:

    def __init__(self, source):
        self.embedding_dict = Embedder().embedding_dict
        self.model = Word2Vec.load('word2vec.model')
        self.wv = W2V()
        _, self.source = self.wv.get_source_vectors(source, self.model)
        self.pair = {}
        self.result = []


    def pre_process_source(self, source: str):
        token = []
        source_list = source.split('\n')
        for so in source_list:
            token.append(so)

        return token

    def check_data(self, path, file_name: str):
        # file = open(path, 'rb')
        # encoding = chardet.detect(file.read())
        # print(encoding)
        # file.close()
        file = open(path, 'r')
        tokens = file.read()
        file.close()
        # tokens = []
        # while True:
        #     line = file.readline()
        #     if not line:
        #         break
        #     tokens.append(line)
        _, target_matrix = self.wv.get_source_vectors(tokens, self.model)
        score = cos_sim(self.source, target_matrix)

        if score < 0:
            self.result.append({'file': file_name.split('.')[0], 'score': 0})
        else:
            self.result.append({'file': file_name.split('.')[0], 'score': score})



    def precheck(self, root: str):
        file_path = './token_path/' + root
        files = os.listdir(file_path)
        for file in files:
            path = os.path.join(file_path, file)
            self.check_data(path, file)

        self.result = sorted(self.result, key=lambda x: x['score'], reverse=True)

    def get_most_value_pair(self):
        self.pair = self.result[0]
        return self.pair