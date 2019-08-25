''' A dictionary object holds key parameters such as:
    - the location and name of the input data file
    - the location and name of the log file
    - the default logging level
    - an indicator allowing execution in Test mode'''

__author__ = "The Hackett Group"

def getConfig():
    d = {}
    d["dataLoc"] = "/home/tbrownex/data/"
    d["fileName"] = "bostonHousing.csv"
    d["testSize"] = 0.2
    d["labelType"]   = "continuous"
    d["evaluationMethod"] = "--"
    d["logLoc"]     = "/home/tbrownex/"
    #d["logFile"]    = "demoCPU.log"
    #d["logDefault"] = "info"
    d["TBdir"] = '/home/tbrownex/TF/TensorBoard'         # where to store Tensorboard data
    d["modelDir"] = "/home/tbrownex/TF/models/"  # where to save models
    return d