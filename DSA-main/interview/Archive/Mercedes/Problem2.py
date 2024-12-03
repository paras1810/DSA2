input = [1, 4, 6, 0, 5, 8, 0, 45, 46, 0, 0, 4, 5, 6, 0, 6]
output = [[1, 4, 6], [5, 8], [45, 46], [4, 5, 6], [6]]

ans = []
res = []
for i in range(len(input)):
    if input[i] == 0 and len(res)>0:
        ans.append(res)
        res = []
    else:
        res.append(input[i])
print(ans)






