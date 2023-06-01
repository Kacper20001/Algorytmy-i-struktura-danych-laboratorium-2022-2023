class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def BFS(G,s):
    n=len(G)
    visited = [False] * n
    d = [-1] * n
    p = [-1] * n

    visited[s] = True
    d[s] = 0
    Q = Queue()
    Q.enqueue(s)

    while not Q.isEmpty():
        u=Q.dequeue()
        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                p[v] = u
                Q.enqueue(v)

    return visited, d, p

#graf
G = [
    [0,1,0,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,1],
    [1,0,0,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,1]
]
startV = 3

visited, distance, parent = BFS(G, startV)
for v in range(len(G)):
    print(f"Wierzchołek {v}: visited = {visited[v]}, distance = {distance[v]}, parent = {parent[v]}")
