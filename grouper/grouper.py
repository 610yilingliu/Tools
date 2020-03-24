import pandas as pd
import random
from random import shuffle


f = pd.read_csv('students.csv', delimiter = "   ", encoding = "gb2312")
accounting = pd.DataFrame(f[f['major'] == '会计']).reset_index()
finance = pd.DataFrame(f[f['major'] == '经济']).reset_index()
others = pd.DataFrame(f[(f['major'] != '经济') and (f['major'] != '会计')]).reset_index()

wenke = []
like = []
# init a dataframe, use for loop to merge majors in dict(concat works)

print('会计系人数' + str(len(accounting)))
print('经院人数' + str(len(finance)))
print('其他' + str(len(others)))


random.seed(1)
kuaiji = [i for i in range(len(accounting))]
shuffle(kuaiji)
