import pandas as pd
import numpy as np


data = [15,4,3,8,15,22,7,9,2,3,3,12,6]

x = pd.Series(data)
print('The standard dev of this data is:',np.std(x))
print('The number of samples in this data is:',len(x))
print('The first quartile is:',np.quantile(x,q=0.25))
print('The median is:',np.quantile(x,q=0.5))
print('The third quantile is:',np.quantile(x,q=0.75))
print('The mean of these data is:',np.mean(x))
print('The variance of these data is:',np.std(x)**2)
