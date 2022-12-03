from exception import JFileReadError

class Reader:

    def __init__(self, file_path: str):
        self.source = ''
        self.write_path = ''
        paths = file_path.split('/')
        if len(paths) < 2:
            raise JFileReadError("File Read Error")

        for path in paths:
            if path == '.' or path == '..':
                continue
            if '.' in path and len(path) > 1:
                extend = path.split('.')
                self.write_path = self.write_path + '_' + extend[0] + '.txt'
            else:
                if self.write_path == '':
                    self.write_path = path
                else:
                    self.write_path = self.write_path + '_' + path

        source = open(file_path, 'r')
        self.source = source.read()
        source.close()

    def get_source(self) -> str:
        return self.source

    def get_write_path(self) -> str:
        return self.write_path