import pandas as pd
import numpy  as np

from getConfig         import getConfig
from getData           import getData
from preProcessor    import preProcess
from getModelParms import getParms
from calcRMSE         import calcRMSE
from nn                   import runNN
#from evaluate           import evaluate

def loadParms(x):
    ''' Load a dictionary with the hyperparameter combinations for one run '''
    d = {}
    d['l1Size']      = x[0]
    d['batchSize']   = x[1]
    d['lr']          = x[2]
    d["lambda"]      = x[3]
    d['std']         = x[4]
    d['dropout']     = x[5]
    d['dropoutTest'] = x[6]
    d['optimizer']   = x[7]
    return d

def getPreds(dataDict, parms, config):
    return preds[:,0]

# This file stores the results for each set of parameters so you can review a series
# of runs later
def writeResults(results):
    with open("/home/tbrownex/results.csv", 'w') as output:
        keys = results[0][0].keys()
        hdr = ",".join(keys)
        hdr += ","+"rmse" + "\n"
        output.write(hdr)        
        
        for x in results:
            rec = ",".join([str(t) for t in x[0].values()])
            rec += ","+ str(x[1]) +"\n"
            output.write(rec)

if __name__ == "__main__":
    config = getConfig()
    arr = getData(config)
    parms = getParms("NN")
    
    results = []
    for x in parms:
        parmDict = loadParms(x)
        loops = 10
        predArray = []
        for l in loops:
            dataDict = preProcess(arr, config)   # do this here because small data size could be affected by the train/test split
            actuals = np.reshape(dataDict["testY"], newshape=[-1,])
            
            preds = runNN(dataDict, parmDict, config)
            
            predArray.append(list(preds[:,0]))
        preds = np.array(predArray)
        rmse = calcRMSE(actuals, preds.mean(axis=1))
        tup = (parmDict, rmse)
        results.append(tup)
    writeResults(results)
    #np.savetxt("/home/tbrownex/preds.csv", np.array(predArray), delimiter=",", fmt='%.2f')