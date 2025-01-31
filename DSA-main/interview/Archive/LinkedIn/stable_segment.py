# Organization there are n servers each with capacity of capacity[i]. A contiguous subsegment
# [l,r] of server is said to be stable if capacity[i] = capacity[r] = sum[l+1,r-1]. In
# other words, capacity of server at endpoint of segment should be equal to capacity of interior servers.
# Find the number of stable segments of length 3 and more.
# For example n=5 and capacity=[9,3,3,3,9] there are two stable subsegmets [3,3,3] and [9,3,3,3,9]. We need to return count 2 
# Help in writing python code for this.

def count_stable_segments(capacity):
    n = len(capacity)
    stable_count = 0
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + capacity[i - 1]
    index_map = {}
    unique_nums = set()
    for i in range(n):
        if capacity[i] not in index_map:
            index_map[capacity[i]] = []
            unique_nums.add(capacity[i])
        index_map[capacity[i]].append(i)
    #print(unique_nums, index_map)
    for value in unique_nums:
        next_index = 0
        while next_index<len(index_map[value]):
            l=index_map[value][next_index]
            next_next_index = next_index+1
            while next_next_index < len(index_map[value]):
                r = index_map[value][next_next_index]
                if r > l + 1:
                    interior_sum = prefix[r] - prefix[l + 1]
                    if interior_sum == capacity[l]:
                        stable_count += 1
                if r>l+2:
                    break
                next_next_index += 1
            next_index=next_index+1
    return stable_count
# Test the function
capacity = [9, 3, 3, 3,3,3, 3,9]
print(count_stable_segments(capacity))  # Output should be 2
capacity = [6,1,2,3,6]
print(count_stable_segments(capacity))
capacity = [9,3,1,2,3,9,14]
print(count_stable_segments(capacity))
