def findXor(set_r, n):
    if n == 1:
        return set_r[0]
    else:
        return 0

if __name__ == "__main__":
    set_r = [1, 2, 3, 4]
    n = len(set_r)
    print(findXor(set_r, n))
