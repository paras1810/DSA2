# list1 = [1, 5, 5, 10]
# list2 = [1, 5, 10, 20]

def findcommon(list1, list2):
    dic = {}
    for i in range(len(list1)):
        if list1[i] not in dic:
            dic[list1[i]] = True
    for i in range(len(list2)):
        if list2[i] in dic.keys():
            print(list2[i])

if __name__ == "__main__":
    list1 = [1, 5, 5, 10]
    list2 = [1, 5, 10, 20]
    findcommon(list1, list2)