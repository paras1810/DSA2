def mergeIntervals(arr):
    arr.sort()
    stack = []
    stack.append(arr[0])
    for i in arr[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    for i in range(len(stack)):
        print(stack[i])


arr = [[6, 8], [1, 9], [2, 4], [4, 7], [11, 12]]
mergeIntervals(arr)