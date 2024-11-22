
def getMissing(arr, N):
    x1 = arr[0]
    x2 = 1
    for i in range(1, N):
        x1 = x1 ^ arr[i]
    for i in range(1, N):
        x2 = x2 ^ i
    return x1 ^ x2

if __name__ == "__main__":
    arr = [1, 2, 3, 5]
    N = len(arr)
    print(getMissing(arr, N))