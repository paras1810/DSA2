
def recRev(a, b):
    if len(a) > 1:
        temp = b + a[-1]
        b = recRev(a[0:len(a)-1], temp)
    elif len(a) ==1:
        b = b + a[0]
    return b


if __name__ == '__main__':
    a = "Para"
    b = ""
    result = recRev(a,b)
    print(result)