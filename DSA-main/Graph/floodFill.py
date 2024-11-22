def isValid(screen, m, n, x, y, prevC, newC):
    if x<0 or x>=m or y<0 or y>=n or screen[x][y]!=prevC or screen[x][y]==newC:
        return False
    return True

def floodFill(screen, m, n, x, y, prevC, newC):
    queue = []
    queue.append([x, y])
    screen[x][y] = newC
    while queue:
        currPixel = queue.pop()
        posX = currPixel[0]
        posY = currPixel[1]
        rowNbr = [1, -1, 0, 0]
        colNbr = [0, 0, 1, -1]
        for k in range(4):
            if isValid(screen, m, n, posX+rowNbr[k], posY+colNbr[k], prevC, newC):
                screen[posX+rowNbr[k]][posY+colNbr[k]] = newC
                queue.append([posX+rowNbr[k], posY+colNbr[k]])


if __name__ == "__main__":
    screen = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 2, 2, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 2, 2, 0],
        [1, 1, 1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 2, 2, 1],
    ]
    m = len(screen)
    n = len(screen[0])
    x = 4
    y = 4
    prevC = screen[x][y]
    newC = 3
    floodFill(screen, m, n, x, y, prevC, newC)
    for i in range(m):
        for j in range(n):
            print(screen[i][j], end=" ")
        print()
