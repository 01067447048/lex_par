from lexer import Lexer, Embedder
from filecontroller import Reader, Writer, Explorer
from measure_copy_value import Measure
import sys

def create_opensource_token_process(source: str, save: str, token_save_path: str):
    reader = Reader(source)
    lexer = Lexer(reader.get_source())
    tokens = lexer.lex()
    token = '\n'.join(map(str, tokens))
    # print(token)
    # file = open(f'token{times}.txt', 'w')
    # file.write(token)

    embedder = Embedder()
    writer = Writer(reader.get_write_path(), save, embedder.get_embedding(tokens), token_save_path, token)


def create_opensource_token_file():
    if len(sys.argv) != 4:
        print('python main.py open_source_path save_embedding_path, save_token_path')
        sys.exit()

    # model = SentenceTransformer('all-MiniLM-L6-v2')
    explorer = Explorer(sys.argv[1])
    explorer_paths = explorer.get_paths()

    for path in explorer_paths:
        print(path)
        create_opensource_token_process(path, save=sys.argv[2], token_save_path=sys.argv[3])

def create_source_token(path: str):
    reader = Reader(path)
    lexer = Lexer(reader.get_source())
    tokens = lexer.lex()
    return '\n'.join(map(str, tokens))

def measure_process():
    if len(sys.argv) != 2:
        print('python main.py source_path')

    explorer = Explorer(sys.argv[1])
    explorer_paths = explorer.get_paths()

    for path in explorer_paths:
        print(path)
        measure = Measure(create_source_token(path))
        measure.measure('Python')
        print(f'source_file: {path} / score: {measure.pair[len(measure.pair)-1]}')


if __name__ == '__main__':
    # create_opensource_token_file()
    measure_process()