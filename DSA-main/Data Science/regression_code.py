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
a_train, a_test = train_test_split(a, test_size=0.2, shuffle=False)
a_train.shape, a_test.shape
# Random number Default 75:25 split.

#Car Sales Data Code:
raw_data = pd.read_csv('1.04. Real-life example.csv')
raw_data.head()

# Preprocessing
## Exploring the descriptive statistics of the variables
raw_data.describe(include='all')
data = raw_data.drop(['Model'],axis=1)
data.isnull.sum()
data_no_mv=data.dropna(axis=0)
sns.distplot(data_no_mv['Price'])

#For removing the outliers
q=data_no_mv['Price'].quantile(0.99)
data_1 = data_no_mv[data_no_mv['Price']<q]
data_cleaned = data_1.reset_index(drop=True)

#Checking OLS assumptions:
sns.distplot(data_cleaned['Price'])
np.log(x) = np.log(data_cleaned['Price']) #No Endogenity
# Normality and Homoscedasticity
# No autocorrelation 
cols = data_cleaned.columns.values
#VIF Variance inflation factor
data_no_multicollinear = data_cleaned.drop(['Year'], axis=1)
# Create dummy variables:
data_with_dummies = pd.get_dummies(data_no_multicollinear, drop_first=True)
data_preprocessed = data_with_dummies[cols]

# Declare inputs and targets
targets=data_preprocessed['log_price']
inputs = data_preprocessed.drop(['log_price'], axis=1)
scaler1=StandardScaler()
scaler1.fit(inputs)
input_scaled=scaler1.transform(inputs)
  

## Determining the variables of interests

## Dealing with missing values










