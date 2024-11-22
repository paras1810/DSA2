def maxArea(a):
    l = 0
    r = len(a)-1
    area = 0
    while l < r:
        area = max(area, min(a[l], a[r]) * (r-l))
        if a[l] <= a[r]:
            l += 1
        else:
            r -= 1
    return area
a = [1, 5, 4, 3]
b = [3, 1, 2, 4, 5]

print(maxArea(a))
print(maxArea(b))