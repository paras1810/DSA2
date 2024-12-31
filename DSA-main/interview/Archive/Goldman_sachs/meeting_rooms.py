import heapq

def minMeetingRooms(start, end):
    if not start or not end or len(start) != len(end):
        return 0
    # start.sort()
    # end.sort()
    heap = []
    heapq.heappush(heap, end[0])
    for i in range(1, len(start)):
        if start[i] > heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, end[i])
    return len(heap)

# Example usage:
start = [1, 2, 3]
end = [3, 3, 5]
print(minMeetingRooms(start, end))  # Output: 2
