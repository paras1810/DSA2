def modifyMatrix(mat):
       r = len(mat)
       c = len(mat[0])
       row = [0] * r
       col = [0] * c
       for i in range(0, r):
              for j in range(0, c):
                     if mat[i][j] == 1:
                            row[i] = 1
                            col[j] = 1
       for i in range(0,r):
              for j in range(0,c):
                     if row[i]==1 or col[j]==1:
                            mat[i][j] = 1

       for i in range(0,r):
              for j in range(0,c):
                     print(mat[i][j], end=" ")
              print()



mat = [[1, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 0, 0]]
modifyMatrix(mat)
#print(mat)