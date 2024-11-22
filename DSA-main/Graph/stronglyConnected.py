class GFG:
    def dfs(self, curr, des, adj, vis):
        if curr == des:
            return True
        vis[curr] = 1
        for x in adj[curr]:
            if not vis[x]:
                if self.dfs(x, des, adj, vis):
                    return True
        return False

    def isPath(self, src, des, adj):
        vis = [0] * (len(adj)+1)
        return self.dfs(src, des, adj, vis)

    def findSCC(self, n, a):
        ans = []
        is_scc = [0] * (n+1)
        adj = [[] for _ in range(n+1)]
        for i in range(len(a)):
            adj[a[i][0]].append(a[i][1])

        for i in range(1, (n+1)):
            if not is_scc[i]:
                scc = [i]
                for j in range(i+1, n+1):
                    if not is_scc[j] and self.isPath(i, j , adj) and self.isPath(j, i, adj):
                        is_scc[j] = 1
                        scc.append(j)
                ans.append(scc)
        return ans

if __name__ == "__main__":
    obj = GFG()
    V = 5
    edges = [
        [1,3], [1,4], [2,1], [3,2], [4,5]
    ]
    ans = obj.findSCC(V, edges)
    for x in ans:
        for y in x:
            print(y, end=" ")
        print()