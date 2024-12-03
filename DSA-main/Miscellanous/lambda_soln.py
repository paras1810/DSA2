
add  = lambda a, b:a+b
print(add(2, 3))


data = [(1, 'a'), (3, 'c'), (2, 'b')]
sorted_data = sorted(data, key=lambda x:x[1])
print(sorted_data)

numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = list(filter(lambda x:x%2==0, numbers))
print(filtered_numbers) 

numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x:x**2, numbers))
print(squared_numbers)

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y:x*y, numbers)
print(product)

larger = lambda x,y:x if x>y else y
print(larger(5, 3))

sum_three = lambda x,y,z:x+y+z
print(sum_three(1, 2, 3))


words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=lambda x:len(x), reverse=True)
print(sorted_words)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x,y:x+y, list1, list2))
print(result)

numbers = [1, 2, 3, 4, 5, 6, 12, 18]
filtered_numbers = list(filter(lambda x:x%2==0 and x%3==0, numbers))
print(filtered_numbers)

squared_dict = {x:(lambda x:x**2)(x) for x in range(5)}
print(squared_dict)

is_prime = lambda n:(all(n%i!=0) for i  in range(2,int(n**0.5)+1)) if n>1 else False
print(is_prime(7))  # Output: True
print(is_prime(10)) 

convert = lambda s:s.upper() if len(s)%2!=0 else s.lower()
print(convert("hello"))  # Output: hello (length is even)
print(convert("world"))


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(filter(lambda x:numbers.count(x)==1, numbers))
print(unique_numbers)