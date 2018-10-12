import math
from scipy import stats

## p in [0,1]
## prop in what confidence interval you want(eg:if you want 90% confidence interval,p is 0.9)
def prop_conf_interval(p,prop,n):
    minimun=p-stats.norm.ppf(1-(1-prop)/2)*math.sqrt(p*(1-p)/n)
    maximun=p-stats.norm.ppf(1-(1-prop)/2)*math.sqrt(p*(1-p)/n)
    print([round(minimun,3),round(maximun,3)])



