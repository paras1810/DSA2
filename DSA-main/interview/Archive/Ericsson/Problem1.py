arr = (5)
print(type(arr))

dict_input = {
    "a": 5,
    "b": 10,
    "c": 15
}
del(dict_input["b"])
print(dict_input)
dict_result = {
    
}
for key,value in dict_input.items():
    if key=="b":
        pass
    else:
        dict_result[key]=value
print(dict_result)
del(dict_input["b"])


a = [1,2,3]
b = [4,a]
del a
print(b)

# [4, [1,2,3]]

w = [[]] *3
w[0].append(23)
w[1].append(11)
w.append(55)

# [[23,55], [11,55], [55]]

f = lambda x: (x, x**2)[x > 0]
print(f(-2), f(2))

# -2, 4

import pandas as pd
colors={'first_set':['99', '88', '77', '66','55', '44', '33', '22'],
        'second_set': ['1', '2', '3', '4', '5','6', '7', '8']}
# Convert second_set datatype into int
# Filter all elements where value are in [6, 7, 8]
# Convert first_set elements into 'Q' where second_element is '5'


# Using Dict
colors['second_set'] = list(map(int, colors['second_set']))

filtered_values = [val for val in colors['second_set'] if val in [6, 7, 8]]

for i, val in enumerate(colors['second_set']):
    if val==5:
        colors['first_set'][i]='Q'

df = pd.DataFrame(colors)
df['second_set'] = df['second_set'].astype(int)
filtered = df[df['second_set'].isin([6,7,8])]
df.loc[df['second_set']==5, 'first_set']='Q'

 