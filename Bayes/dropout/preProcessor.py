import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def splitLabel(arr):
    ''' Last column of array is the label (house price) '''
    X = arr[:,:-1]
    Y = arr[:,-1:]
    return X,Y

def preProcess(arr, config):
    '''
    - Split label and features
    - Split Train and Test
    - Get Normalization parameters from Train and apply to both Train and Test
    Do not normalize Label
    '''
    X, Y  = splitLabel(arr)
    
    d = {}
    d["trainX"], d["testX"], d["trainY"], d["testY"] = train_test_split(X, Y, test_size=config["testSize"])
    
    scaler = StandardScaler().fit(d["trainX"])
    d["trainX"] = scaler.transform(d["trainX"])
    d["testX"] = scaler.transform(d["testX"])
    return d