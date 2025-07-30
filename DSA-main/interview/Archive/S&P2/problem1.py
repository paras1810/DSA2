#1
x=[10,20,30]
y={x:10
}
print(y)

#2
def method_var(x, *args, **kwargs):
    print(x)

#3
def validate(func):
    def wrapper(a, b):
        if type(a)!=int and type(b)!=int:
            print("Type of both a and b should be int")
            return 0
        return func(a, b)
    return wrapper            
@validate
def sum(a, b):
    return a+b

print(sum("str",10))
x=sum(5,10)

#4
x="Paras"
x=""
x[::-1]
y=""
for i in range(len(x)-1,-1,-1):
    y+=x[i]
y

#5
class A:
    pass
 
class B(A):
    pass
 
class C(B):
    pass
 
class D(C, B, A):
    pass

d=D()
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

#6
x,y={'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'a':5}
for key,val in y.items():
    if key in x:
        x[key]=max(x[key],val)
    else:
        x[key]=val
x

#7
result_list=[]
def flat_list(input_list):
    for i in input_list:
        if type(i)==list:
            flat_list(i)
        else:
            result_list.append(i)
        
flat_list([1,[2, [3, 4]]])
print(result_list)