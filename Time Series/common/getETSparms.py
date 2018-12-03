def getETSparms():
    '''
    As part of an ETS grid search, build a list of different combinations of parameters
    for the ETS "model" and the "fit"
    '''
    mParms   = []
    trend    = [None]
    damped   = [False]
    seasonal = [None]
    seasonalPeriods = [99]
        
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
    BoxCox = [True]
    bias   = [False]
    alpha = [0.1*x for x in range(6,12)]
    alpha = [1.0]
    beta = [0.1*x for x in range(5,11)]
    beta = [0.7]
    gamma = [0.2*x for x in range(1,5)]
    gamma = [0.5]
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