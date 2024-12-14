from collections import deque
import heapq

def min_cost_to_reach(x, a, b):
    if x==0:
        return 0
    pq = [(a,1)]
    visited = set([1])
    while pq:
        current_cost, current_num = heapq.heappop(pq)
        if current_num == x:
            return current_cost
        if current_num+1 not in visited:
            visited.add(current_num+1)
            heapq.heappush(pq, (current_cost+a, current_num+1))
        if current_num-1>0 and current_num-1 not in visited:
            visited.add(current_num-1)
            heapq.heappush(pq, (current_cost+a, current_num-1))
        if current_num*2 not in visited:
            visited.add(current_num*2)
            heapq.heappush(pq, (current_cost+b, current_num*2))
        print(pq)

    return -1


x=10
a=2
b=20
print(min_cost_to_reach(x,a,b))