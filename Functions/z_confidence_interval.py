import math
from scipy import stats
## one tail z test, if you want to count 95% confidence inverval of 2 tail
## z_prop is 0.975
def z_conf_interval(xbar,sigma,z_prop,n):
    minimun=xbar-stats.norm.ppf(z_prop)*(sigma/math.sqrt(n))
    maximun=xbar+stats.norm.ppf(z_prop)*(sigma/math.sqrt(n))
    print([minimun,maximun])
