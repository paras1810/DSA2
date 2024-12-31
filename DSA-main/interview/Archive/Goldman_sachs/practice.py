
def getMinTransactions(n, debt):
    arr = [0 for i in range(n)]
    for i in range(len(debt)):
        arr[debt[i][0]] = arr[debt[i][0]] + debt[i][2] 
        arr[debt[i][1]] = arr[debt[i][1]] - debt[i][2]
    arr.sort()
    i = 0
    j=n-1
    count=0
    while(i<j):
        if arr[i]==0: i=i+1
        elif arr[j]==0: j=j-1
        elif -1*arr[i]<arr[j]:
            arr[j] = arr[j]+arr[i]
            i=i+1
            count=count+1
        elif -1*arr[i]>arr[j]:
            arr[i] = arr[i]+arr[j]
            j=j-1
            count=count+1
        else:
            i=i+1
            j=j-1
            count=count+1

    #print(arr)
    return count



if __name__ == "__main__":
    n  = 4
    debt = [[1,2,15], [3,2,14], [0,3,10], [3,1,20]]
    count = getMinTransactions(n, debt)
    print(count)
    debt = [[0,0,0]]
    count = getMinTransactions(n, debt)
    print(count)
