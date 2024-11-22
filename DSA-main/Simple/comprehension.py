import functools
x = [3, 4, 7 ,8 ,10]
list_x = [i*i for i in x if i%2==0]
print(list_x)

dict_x = {i:i*i for i in x if i%2==0}
print(dict_x)

list_y = [(lambda i:i/2)(i) for i in x]
print(list_y)

lst = [5, 6, 7]
sum_x = functools.reduce(lambda x,y: x+y, lst)
print(sum_x)

res = [(a+b) for (a,b) in zip(x, lst)]
print(res)

res = [(a,b) for a in x for b in lst]
print(res)

my_lst = [[10,20,20], [20,20,90]]
flat = [x for temp in my_lst for x in temp]
print(flat)