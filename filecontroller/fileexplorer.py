import os
from typing import List

class Explorer:
    def __init__(self, root_dir: str):
        self.paths = []
        self.root = root_dir
        self.explorer_file(root_dir)

    def explorer_file(self, root):
        files = os.listdir(root)
        for file in files:
            path = os.path.join(root, file)
            if os.path.isdir(path):
                self.explorer_file(path)
            else:
                # if os.path.splitext(path)[1] == '.c' or os.path.splitext(path)[1] == '.h' or os.path.splitext(path)[1] == '.java' or os.path.splitext(path)[1] == '.py':
                #     self.paths.append(path)
                if os.path.splitext(path)[1] == '.py':
                    self.paths.append(path)
                else:
                    continue

    def get_paths(self) -> List:
        return self.paths