from collections import defaultdict
def printAnaTog(arr):
    groupWord = defaultdict(list)
    for word in arr:
        groupWord["".join(sorted(word))].append(word)

    for group in groupWord.values():
        print(" ".join(group))



if __name__ == '__main__':
    arr = ["cat", "dog", "tac", "god", "act"]
    printAnaTog(arr)