class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def find(node, key):
    if node is None or node.data == key:
        return node
    if node.data < key:
        return find(node.right, key)
    if node.data > key:
        return find(node.left, key)


def insert(node, keyNode):
    if node is None:
        node = keyNode
    else:
        if node.data < keyNode.data:
            if node.right is None:
                node.right = keyNode
            else:
                insert(node.right, keyNode)
        else:
            if node.left is None:
                node.left = keyNode
            else:
                insert(node.left, keyNode)
