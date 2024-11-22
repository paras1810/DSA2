class pair:
    def __init__(self, f, s):
        self.f = f
        self.s = s

def makeGraph(numTasks, prerequisites):
    graph = []
    for i in range(numTasks):
        graph.append([])
    for pre in prerequisites:
        graph[pre.s].append(pre.f)
    return graph

def dfs_cycle(graph, node, onPath, visited):
    if visited[node]:
        return False
    onPath[node] = visited[node] = True
    for neigh in graph[node]:
        if (onPath[neigh] or dfs_cycle(graph, neigh, onPath, visited)):
            return True
    return False

def canFinish(numTasks, prerequisites):
    graph = makeGraph(numTasks,prerequisites)
    onPath = [False]*numTasks
    visited = [False]*numTasks
    for i in range(numTasks):
        if (not visited[i] and dfs_cycle(graph, i, onPath, visited)):
            return False
    return True


if __name__ == "__main__":
    numTasks = 4
    prerequisites = []

    prerequisites.append(pair(1, 0))
    prerequisites.append(pair(2, 1))
    prerequisites.append(pair(3, 2))

    if canFinish(numTasks, prerequisites):
        print("Possible to finish all tasks")
    else:
        print("Impossible to finish all tasks")
