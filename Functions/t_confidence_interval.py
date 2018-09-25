import math
from scipy import stats
## one tail t test, if you want to count 95% confidence inverval of 2 tail
## t_interv is 0.975
def t_conf_interval(xbar,s,t_interv,n):
    minimun=xbar-stats.t.ppf(t_interv,n-1)*(s/math.sqrt(n))
    maximun=xbar+stats.t.ppf(t_interv,n-1)*(s/math.sqrt(n))
    print([minimun,maximun])