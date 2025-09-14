# Basics of logistic regression

# Import relevant libraries
import pandas as pd
import numpy as np 
import statsmodels.api as sm 
import matplotlib.pyplot as plt
import seaborn as sn 
sns.set()

# Load the data
raw_data = pd.read_csv('csv_file_name')
data=raw_data.copy()
data['Admitted'] = data['Admitted'].map({'Yes':1, 'No':0})

# Variables
y=data['Admitted']
x1=data['SAT']

#Regression
x=sm.add_constant(x1)
reg_log=sm.Logit(y,x)
results_log=reg_log.fit()

# Accuracy
np.set_printoptions(formatter={'float':lambda x: "{0:0.2f}".format(x)})
results_log.predict()
results_log.pred_table()
cm_df = pd.DataFrame(results_log.pred_table()) # Confusion matrix



#Lets Plot the data
# Scatter Plot
plt.scatter(x1,y,color='C0')
plt.xlabel('SAT')
plt.ylabel('Admitted')
plt.show()
