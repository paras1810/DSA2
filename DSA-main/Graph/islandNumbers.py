class Graph:
    def __init__(self, row, col, graph):
        self.row = row
        self.col = col
        self.graph = graph

    def dfs(self, i, j):
        if i<0 or j<0 or i>=self.row or j>=self.col or self.graph[i][j]!=1:
            return
        self.graph[i][j] = -1
        self.dfs(i-1, j-1)
        self.dfs(i-1, j)
        self.dfs(i-1, j+1)
        self.dfs(i, j-1)
        self.dfs(i, j+1)
        self.dfs(i+1, j-1)
        self.dfs(i+1, j)
        self.dfs(i+1, j+1)



    def countIslands(self):
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.graph[i][j] == 1:
                    self.dfs(i, j)
                    count += 1
        return count

if __name__ == "__main__":
    graph = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]

    row = len(graph)
    col = len(graph[0])

    g = Graph(row, col, graph)

    print("Number of islands is:", g.countIslands())