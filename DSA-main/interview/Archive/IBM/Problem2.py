# input = 3
# hat happy speaker-->a
# haat haapy speaaker-->aa
# hai good letters-->""
#
# hart raay-->ar

def findcommon(a, b):
    s1 = []
    s2 = []
    s3 = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in range(26):
        s1.append(0)
        s2.append(0)
    for i in range(len(a)):
        s1[ord(a[i])-ord('a')] = s1[ord(a[i])-ord('a')]+1
    for i in range(len(b)):
        s2[ord(b[i]) - ord('a')] = s2[ord(b[i]) - ord('a')] + 1
    for i in range(26):
        c = min(s1[i], s2[i])
        for j in range(c):
            res+=s3[i]
    return res


if __name__ == "__main__":
    n = 3
    list1 = ["haapt", "haapppy", "speaakper"]

    while len(list1) > 1:
        a = list1.pop()
        b = list1.pop()
        c = findcommon(a, b)
        list1.append(c)
    print(list1[0])


