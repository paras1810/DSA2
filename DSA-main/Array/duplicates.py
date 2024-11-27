#Find if numbers are repeated in array using o(n) and constant space
def find_duplicates(arr):
    duplicates = []
    n = len(arr)
    for i in range(n):
        index = arr[i] % n
        arr[index] += n
    print(arr)
    #[1, 20, 3, 15, 3, 6, 27]
    for i in range(n):
        if arr[i] // n >= 2:
            duplicates.append(i)
    return duplicates

arr = [1, 6, 3, 1, 3, 6, 6]
ans = find_duplicates(arr)
for x in ans:
    print(x, end=" ")