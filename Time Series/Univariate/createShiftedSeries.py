import numpy as np

def createData(length, shift, batch_size):
    '''
    This version has Y as 3 steps ahead of X
    Try other ways of having dependence between X and Y
    X is initially a series of length "length". It is then "reshaped" into 2-d
    array, where "ABCDEF" would become [ABC][DEF]
    '''
    X = np.array(np.random.choice(2, length, p=[0.5, 0.5]))
    Y = np.roll(X, shift)
    Y[0:shift] = 0

    X = X.reshape((batch_size, -1))
    Y = Y.reshape((batch_size, -1))

    return (X, Y)