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

def algorytm_prima(wierzcholki, krawedzie):
    minimalne_drzewo_rozpinajace = []
    uzyte_wierzcholki = {wierzcholki[0]}
    mozliwe_krawedzie = Queue()

    for krawedz in krawedzie[wierzcholki[0]]:
        mozliwe_krawedzie.enqueue(krawedz)

    while not mozliwe_krawedzie.isEmpty():
        najmniejsza_krawedz = None
        for i in range(mozliwe_krawedzie.size()):
            krawedz = mozliwe_krawedzie.dequeue()
            if najmniejsza_krawedz is None or krawedz[0] < najmniejsza_krawedz[0]:
                if krawedz[2] not in uzyte_wierzcholki:
                    najmniejsza_krawedz = krawedz
            mozliwe_krawedzie.enqueue(krawedz)

        if najmniejsza_krawedz is not None:
            mozliwe_krawedzie.items.remove(najmniejsza_krawedz)
            uzyte_wierzcholki.add(najmniejsza_krawedz[2])
            minimalne_drzewo_rozpinajace.append(najmniejsza_krawedz)

            for krawedz in krawedzie[najmniejsza_krawedz[2]]:
                if krawedz[2] not in uzyte_wierzcholki:
                    mozliwe_krawedzie.enqueue(krawedz)
    return minimalne_drzewo_rozpinajace
