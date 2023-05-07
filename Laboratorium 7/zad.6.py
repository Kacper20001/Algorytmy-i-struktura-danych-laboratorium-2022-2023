from QueueExample import Queue

def game(names, n):
    s = Queue()
    for i in names:
        s.enqueue(i)

    while s.size() > 1:
        for j in range(n):
            s.enqueue(s.dequeue())
        s.dequeue()

    return s.dequeue()


print(game(["Kacper","Marcin","Przemek","Kasia","Basia","Monika","Seweryn"],9))