def printPairs(arr, arr_size, sum):
    hashmap = {}
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if temp in hashmap:
            print("Yes")
            return
        hashmap[arr[i]] = i
    print("No")


A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)