"""Copy from silence-tensorflow
https://github.com/LucaCappelletti94/silence_tensorflow/blob/aa02373647db93f92ec824a55f37b6ae175d7227/silence_tensorflow/silence_tensorflow.py#L5
"""

import os
import logging


def silence_tensorflow():
    """Silence every warning of notice from tensorflow."""
    logging.getLogger('tensorflow').setLevel(logging.ERROR)
    os.environ["KMP_AFFINITY"] = "noverbose"
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    import tensorflow as tf
    tf.get_logger().setLevel('ERROR')
    tf.autograph.set_verbosity(3)
