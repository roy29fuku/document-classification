import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/conll_2003/')
TRAIN_FILE_PATH = os.path.join(DATA_DIR, 'eng.train')
VALID_FILE_PATH = os.path.join(DATA_DIR, 'eng.testa')
TEST_FILE_PATH = os.path.join(DATA_DIR, 'eng.testb')


def load_sentences():
    """
    train, valid, testのデータを文章単位で読み込む
    これをgensimのcorporaに突っ込む
    train, test分けてから突っ込んでいいのか？
    https://qiita.com/tatsuya-miyamoto/items/f505dfa8d5307f8c6e98
    :return:
    """
    X_train, y_train = load_conll2003_sentences(TRAIN_FILE_PATH)
    X_valid, y_valid = load_conll2003_sentences(VALID_FILE_PATH)
    X_test, y_test = load_conll2003_sentences(TEST_FILE_PATH)

    return X_train, y_train, X_valid, y_valid, X_test, y_test


def load_conll2003_sentences(file_path):
    """
    CoNLL-2003形式のデータを文章単位で読み込む
    :param file_path:
    :return:
    """
    sentences, labels = [], []
    sentence, label = [], []

    with open(file_path) as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('-DOCSTART-'):
                continue

            if line:
                word, _, _, ner_label = line.split()
                sentence.append(word)
                label.append(ner_label)
            else:
                if not sentence:
                    continue
                sentences.append(sentence)
                labels.append(label)
                sentence, label = [], []

    return sentences, labels