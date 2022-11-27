from exception import JFileWriteError
import os
from typing import List

class Writer:
    def __init__(self, file_path: str, default_path: str, tokens: List):
        self.default_path = './' + default_path + '/' + file_path
        if len(file_path.split('.')) < 2:
            raise JFileWriteError('Writer Error')

        try:
            if not os.path.exists('./' + default_path):
                os.makedirs('./' + default_path)
            file = open(self.default_path, 'w')
            for token in tokens:
                if token == 99:
                    file.write(f'{token}')
                else:
                    file.write(f'{token}, ')
            file.close()
        except JFileWriteError:
            print('Create Directory Error')