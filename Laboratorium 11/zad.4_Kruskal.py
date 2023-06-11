class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def algorytm_kruskala(wierzcholki, krawedzie):
    drzewo_rozpinajace = []
    zbior_wierzcholkow = UnionFind(wierzcholki)
    krawedzie = sorted(krawedzie, key=lambda x: x[0], reverse=True)
    kolejka = Queue()
    for krawedz in krawedzie:
        kolejka.enqueue(krawedz)

    while not kolejka.isEmpty():
        krawedz = kolejka.dequeue()
        koszt, v1, v2 = krawedz
        if zbior_wierzcholkow.find(v1) != zbior_wierzcholkow.find(v2):
            zbior_wierzcholkow.union(v1, v2)
            drzewo_rozpinajace.append(krawedz)

    return drzewo_rozpinajace
