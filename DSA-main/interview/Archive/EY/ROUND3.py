# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

# string1= "ParaP"
# if string1==string1[::-1]:
#     print(f"{string1} is pallindrome")
# else:
#     print(f"{string1} is not pallindrome")

# def compound(func):
#     def wrapper(p, r, t):
#         print("printing compund interest")
#         ci=(p*(1 + r/100)**t) -p
#         print(ci)
#         return func(p,r,t)
#     return wrapper
    
# @compound
# def simple_interest(p, r, t):
#     return (p*r*t)//100
# print(simple_interest(100, 10, 10))


    
def print_nums():
    yield(1)
    yield(2)

for num in print_nums():
    print(num)

    

