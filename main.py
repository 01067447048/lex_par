from lexer import Lexer, Embedder
from filecontroller import Reader, Writer, Explorer
import sys

def process(source: str, save: str):
    reader = Reader(source)
    lexer = Lexer(reader.get_source())
    tokens = lexer.lex()
    token = '\n'.join(map(str, tokens))
    print(token)
    file = open('token.txt', 'w')
    file.write(token)

    embedder = Embedder()
    writer = Writer(reader.get_write_path(), save, embedder.get_embedding(tokens))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('python main.py open_source_path save_embedding_path')
        sys.exit()

    explorer = Explorer(sys.argv[1])
    explorer_paths = explorer.get_paths()

    for path in explorer_paths:
        print(path)
        process(path, save=sys.argv[2])
