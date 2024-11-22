
def maxProd(n):
    val = [0 for i in range(n+1)]
    for i in range(1, n+1):
        max_val = 0
        for j in range(1, i):
            max_val = max(max_val, (i-j)*j, j*val[i-j])
        val[i] = max_val
    for i in range(1, n+1):
        print(val[i])
    return val[n]

if __name__ == "__main__":
    print(maxProd(10))