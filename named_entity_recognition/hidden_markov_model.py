import nltk
import numpy as np
import re
from util import data_loader

# BOS, EOS, UNKを設定
BOS = '<BOS>'
EOS = '<EOS>'
UNK = '<UNK>'


def _get_unk_words_replaced_corpus(corpus):
    """
    未知語リストに含まれる単語は<UNK>で置換する
    """
    unk_words = _get_unk_words(corpus)
    return [[(wt[0], wt[1]) if wt[0] not in unk_words else (UNK, wt[1]) for wt in s] for s in corpus]


def _get_unk_words(corpus, num=1):
    """
    出現回数一定以下の単語を未知語としてリストにまとめる
    """
    word_list = [wt[0].lower() for s in corpus for wt in s]
    word_list = [re.sub(r'[0-9]+', '0', w) for w in word_list]
    fdist = nltk.FreqDist(word_list)
    unk_words = []
    for k, v in fdist.items():
        if v <= num:
            unk_words.append(k)
    return unk_words


def _split_data(corpus, ratio=0.9):
    """
    train, testデータに分ける
    """
    num = len(corpus)
    train_data = corpus[:int(num * ratio)]
    test_data = corpus[int(num * ratio):]

    # 動作確認用
    # train_data = [
    #     [('they', 'N'), ('saw', 'V'), ('a', 'D'), ('bear', 'N')],
    #     [('we', 'N'), ('meet', 'V'), ('a', 'D'), ('man', 'N')],
    #     [('a', 'D'), ('man', 'N'), ('bear', 'V'), ('a', 'D'), ('gold', 'N')],
    # ]
    # # 全ての遷移、出力のパターンはtrainに含まれている
    # test_data = [
    #     [('a', 'D'), ('bear', 'N'), ('saw', 'V'), ('a', 'D'), ('man', 'N')]
    # ]
    return train_data, test_data


def _get_words_and_tags(corpus):
    """
    単語と品詞のリストを取得
    """
    words = list(set([wt[0] for s in corpus for wt in s])) + [BOS, EOS]
    tags = list(set([wt[1] for s in corpus for wt in s])) + [BOS, EOS]
    return words, tags


def _get_freq(count_matrix):
    """
    カウントの行列を確率に変換する
    = 行の合計を1にする
    """
    freq_matrix = np.zeros(count_matrix.shape)
    for i, row in enumerate(count_matrix):
        freq_row = np.zeros(len(row))
        if sum(row) != 0:
            freq_row = row / sum(row)
        freq_matrix[i] = freq_row

    return freq_matrix


if __name__ == '__main__':
    X_train, y_train, X_valid, y_valid, X_test, y_test = data_loader.load_sentences()
    print(X_test[0])
