from sentence_transformers import SentenceTransformer, util
import os
from exception import JMeasureError

class Measure:

    def __init__(self, source: str):
        # self.model = SentenceTransformer('all-MiniLM-L6-v2')
        # self.model = SentenceTransformer('flax-sentence-embeddings/st-codesearch-distilroberta-base')
        # self.model = SentenceTransformer('mchochlov/codebert-base-cd-ft')
        self.model = SentenceTransformer('krlvi/sentence-t5-base-nlpl-code_search_net')
        self.target_embedding = self.model.encode(source, convert_to_tensor=True)
        self.source_embedding = []
        self.pair = []

    def get_target_embedding(self):
        return self.target_embedding

    def find_open_source(self, root: str):
        file_path = './token_path/' + root
        files = os.listdir(file_path)
        for file in files:
            path = os.path.join(file_path, file)
            self.source_embedding.append(self.measure_value(path))

        self.measure_cos_sim()

    def measure(self, source_type: str):
        if source_type == 'Python' or source_type == 'C' or source_type == 'Java':
            self.find_open_source(source_type)
        else:
            raise JMeasureError('Plz Python or C or Java')

    def measure_cos_sim(self):
        file = ''
        value = None

        for source_dict in self.source_embedding:
            for key, value in source_dict.items():
                if key == 'file':
                    file = value
                elif key == 'embedding':
                    value = util.cos_sim(self.target_embedding, value)

            self.pair.append({'file': file, 'score': value})

        self.pair = sorted(self.pair, key=lambda x: x['score'], reverse=True)

    def measure_value(self, file: str):
        sentence2 = ''
        f = open(file, 'r')

        while True:
            line = f.readline()
            if not line:
                break
            sentence2 = sentence2 + line.replace('\n', ',')
        f.close()
        return {'file': file, 'embedding': self.model.encode(sentence2, convert_to_tensor=True)}