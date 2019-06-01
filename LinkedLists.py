class Node:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.dummyhead = None
        self.dummytail = None
        self.pre = Node()
        self.pre.value = None
        self.pre.next = self.dummytail

    def pushBack(self, value):
        current = Node()
        current.value = value
        current.next = self.dummytail
        if self.pre is None:
            self.pre = current
            self.dummyhead.next = self.pre
        else:
            self.pre.next = current
            self.pre = current

    def popBack(self):
        node = self.dummyhead.next
        value = self.pre.value
        while node != self.pre:
            node = node.next
        node.next = self.dummytail
        self.pre = node
        return value

    def insert(self, index, value):
        if index >= LinkedList.size:
            return
        else:
            node = self.dummyhead.next
            previous = None
            i = 0
            while i != index and node is not self.dummytail:
                previous = node
                node = node.next
                i += 1
            current = Node()
            current.value = value
            current.next = node
            previous.next = current

    def erase(self, index):
        node = self.dummyhead.next
        previous = None
        i = 0
        while i != index and node is not self.dummytail:
            previous = node
            node = node.next
            i += 1
        previous.next = node.next

    def elementAt(self, index):
        node = self.dummyhead.ext
        i = 0
        while i != index and node is not self.dummytail:
            node = node.next
            i += 1
        return node.value
    
    def size(self):
        node = self.dummyhead.next
        i = 0
        while node is not None:
            node = node.next
            i += 1
        return i

