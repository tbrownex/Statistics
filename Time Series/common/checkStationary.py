from statsmodels.tsa.stattools import adfuller

def checkStationary(ts, CI):
    '''
    - "ts" is a Series
    - "CI" is a confidence interval
    - "results" is a dictionary of confidence intervals with associated value
    '''
    assert (CI in ["1%", "5%", "10%"]), "Invalid confidence interval. Should be '1%', '5%' or '10%'"
    
    adf = adfuller(ts)
    
    ADFstat = adf[0]
    Pvalue  = adf[1]
    results = adf[4]
    if ADFstat < results[CI]:
        return True
    else:
        return False