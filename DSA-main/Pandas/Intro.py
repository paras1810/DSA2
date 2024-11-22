import pandas as pd

pd.options.display.max_rows = 20

#DataFrame
data_df = {
    'cars' : ['BMW', 'FORTUNER', 'MERCEDES'],
    'passings' : [5, 7, 2]
}

i = 0
data_df = pd.DataFrame(data_df, index=["Cars"+str(i) for i in range(3)])
print(data_df.head())
print(data_df.tail(2))
print(data_df.info())

# By default dropna return new dataframe we can use inplace also
new_df = data_df.dropna()
new_df = data_df['passings'].fillna(130)
data_df_mean = data_df['passings'].mean() #median, mode

#data_df['date'] = pd.to_datetime(data_df['date'])



print(pd.__version__)

#Series
a = [1, 7, 2]
x = pd.Series(a, index=["x", "y", "z"])
print(x)

#Loc for looking rows
#print(data_df.loc[0])
#print(data_df.loc[[0, 1]])
print(data_df.loc[['Cars2']])

#df = pd.read_csv('file_name.csv')
#df = pd.read_json('file_name.json')

