
def checkMirror(n, e, a, b):
    s = []
    q = []
    for i in range(n+1):
        s.append([])
        q.append([])
    for i in range(0, 2*e, 2):
        s[a[i]].append(a[i+1])
        q[b[i]].append(b[i+1])
    for i in range(1, n+1):
        while len(s[i])>0 and len(q[i])>0:
            c=s[i][-1]
            s[i].pop()
            d=q[i][0]
            q[i].pop(0)
            if c!=d:
                return 0
    return 1





if __name__ == "__main__":
    n = 3
    e = 2
    A = [1, 2, 1, 3]
    B = [1, 3, 1, 2]
    if checkMirror(n, e, A, B) == 1:
        print("Yes")
    else:
        print("No")