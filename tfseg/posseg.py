from tfseg.model import MODEL, cut_func


def cut(sent: str):
    for word, pos in zip(*cut_func(MODEL, sent, use_pos=True)):
        yield (word, pos)


def lcut(sent: str):
    return [
        (word, pos)
        for word, pos in zip(*cut_func(MODEL, sent, use_pos=True))
    ]
