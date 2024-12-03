
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
        