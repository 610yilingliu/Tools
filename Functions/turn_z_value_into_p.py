from scipy import stats

def turn_z_into_p(z_value):
## turn z-value into p-value
    print(stats.norm.cdf(z_value))