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

#students.grade = students.grade.astype(int)

'''
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
Melt in Pandas
'''
# pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')

# df.drop_duplicates('email')

# students.rename(columns={'id':'student_id', 'first':'first_name','last':'last_name','age':'age_in_years'}, inplace=True)

data_df.shape
