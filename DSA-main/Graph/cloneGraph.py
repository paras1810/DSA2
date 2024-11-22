from collections import deque
class GraphNode:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

def cloneGraph(src: GraphNode)->GraphNode:
    m = {}
    q = deque()
    q.append(src)
    node = None
    node = GraphNode()
    node.val = src.val
    m[src] = node
    while q:
        u = q.popleft()
        v = u.neighbors
        for neighbor in v:
            if neighbor not in m:
                node = GraphNode()
                node.val = neighbor.val
                m[neighbor] = node
                q.append(neighbor)
            m[u].neighbors.append(m[neighbor])
    return m[src]





def buildGraph() -> GraphNode:
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node3, node1]
    return node1

def bfs(src: GraphNode):
    visit = {}
    q = deque()
    q.append(src)
    visit[src] = True
    while q:
        u = q.popleft()
        print(f"Value of Node {u.val}")
        print(f"Address of Node {u}")
        v = u.neighbors
        for neighbor in v:
            if neighbor not in visit:
                visit[neighbor] = True
                q.append(neighbor)

if __name__ == "__main__":
    src = buildGraph()
    print("BFS Traversal before cloning")
    bfs(src)
    clone = cloneGraph(src)
    print("\nBFS Traversal after cloning")
    bfs(clone)