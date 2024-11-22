
def fib(n):
    p, q = 0, 1
    while p<n:
        yield p
        p, q = q, p+q
x = fib(10)
print(x.__next__())
print(x.__next__())

for i in fib(10):
    print(i)


class ArrayList():
    def __init__(self, number_list) -> None:
        self.numbers = number_list

    def __iter__(self):
        self.pos = 0
        return self
    
    def __next__(self):
        if self.pos<len(self.numbers):
            self.pos += 1
            return self.numbers[self.pos-1]
        else:
            raise StopIteration
        
array_obj = ArrayList([1, 2, 3])
it = iter(array_obj)
print(next(it))
print(next(it))

def gen():
    for i in range(0, 5):
        yield(i)
x = gen()
print(x.__next__())

x = [1, 2, 3, 4, 5]
it = iter(x)
print(next(it))