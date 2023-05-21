class Node:
    def __init__(self, inidata):
        self.data = inidata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

temp = Node(93)
print(temp.getData())
print(temp.getNext())


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def add_sorted(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() >= item:
                found = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def merge_sorted(self, other_list):
        merged_list = UnorderedList()
        current_self = self.head
        current_other = other_list.head

        while current_self is not None and current_other is not None:
            if current_self.getData() < current_other.getData():
                merged_list.add_sorted(current_self.getData())
                current_self = current_self.getNext()
            else:
                merged_list.add_sorted(current_other.getData())
                current_other = current_other.getNext()


        while current_self is not None:
            merged_list.add_sorted(current_self.getData())
            current_self = current_self.getNext()


        while current_other is not None:
            merged_list.add_sorted(current_other.getData())
            current_other = current_other.getNext()

        return merged_list

myList = UnorderedList()
myList.add(12)
myList.add(122)
myList.add(43)
myList.add(4)
myList.add(1)
myList.add(-32)
myList.add(345)
myList.add(-43)

print(myList.size())
print(myList.search(-32))
print(myList.search(-1234143))





