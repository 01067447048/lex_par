from lexer import Lexer, Embedder
from filecontroller import Reader, Writer, Explorer
from measure_copy_value import Measure, CheckSourceRoutine
from precheck import PreCheck, W2V, D2V
import sys
from sentence_transformers import SentenceTransformer, util
import time
from gensim.models import Word2Vec
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm
import pandas as pd


def cos_sim(a, b):
    return dot(a, b) / (norm(a) * norm(b))

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
    return writer.get_token_list()
    # return TaggedDocument(tags=[reader.get_write_path()], words=writer.get_token_list())

def create_opensource_token_file():
    if len(sys.argv) != 4:
        print('python main.py open_source_path save_embedding_path, save_token_path')
        sys.exit()

    # model = SentenceTransformer('all-MiniLM-L6-v2')
    explorer = Explorer(sys.argv[1])
    explorer_paths = explorer.get_paths()
    sentence = []
    for path in explorer_paths:
        print(path)
        sentence.append(create_opensource_token_process(path, save=sys.argv[2], token_save_path=sys.argv[3]))
    w2v(sentence)
    # documents = []
    #
    # for path in explorer_paths:
    #     print(path)
    #     documents.append(create_opensource_token_process(path, save=sys.argv[2], token_save_path=sys.argv[3]))
    # d2v(documents)

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
        start = time.time()
        measure = Measure(create_source_token(path))
        measure.measure('Python')
        print(f'source_file: {path} / score: {measure.pair[0]} / taken time: {time.time() - start:.5f} sec')
        # print(f'source_file: {path} / score: {measure.pair[len(measure.pair)-1]}')
        # print(measure.pair)

def test():
    reader = Reader('./OpenSource/blockchain-python/account.py')
    reader2 = Reader('./test_source/gameRole.py')
    # model = SentenceTransformer('krlvi/sentence-msmarco-bert-base-dot-v5-nlpl-code_search_net')
    model = SentenceTransformer('krlvi/sentence-t5-base-nlpl-code_search_net')
    # model = SentenceTransformer('flax-sentence-embeddings/st-codesearch-distilroberta-base')
    # model = SentenceTransformer('mchochlov/codebert-base-cd-ft')
    # reader1_embedding = model.encode(reader.get_source(), convert_to_tensor=True)
    # reader2_embedding = model.encode(reader2.get_source(), convert_to_tensor=True)
    reader1_embedding = model.encode(reader.get_source())
    reader2_embedding = model.encode(reader2.get_source())
    value = util.cos_sim(reader1_embedding, reader2_embedding)
    print(value, value[0], value[0][0])
    if value[0][0] > 0.75:
        print('over')
    else:
        print('lower')

def pre_check():
    if len(sys.argv) != 2:
        print('python main.py source_path')

    explorer = Explorer(sys.argv[1])
    explorer_paths = explorer.get_paths()
    result = ''

    for path in explorer_paths:
        print(path)
        precheck = PreCheck(create_source_token(path))
        precheck.precheck('Python')
        result = result + '\n' + f'source_file: {path} / most_score: {precheck.get_most_value_pair()}'
        # print(f'source_file: {path} / most_score: {precheck.get_most_value_pair()}')
    save_result(result)


def save_result(result: str):
    file = open('./result/result.txt', 'w')
    file.write(result)
    file.close()

def w2v(sentence):
    wv = W2V()
    wv.train(sentence)

def d2v(documents):
    dc = D2V(documents)


def w2v_test():
    model = Word2Vec.load('word2vec.model')
    result = f'IMPORT : {model.wv["IMPORT"]}'
    print(result)
    file = open('embedding_value_example.txt', 'w')
    file.write(result)

    print(model.wv.index_to_key)

def w2v_pretest():
    model = Word2Vec.load('word2vec.model')
    source1 = create_source_token('./test_source/source5.py')
    source2 = create_source_token('./OpenSource/blockchain-python/account.py')
    wv = W2V()
    _, doc2vec1 = wv.get_source_vectors(source1, model)
    _, doc2vec2 = wv.get_source_vectors(source2, model)
    print(cos_sim(doc2vec1, doc2vec2))

# 실제 실행 코드.
def main():
    if len(sys.argv) != 2:
        print('python main.py source_path')
        exit()
    main_start_time = time.time()
    explorer = Explorer(sys.argv[1])
    explorer_paths = explorer.get_paths()
    print(f'file count : {len(explorer_paths)}')
    result = []

    for path in explorer_paths:
        start = time.time()
        print(f'{path} start')
        precheck = PreCheck(create_source_token(path))
        precheck.precheck('Java') ## Guesslang 이식을 하다가 말아서. 소스가 무슨 언어로 되어있는지 판별이 추가가 되어야 함.
        check = CheckSourceRoutine(Reader(path).get_source(), precheck.result)
        # ./OpenSource/{language}
        check.check_value('./OpenSource', 'Java') ## forder 이름 맞춰주기.
        # print(f'source_file: {path} / most_score: {check.value}')
        if len(check.result) > 0:
            print(f'source_file: {path} / most_score: {check.result[0]} / taken time : {time.time() - start:.5f} sec')
            result.append({'source_file': path, 'value': check.result, 'taken time': f'{time.time() - start:.5f} sec'})
        else:
            print(f'source_file: {path} / [], taken time : {time.time() - start:.5f} sec')
            result.append({'source_file': path, 'value': '[]', 'taken time': f'{time.time() - start:.5f} sec'})
        # result.append({'source_file': path, 'value': check.result[0], 'taken time': f'{time.time() - start:.5f} sec'})

    df = pd.DataFrame(result)
    # print(df)
    df.to_csv('result.csv')
    print(f'total : {time.time() - main_start_time:.5f} sec')

if __name__ == '__main__':
    create_opensource_token_file()  # Word2Vec 으로 오픈 소스의 문서 자체를 벡터화 진행. (학습)
    main() # 시스템을 동작 시키는 과정.

# 학습 과정.
# 1. 렉서 > 소스코드 분석 > 예약어 구분 > 인코딩 & 임베딩 > W2V > D2V(Document 2 Vector)

# 시스템을 동작 시키는 과정.
# 작성된 코드를 가지고 > 어떤 언어로 구성 되어 있는지 판별 (Guesslang) >
# 렉서 > 소스코드 분석 > 예약어 구분 > 인코딩 & 임베딩 > W2V > D2V(Document 2 Vector)
# D2V Score 1번의 과정 지나쳐온 여러 오픈소스들과 비교 문서의 유사도를 측정(코사인 유사도)
# -1 < < 1 >>> result < 0 >> 버려요. (코드의 형태가 아니라는 반증) stop  // result > 0
# SBERT 1번코드 (시스템내에 갖고 있는 오픈소스) / 2번코드 (작성된 코드) result2
# result2 * result = score

# BERT > 개선버전 SBERT (Sentence BERT) Fine tunning