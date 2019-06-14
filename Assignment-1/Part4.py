class Node:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.dummyhead = Node()
        self.dummytail = Node()
        self.pre = Node()
        self.dummyhead.value = None
        self.dummytail = None
        self.pre = Node()
        self.pre.value = None
        self.pre.next = self.dummytail
        self.dummyhead.next = self.pre

    def __str__(self):
        node = self.dummyhead.next
        string = ""
        while node.next != self.dummytail:
            string = string + str(node.value) + " "
            node = node.next
        string = string + str(node.value)
        return string

    def pushBack(self, value):
        current = Node()
        current.value = value
        current.next = self.dummytail
        if self.pre.value is None:
            self.pre = current
            self.dummyhead.next = self.pre
        else:
            self.pre.next = current
            self.pre = current

    def popBack(self):
        node = self.dummyhead.next
        value = self.pre.value
        while node.next != self.pre:
            node = node.next
        node.next = self.dummytail
        self.pre.value = node.value
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
        if self.pre.value is not None:
            while i != index and node is not self.dummytail:
                previous = node
                node = node.next
                i += 1
            previous.next = node.next
        else:
            return

    def elementAt(self, index):
        node = self.dummyhead.next
        i = 0
        if self.pre.value is not None:
            while i != index and node is not self.dummytail:
                node = node.next
                i += 1
            return node.value
        else:
            return

    def size(self):
        node = self.dummyhead.next
        i = 0
        if self.pre.value is not None:
            while node is not self.dummytail:
                node = node.next
                i += 1
            return i
        else:
            return 0

def testPushBackAddsOneNode(linkedlist):
    a = linkedlist.size()
    print("Before push: ", a)
    print("Pushed 8 ")
    linkedlist.pushBack(8)
    b = linkedlist.size()
    print("After push: ", b)

def testPopBackRemovesCorrectNode(linkedlist):
    print("Size before pop: ",linkedlist.size())
    print("Popped: ", linkedlist.popBack())
    print("Size after pop: ", linkedlist.size())

def testEraseRemovesCorrectNode(linkedlist):
    print(linkedlist)
    linkedlist.erase(2)
    print("Removing 3rd element")
    print(linkedlist)

def testEraseDoesNothingIfNoNode(linkedlist):
    linkedlist.erase(2)
    print("Removing 3rd element from an empty list")
    print(linkedlist)

def testElementAtReturnNode(linkedlist):
    print(linkedlist)
    print("Element at index 3: ", linkedlist.elementAt(3))

def testElementAtReturnNoNodeIfIndexDoesNotExist(linkedlist):
    print(linkedlist)
    print("Element at index 3 in an empty list: ", linkedlist.elementAt(3))

def testSizeReturnsCorrectSize(linkedlist):
    print(linkedlist)
    print("Size of: ", linkedlist.size())



def hasCycle(linkedlist):
    slow = linkedlist.dummyhead.next
    fast = linkedlist.dummyhead.next
    while fast.next is not linkedlist.dummytail and fast.next is not linkedlist.dummytail:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        else: return False

def isPalindrome(linkedlist):
    reverse = LinkedList()
    i = linkedlist.size() - 1
    while i != 0 :
        value = linkedlist.elementAt(i)
        reverse.pushBack(value)
    a = linkedlist.dummyhead.next
    b = reverse.dummyhead.next
    while a is not linkedlist.dummytail and b is not reverse.dummytail:
        if a == b:
            a = a.next
            b = b.next
        else:
            return False
    return True



linkedlist = LinkedList()
linkedlist.pushBack(3)
linkedlist.pushBack(6)
linkedlist.pushBack(9)
linkedlist.pushBack(12)
linkedlist.pushBack(15)
testPushBackAddsOneNode(linkedlist)
testPopBackRemovesCorrectNode(linkedlist)
testEraseRemovesCorrectNode(linkedlist)
emptylinkedlist = LinkedList()
testEraseDoesNothingIfNoNode(emptylinkedlist)
testElementAtReturnNode(linkedlist)
testElementAtReturnNoNodeIfIndexDoesNotExist(emptylinkedlist)
testSizeReturnsCorrectSize(linkedlist)
testSizeReturnsCorrectSize(emptylinkedlist)
