from datetime import datetime
import os
from os import listdir
from os.path import isfile, join

import librosa
import librosa.display

import numpy as np
import pandas as pd

# noinspection PyUnresolvedReferences
from tensorflow.keras.models import Sequential, load_model
# noinspection PyUnresolvedReferences
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, GlobalAveragePooling2D
# noinspection PyUnresolvedReferences
from tensorflow.keras.utils import to_categorical
# noinspection PyUnresolvedReferences
from tensorflow.keras.callbacks import ModelCheckpoint

from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import matplotlib.pyplot as plt
import seaborn as sns

os.environ["CUDA_VISIBLE_DEVICES"]="-1"

def predict_pneumonia(filename):
    max_pad_len = 862  # to make the length of all MFCC equal

    def extract_features(file_name):
        """
        This function takes in the path for an audio file as a string, loads it, and returns the MFCC
        of the audio"""

        try:
            audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast', duration=20)
            mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
            pad_width = max_pad_len - mfccs.shape[1]
            mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')

        except Exception as e:
            print("Error encountered while parsing file: ", file_name, e)
            return None

        return mfccs


    features = []
    data = extract_features(filename)
    features.append(data)
    features = np.array(features)  # convert to numpy array
    features = np.reshape(features, (*features.shape, 1))
    model = load_model('./model/model.h5')
    pred = model.predict(features)
    classpred = np.argmax(pred, axis=1)
    if classpred[0] == 0:
        return "Other"
    elif classpred[0] == 1:
        return "Healthy"
    elif classpred[0] == 2:
        return "Pneumonia"
