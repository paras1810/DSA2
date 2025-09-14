import numpy as np
s=5
v=np.array([5, -2, 4])
m=np.array([5,12,6],[-3,0,14])
type(s)
type(v) #numpy.ndarray
s_array=np.array(5)
m.shape

# pandas library steps on computational abilities of Numpy
import pandas as pd
products = ['A', 'B', 'C', 'D']
type(products)
product_categories = pd.Series(products)
type(product_categories)
daily_rates_dollars = pd.Series([40, 45, 50, 60])

start_date_deposits = pd.Series({
    '7/4/2014': 2000,
    '1/2/2015': 2000
})

'''
Attributes(Passive): Metadata
Methods: Functionalities and behaviour of object
    can have access to object data and state
Function: Independent entity
'''

start_date_deposits.sum() #.min(), .max(), .idxmin(), .idxmax(), .head(), .tail(), .head(3)

location_data = pd.read_csv('Location.csv', squeeze=True)
type(location_data)
location_data.describe()
len(location_data)
location_data.nunique()

numbers = pd.Series([15, 100, 23, 45, 444])
numbers.sort_values(ascending=True)

# DataFrame: A collection of one or several Series objects
array_a = np.array([[3,2,1],[6,3,2]])
type(pd.DataFrame(array_a))
df=pd.DataFrame(array_a, columns=['Column1', 'Column2', 'Column3'], index=['Row1', 'Row2'])
data = pd.read_csv('Lending_company.csv', index_col='LoanID')
lending_co_data = data.copy()
lending_co_data.head()
type(lending_co_data.index)
lending_co_data.axes
lending_co_data.dtypes
type(lending_co_data.values)

# Subset selection means extracting elements, columns, rows or subsets from an object.
lending_co_data.Product 
lending_co_data.Location
lending_co_data['Product']
lending_co_data['Location']
lending_co_data[['Location', 'Product']].head()

# .iloc integer location
lending_co_data.iloc[1]
lending_co_data.iloc[1, 3]
lending_co_data.iloc[1,:]
lending_co_data.iloc[[1,3],:]
lending_co_data.iloc[:,[3,1]]

# .loc
lending_co_data.loc[:, 'Location']









