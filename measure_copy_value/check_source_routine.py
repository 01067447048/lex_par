from sentence_transformers import SentenceTransformer, util
import os
from exception import JMeasureError
from filecontroller import Reader, Explorer
from typing import List
from .config import THRESHOLD

class CheckSourceRoutine:

    def __init__(self, source: str, word_embedding_value: List[dict]):
        self.source = source
        self.model = SentenceTransformer('krlvi/sentence-t5-base-nlpl-code_search_net') ## Python
        self.java_model = SentenceTransformer('ncoop57/codeformer-java') ## Java
        self.value = word_embedding_value
        self.result = []

    def check_value(self, root: str, lang: str):
        explorer = Explorer(root)
        explorer_paths = explorer.get_paths()

        for path in explorer_paths:
            tmp: list = path.split('.')
            key: str = tmp[len(tmp)-2][1:].replace('/', '_')
            target = Reader(path)
            for value in self.value:
                if value['file'] == key:
                    # print(f'value: {value["score"]}')
                    # print(f'cos: {util.cos_sim(self.model.encode(self.source), self.model.encode(target.get_source()))}')
                    # self.value['score'] = value['score'] * util.cos_sim(self.model.encode(self.source), self.model.encode(target.get_source()))[0][0]
                    # if lang == 'Python':
                    #     cos_value = value['score'] * util.cos_sim(self.model.encode(self.source), self.model.encode(target.get_source()))[0][0]
                    # elif lang == 'Java':
                    #     cos_value = value['score'] * util.cos_sim(self.java_model.encode(self.source), self.java_model.encode(target.get_source()))[0][0]
                    # else:
                    #     cos_value = 0.0

                    cos_value = value['score'] * \
                                util.cos_sim(self.model.encode(self.source), self.model.encode(target.get_source()))[0][0]
                    if cos_value >= 0.5:
                        self.result.append(
                            {
                                'file': value['file'],
                                'score': cos_value
                            }
                        )
                        break
        self.result = sorted(self.result, key=lambda x: x['score'], reverse=True)