import heapq
def print_N_mostFrequentNumber(arr, N, K):
    mp = dict()
    for i in range(N):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        else:
            mp[arr[i]] += 1

    heap = [(value, key) for key, value in mp.items()]
    large = heapq.nlargest(K, heap)
    for i in range(K):
        print(large[i][1], end=" ")

if __name__ == "__main__":

    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    N = len(arr)
    K = 2

    # Function call
    print_N_mostFrequentNumber(arr, N, K)