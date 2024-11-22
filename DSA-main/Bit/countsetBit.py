
def countSetBits(n):
    if n==0:
        return 0
    else:
        return 1 + countSetBits(n&(n-1))


n = 9
print(countSetBits(n))