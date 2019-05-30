class Node:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    def pushBack(self, value):
        current = Node()
        current.value = value
        current.next = None
        self.last.next = current
        self.last = current
    def popBack(self):
        return self.last.value.pop()
    def insert(self, index, value):
        if index > LinkedList.size:
            return
        else:
            node = self.first
            previous = None
            i = 0
            while i != index:
                previous = node
                node = node.next
            current = Node()
            current.value = value
            current.next = node
            previous.next = current
    def erase(self):
        
    def size(self):
        node = self.first
        i = 0
        while node is not None:
            node = node.next
            i += 1
        return i
