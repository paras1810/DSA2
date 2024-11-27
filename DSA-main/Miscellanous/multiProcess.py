import multiprocessing
import os


class list:
    def __init__(self, mylist):
        print("I will be called")
        self.data = mylist

def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n * n)

#If we not use __main__ in Python on Windows OS it will went in infinite loop
if __name__ == "__main__":
    # input list
    mylist = [1, 2, 3, 4, 5]
    li = list(mylist)

    # creating a pool object
    p = multiprocessing.Pool()

    # map list to target function
    result = p.map(square, li.data)

    print(result)


