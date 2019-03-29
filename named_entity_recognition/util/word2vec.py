from .data import load_sentences


if __name__ == '__main__':
    X_train, y_train, X_valid, y_valid, X_test, y_test = load_sentences()
    # TODO: gensim word2vev
    # gensim corpora dictionary
    # などでword embedding作成？