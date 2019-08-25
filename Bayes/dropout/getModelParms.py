import itertools
from tensorflow import keras

def getParms(typ):
    if typ == "NN":
        L1Size       = [90]
        batchSize    = [64]
        learningRate = [3e-2]
        Lambda       = [1e-3]
        std          = [0.05]
        dropout      = [0.4]
        dropoutTest  = [0.05]
        optimizer    = ["Adam"]
        return list(itertools.product(L1Size,
                                      batchSize,
                                      learningRate,
                                      Lambda,
                                      std,
                                      dropout,
                                      dropoutTest,
                                      optimizer))