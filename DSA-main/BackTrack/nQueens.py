
def is_safe(board,row,col):
    for i in range(row):
        if board[i] == col or board[i]-i==col-row or board[i]+i==col+row:
            return False
    return True
def solve(board,row,solutions):
    if row==n:
        solutions.append(['.'*i+'Q'+'.'*(n-i-1) for i in board])
        return
    for col in range(n):
        if is_safe(board,row,col):
            board[row]=col
            solve(board,row+1,solutions)
            board[row]=-1        

n=4
solutions=[]
board = [-1] * n
solve(board, 0, solutions)
print(solutions)      

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count=0
        cols=[False]*n
        d1=[False]*(2*n)
        d2=[False]*(2*n)
        self.backtrack(0,n,cols,d1,d2)
        return self.count

    def backtrack(self, row, n, cols, d1, d2):
        if row==n:
            self.count+=1
            return 
        for col in  range(n):
            id1=row-col+n
            id2=row+col
            if cols[col] or d1[id1] or d2[id2]:
                continue
            cols[col]=d1[id1]=d2[id2]=True
            self.backtrack(row+1,n,cols,d1,d2)
            cols[col]=d1[id1]=d2[id2]=False
        