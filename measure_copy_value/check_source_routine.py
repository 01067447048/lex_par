from sentence_transformers import SentenceTransformer, util
import os
from exception import JMeasureError
from filecontroller import Reader, Explorer
from typing import List

class CheckSourceRoutine:

    def __init__(self, source: str, word_embedding_value: List[dict]):
        self.source = source
        self.model = SentenceTransformer('krlvi/sentence-t5-base-nlpl-code_search_net')
        self.value = word_embedding_value

    def check_value(self, root: str):
        explorer = Explorer(root)
        explorer_paths = explorer.get_paths()

        for path in explorer_paths:
            tmp = path.split('.')
            key = tmp[len(tmp)-1]
            target = Reader(path)
            for value in self.value:
                if value['file'] == key:
                    value['score'] = value['score'] * util.cos_sim(self.model.encode(self.source), self.model.encode(target.get_source()))[0][0]
                    break