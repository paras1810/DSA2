
def func(x):
    #global x
    print(x)
    return x

if __name__ == "__main__":
    print('Hello')
    x=(10)
    y=func(x)
    print(x,y)