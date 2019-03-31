import torch

UNK_TOKEN = '<UNK>'
UNK = 0


def get_conversion_tables(train_data, min_count=1):
    # TODO: count words and

    word_to_ix = {
        UNK_TOKEN: UNK
    }
    tag_to_ix = {}

    for sent, tags in train_data:
        for word, tag in zip(sent, tags):
            if word not in word_to_ix:
                word_to_ix[word] = len(word_to_ix)
            if tag not in tag_to_ix:
                tag_to_ix[tag] = len(tag_to_ix)

    return word_to_ix, tag_to_ix


def prepare_sequence(seq, to_ix):
    idxs = [to_ix.get(w, UNK) for w in seq]
    return torch.tensor(idxs, dtype=torch.long)
