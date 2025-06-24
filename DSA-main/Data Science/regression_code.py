import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import statsmodel.api as sm 

data = pd.read_csv('1.01. Simple linear regression.csv')
data
data.describe() # count, mean, std, min, 25%, 75%, 50%, max
y=data['SAT']
x1=data['GPA']
plt.scatter(x1,y)
plt.xlabel('SAT',fontsize=20)
plt.ylabel('GPA',fontsize=20)
plt.show()
x=sm.add_constant(x1)
results=sm.OLS(y,x).fit()
results.summary()

import seaborn as sns
sns.set()

data = pd.read_csv('1.02. Multiple linear regression.csv')
data 
data.describe()
#GPA=b0+b1SAT+b2Rand1,2,3
y=data['GPA']
x1=data[['SAT', 'Rand 1,2,3']]
results.summary()

