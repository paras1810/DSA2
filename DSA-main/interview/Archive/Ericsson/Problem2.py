list1=[11,55,2,2,56,55,77,65,77,66]
# No pre-defined funtions
# Repeated number as one entity
def find_nth(n):
    m=len(list1)
    list2=[]
    for i in range(0,m):
        small=list1[i]
        for j in range(0,m):
            if small>=list1[j]:
                small=list1[j]
        list2.append(small)
        for j in range(0,m):
            if list1[j]==small:
                list1[j]=10000
    print(list2)
    return list2[n-1]

print(find_nth(3))