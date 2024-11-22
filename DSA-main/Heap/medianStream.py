from heapq import heappush, heappop, heapify
import math
def streamMed(arr, n):
    g = []
    s = []
    for i in range(len(arr)):
        heappush(s, -arr[i])
        heappush(g, -heappop(s))
        if len(g) > len(s):
            heappush(s, -heappop(g))
        if len(g) != len(s):
            print(-s[0])
        else:
            print((g[0] - s[0])/2)
    pass

if __name__ == '__main__':
    A = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    N = len(A)

    # Function call
    streamMed(A, N)