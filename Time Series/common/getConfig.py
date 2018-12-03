''' A dictionary object holds key parameters such as:
    - the location of the input data file
    - the name of the label
    - the location and name of the log file
    - the default logging level
    - how many periods to use for training
    - how many periods to use for test

__author__ = "The Hackett Group"'''

def getConfig():

    d = {}
    d["dataLoc"]     = "/home/tbrownex/data/Hackett/Boeing/"
    d["fileName"]    = "tonyAdjustedByPool.csv"
    d["labelColumn"] = "18"
    d["logLoc"]      = "/home/tbrownex/"
    d["logFile"]     = "BoeingPool.log"
    d["logDefault"]  = "info"
    d["trainingSize"]= 24
    d["testSize"]    = 6
    d["numForecasts"]= 3
    
    return d