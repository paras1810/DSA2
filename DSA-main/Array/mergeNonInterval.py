
def findInterval(arr, n):
    arr.sort()
    stack = []
    for i in range(1,n):
        prevEnd = arr[i-1][1]
        currStart = arr[i][0]
        if prevEnd < currStart:
            stack.append([prevEnd, currStart])
    for i in stack:
        print(i)

if __name__ == '__main__':
    arr = [[1, 3], [2, 4],
           [3, 5], [7, 9]]
    n = len(arr)
    findInterval(arr, n)

