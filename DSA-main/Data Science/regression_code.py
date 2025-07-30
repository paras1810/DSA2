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

from sklearn.linear_model import LinearRegression
x=data['SAT'] #feature
y=data['GPA'] #target
x_matrix=x.values.reshape(-1,1)
reg=LinearRegression()
reg.fit(x_matrix,y)
reg.score(x_matrix,y)
reg.coef_
reg.intercept_
reg.predict(1740)
reg.score(x,y)

from sklearn.feature_selection import f_regression 
f_regression(x,y) # gives F-statistics[0] and p-values[1]
reg_summary=pd.DataFrame(data=['SAT','Rand'], columns=['Features'])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x)
# Output StandardScaler(copy=True, with_mean=True, with_std=True)
x_scaled = scaler.transform(x)

reg=LinearRegression()
reg.fit(x_scaled,y)
reg.coef_ 
reg.intercept_
reg_summary=pd.DataFrame([['Intercept'], ['SAT'],['Rand 1,2,3']], columns=['Features'])

new_data = pd.DataFrame(data=[[1700,2],[1800,1]],columns=['SAT', 'Rand 1,2,3'])
new_data
reg.predict(new_data)
new_data_scaled = scaler.transform(new_data)

from sklearn.model_selection import train_test_split
a=np.arange(1,101)









