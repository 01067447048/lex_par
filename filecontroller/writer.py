from exception import JFileWriteError
import os
from typing import List

class Writer:
    def __init__(self, file_path: str, default_path: str, tokens: List, token_save_path: str, str_token: str):
        self.default_path = './' + default_path + '/' + file_path
        self.token_save_path = './' + token_save_path + '/' + file_path
        self.token_list = []
        self.str_token = str_token
        if len(file_path.split('.')) < 2:
            raise JFileWriteError('Writer Error')

        try:
            if not os.path.exists('./' + default_path):
                os.makedirs('./' + default_path)
            file = open(self.default_path, 'w', encoding='utf-8')
            for token in tokens:
                if token == 99:
                    file.write(f'{token}')
                else:
                    file.write(f'{token}, ')
            file.close()

            if not os.path.exists('./' + token_save_path):
                os.makedirs('./' + token_save_path)

            file = open(self.token_save_path, 'w', encoding='utf-8')
            file.write(str_token)
            file.close()
            token_list = str_token.split('\n')
            self.token_list = [token for token in token_list]
        except JFileWriteError:
            print('Create Directory Error')

    def get_token_list(self):
        return self.token_list

    def get_str_token(self):
        return self.str_token.replace('\n', ', ')