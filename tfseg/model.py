import os
import tensorflow as tf
import tensorflow_hub as hub
from tfseg.silence_tensorflow import silence_tensorflow


silence_tensorflow()
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'chn_seg_albert')
MODEL = hub.load(MODEL_PATH)


def cut_func(model, sent: str, use_pos=True):
    if len(sent) <= 0:
        return []
    elif len(sent) > 510:
        sent = sent[:510]
    tokens = ['[CLS]'] + list(sent) + ['[SEP]']
    for lens in (32, 64, 128, 256, 512):
        if len(tokens) <= lens:
            tokens += [''] * (lens - len(tokens))
            break

    inputs = tf.constant([tokens])
    pred = model(inputs)

    words = []
    poses = []
    last_word = ''
    last_pos = ''

    pred_iter = zip(
        sent,
        pred.numpy()[0]
    )

    for w, x in pred_iter:
        x = x.decode('utf-8')
        pos = x[1:]
        if x[0] == 'B' or x[0] == 'S':
            if len(last_word):
                words.append(last_word)
                poses.append(last_pos)
                last_word = ''
                last_pos = ''
            last_word += w
            last_pos = pos
        else:
            last_word += w

    if len(last_word):
        words.append(last_word)
        poses.append(last_pos)

    if use_pos:
        return words, poses
    return words
