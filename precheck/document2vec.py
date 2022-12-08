from gensim.models import Doc2Vec
from lexer import Embedder
from gensim.models import doc2vec

class D2V:
    def __init__(self, tagged_corpus_list):
        print(tagged_corpus_list[0])
        self.model = doc2vec.Doc2Vec(vector_size=1200, alpha=0.025, min_alpha=0.025, workers=8, window=8)
        self.model.build_vocab(tagged_corpus_list)
        # print(f"Tag Size: {len(self.model.docvecs.doctags.keys())}", end=' / ')
        self.model.train(tagged_corpus_list, total_examples=self.model.corpus_count, epochs=50)
        self.model.save('dart.doc2vec')
        similar_doc = self.model.docvecs.most_similar('OpenSource_SimpleCoin_simpleCoin_miner.txt')
        print(similar_doc[0])