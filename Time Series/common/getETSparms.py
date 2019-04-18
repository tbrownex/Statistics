def getETSparms():
    '''
    As part of an ETS grid search, build a list of different combinations of parameters
    for the ETS "model" and the "fit"
    '''
    mParms   = []
    trend    = ["add"]
    damped   = [True]
    seasonal = ["add"]
    seasonalPeriods = [12]
        
    for t in trend:
        for d in damped:
            for s in seasonal:
                for p in seasonalPeriods:
                    x = {}
                    x["trend"]    = t
                    x["damped"]   = d
                    x["seasonal"] = s
                    x["periods"]  = p
                    mParms.append(x)
                    
    fParms   = list()
    BoxCox = [False]
    bias   = [False]
    alpha = [0.1*x for x in range(3,8)]
    #alpha = [0.7]
    beta = [0.1*x for x in range(2,6)]
    #beta = [0.3]
    gamma = [0.2*x for x in range(1,5)]
    #gamma = [0.2]
    for BC in BoxCox:
        for b in bias:
            for A in alpha:
                for B in beta:
                    for G in gamma:
                        x = {}
                        x["BoxCox"]     = BC
                        x["RemoveBias"] = b
                        x["smoothing_level"] = A
                        x["smoothing_slope"] = B
                        x["smoothing_seasonal"] = G
                        fParms.append(x)
    
    return mParms, fParms