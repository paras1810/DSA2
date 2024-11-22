from heapq import heappush, heappop, heapify
def largeTripleProd(arr, n):
    s = []
    for i in range(n):
        heappush(s, -arr[i])
        if i<2:
            print("-1", end=" ")
        else:
            a, b, c = heappop(s), heappop(s), heappop(s)
            print(-1*a*b*c, end=" ")
            heappush(s, a)
            heappush(s, b)
            heappush(s, c)



if __name__ == '__main__':

    arr = [ 1, 2, 3, 4, 5 ]
    n = len(arr)

    largeTripleProd(arr, n)