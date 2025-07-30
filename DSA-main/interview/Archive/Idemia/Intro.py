def a(x,lst=[]):
    lst.append(x)
    return lst 

x,y=10,5
print(a(x))
print(a(y))

#10
#10,5
# You might expect a fresh list, but because default mutable arguments are shared across function calls, the same list is used.
# 5 is appended → list becomes [10, 5].

'''
Problem 2:
Number of ways to climb n stair in one step one or two stairs
'''

'''
Problem 3:
Convert ms into days hours min sec millisec
'''