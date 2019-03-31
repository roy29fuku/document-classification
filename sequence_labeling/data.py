import os
import nltk
import numpy as np
from sklearn.model_selection import train_test_split


def load_penn_treebank_data(train_size=0.7):
    sents = nltk.corpus.treebank.tagged_sents()
    sents = [np.array(s).transpose() for s in sents]
    train_data, test_data = train_test_split(sents, train_size=train_size, test_size=1-train_size)
    print('train size: {}'.format(len(train_data)))
    print('test size: {}'.format(len(test_data)))
    return train_data, test_data


def load_conll_2003_data():
    data_dir = '../data/conll_2003/'
    train_file_path = os.path.join(data_dir, 'eng.train')
    test_file_path = os.path.join(data_dir, 'eng.testb')
    train_data = _load_conll_2003_data(train_file_path)
    test_data = _load_conll_2003_data(test_file_path)
    return train_data, test_data


def _load_conll_2003_data(file_path):
    data = []
    sentence, label = [], []

    with open(file_path) as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('-DOCSTART-'):
                continue

            if line:
                word, pos, _, _ = line.split()
                sentence.append(word)
                label.append(pos)
            else:
                if not sentence:
                    continue
                data.append([sentence, label])
                sentence, label = [], []
    return data

