"""
Run this script before you run below cells
1. installing tensorflow.io
2. import dependencies
3. run code

"""
import os
import json
import glob
import shutil
import random

from tqdm.notebook import tqdm

from jamo import j2hcj, h2j
from krUtils.unicodeUtil import join_jamos

import pandas as pd
import numpy as np

import scipy.signal as signal
from IPython.display import Audio

import tensorflow as tf
import tensorflow_io as tfio

seed = 42
tf.random.set_seed(seed)
np.random.seed(seed)

#%% md

## Get paths

#%%

def get_paths(types=str):
    if types == 'local':
        assert types in ['local', 'colab']
        TRAIN_YOUNG = '/Users/shinjeongtae/DB/External SSD for Data/Elderly Speech Recognition/contents/Train_young/'
        TRAIN_OLD = '/Users/shinjeongtae/DB/External SSD for Data/Elderly Speech Recognition/contents/Train_old/'
        TEST_YOUNG = '/Users/shinjeongtae/DB/External SSD for Data/Elderly Speech Recognition/contents/vali_young/'
        TEST_OLD = '/Users/shinjeongtae/DB/External SSD for Data/Elderly Speech Recognition/contents/vali_old/'
    elif types == 'colab':
        assert types in ['local', 'colab']
        TRAIN_YOUNG = '/content/drive/MyDrive/Colab Notebooks/Project/Project - Machine Learning/Project - EEVR/Contents/Train_young/'
        TRAIN_OLD = '/content/drive/MyDrive/Colab Notebooks/Project/Project - Machine Learning/Project - EEVR/Contents/Train_old/'
        TEST_YOUNG = '/content/drive/MyDrive/Colab Notebooks/Project/Project - Machine Learning/Project - EEVR/Contents/vali_young/'
        TEST_OLD = '/content/drive/MyDrive/Colab Notebooks/Project/Project - Machine Learning/Project - EEVR/Contents/vali_old/'
    else:
        raise AssertionError

    DATA_PATH = 'data'
    LABEL_PATH = 'label'

    subdir_WAV = r'/**/*.wav'
    subdir_json = r'/**/*.json'

    return TRAIN_YOUNG, TRAIN_OLD, TEST_YOUNG, TEST_OLD, DATA_PATH, LABEL_PATH, subdir_json, subdir_WAV

#%%

TRAIN_YOUNG, TRAIN_OLD, TEST_YOUNG, TEST_OLD, DATA_PATH, LABEL_PATH, subdir_json, subdir_WAV = get_paths(types='local')

