#Trees - Ex4
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = Node

    def find(self, node, key):
        if node is None:
            return False
        elif node.data == key:
            return True
        elif node.data < key:
            return BinarySearchTree.find(node.right, key)
        elif node.data > key:
            return BinarySearchTree.find(node.left, key)


    def insert(self, node, key):
        if node is None:
            node = key
        else:
            if node.data < key.data:
                if node.right is None:
                    node.right = key
                else:
                    BinarySearchTree.insert(node.right, key)
            else:
                if node.left is None:
                    node.left = key
                else:
                    BinarySearchTree.insert(node.left, key)



#Trees - Ex5

class ListPhoneBook:
    def __init__(self):
        self.members = []
        self.numbers = []

    def size(self):
        return len(self.members)

    def insert(self, name, phoneNumber):
        self.members.append(name)
        self.numbers.append(phoneNumber)

    def find(self, name):
        numIndex = self.members.index(name)
        return self.numbers[numIndex]

class BinarySearchTreePhoneBook:
    def __init__(self):
        self.phoneBook = BinarySearchTree

   
