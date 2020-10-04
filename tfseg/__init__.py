from tfseg.model import MODEL, cut_func


def cut(sent: str):
    for word in cut_func(MODEL, sent, use_pos=False):
        yield word


def lcut(sent: str):
    return cut_func(MODEL, sent, use_pos=False)
