def func():
    sum1 = lambda x,y: x+y
    x = 10
    y = 20
    print(sum1(x,y))

    lst = [5, 6, 3, 2]
    tot = (lambda x: sum(x,0))(lst)
    print(tot)


if __name__ == "__main__":
    func()