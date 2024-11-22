from heapq import heappush, heappop, heapify
def minCost(arr, n):
    heapify(arr)
    res = 0
    while len(arr) > 1:
        first = heappop(arr)
        second = heappop(arr)
        res += first + second
        heappush(arr, first+second)

    return res

if __name__ == '__main__':

    lengths = [4, 3, 2, 6]
    size = len(lengths)

    print("Total cost for connecting ropes is " +
          str(minCost(lengths, size)))