from tfseg.model import MODEL, cut_func
from tfseg.pair import pair


def cut(sent: str):
    for word, pos in zip(*cut_func(MODEL, sent, use_pos=True)):
        yield pair(word, pos)


def lcut(sent: str):
    return [
        pair(word, pos)
        for word, pos in zip(*cut_func(MODEL, sent, use_pos=True))
    ]
