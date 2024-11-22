N = 8
MATRIX = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]
def knows(a, b):
    return MATRIX[a][b]

def findCeleb(n):
    s = []
    for i in range(n):
        s.append(i)
    while len(s) > 1:
        A = s.pop()
        B = s.pop()
        if knows(A, B):
            s.append(B)
        else:
            s.append(A)
    if len(s) == 0:
        return -1
    C = s.pop()
    if knows(C, B):
        C = B
    if knows(C, A):
        C = A
    for i in range(n):
        if ((i != C) and (knows(C, i) or not(knows(i,C)))):
            return -1
    return C

if __name__ == '__main__':
    n = 4
    id = findCeleb(n)
    if id == -1:
        print("No Celebrity")
    else:
        print("Celebrity Id", id)