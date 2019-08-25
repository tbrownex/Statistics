import numpy as np

def getData(config):
    arr = np.loadtxt(config["dataLoc"]+config["fileName"])
    print("Data has {} rows and {} columns".format(arr.shape[0], arr.shape[1]))
    return arr