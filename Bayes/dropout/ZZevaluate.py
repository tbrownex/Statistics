import numpy as np

from calcRMSE      import calcRMSE

def calcMean(preds):
    ''' These are predictions over the same test data run repeatedly (one column for each run).
    Each run will produce a slightly different prediction due to "dropout" being specified. '''    
    mu    = np.mean(preds, axis=1)
    sigma = np.std(preds, axis=1)
    return mu, sigma

def evaluteSigma(actuals, mu, sigma):
    # What percent of the time was the actual within 1 or 2 StdDevs of the predicted?
    # "mu" is the mean of the predictions for a row
    Z = np.abs(actuals - mu) / sigma
    oneSigma = np.sum(Z<1) / Z.shape[0]
    twoSigma = np.sum(Z<2) / Z.shape[0]
    return np.round(oneSigma, decimals=3), np.round(twoSigma, decimals=3)

def evaluate(actuals, preds):
    ''' get the overall RMSE and see how accurate mean+sigma was '''
    mu, sigma = calcMean(preds)
    rmse = calcRMSE(actuals, mu)
    #oneSigma, twoSigma = evaluteSigma(actuals, mu, sigma)
    return rmse, None, None
    #return rmse, oneSigma, twoSigma
