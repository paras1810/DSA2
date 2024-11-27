#Product of all number except itself in arr[] of size n
def productArray(arr, n):
    if n == 1:
        print(0)
        return
    i, temp = 1, 1
    product = [1 for i in range(n)]
    for i in range(n):
        product[i] = temp
        temp = temp * arr[i]
    temp = 1
    for i in range(n-1, -1, -1):
        product[i] *= temp
        temp *= arr[i]

    for i in range(n):
        print(product[i], end=' ')
    return

arr = [10, 3, 5, 6, 2]
n = len(arr)
productArray(arr, n)
