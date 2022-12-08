from gensim.models import Word2Vec
from lexer import Embedder

class W2V:
    def __init__(self):
        self.model = None
        self.tokens = Embedder().embedding_dict
        # tokens = [key for key, value in self.tokens.items()]
        # print(tokens)
        # print(len(tokens))

    def train(self, embedding_result):
        print(embedding_result)
        self.model = Word2Vec(
            sentences=embedding_result,
            vector_size=100,
            window=5,
            hs=1,
            min_count=1,
            workers=2
        )
        self.model.save('word2vec.model')
        print("말뭉치 개수 ->", self.model.corpus_count)
        print("말뭉치 내 전체 단어수 ->", self.model.corpus_total_words)

    def get_source_vectors(self, source, model):
        source_embedding_list = []
        doc2vec = None
        count = 0
        for line in source.split('\n'):
            count += 1
            if doc2vec is None:
                doc2vec = model.wv[line]
            else:
                doc2vec = doc2vec + model.wv[line]

        if doc2vec is not None:
            doc2vec = doc2vec / count
            source_embedding_list.append(doc2vec)

        return source_embedding_list, doc2vec