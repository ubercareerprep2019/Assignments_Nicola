class TreeNode:
    def __init__(self, data, left = None, right = None):
        if left:
            self.left = TreeNode(left)
        else:
            self.left = left
        if right:
            self.right = TreeNode(right)
        else:
            self.right = right
        self.data = data


    # Trees - Ex1
    def PrintTree(self):
        print(self.data)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(17, 6, 3)
root.PrintTree()




#Trees - Ex2
class OrganizationStructure:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __str__(self):
        string = "Name: " + self.name + " Title: " + self.title
        return string



root2 = TreeNode(OrganizationStructure("A", "CEO"))
root2.left = TreeNode(OrganizationStructure("B", "CFO"))
root2.right = TreeNode(OrganizationStructure("C", "CTO"))
root2.left.left = TreeNode(OrganizationStructure("I", "Director"))
root2.left.left.left = TreeNode(OrganizationStructure("J", "Sales Represenatative"))
root2.left.left.left.left = TreeNode(OrganizationStructure("K", "Sales Intern"))
root2.right.left = TreeNode(OrganizationStructure("D", "Manager"))
root2.right.right = TreeNode(OrganizationStructure("E", "Manager"))
root2.right.left.left = TreeNode(OrganizationStructure("F", "Engineer"))
root2.right.left.right = TreeNode(OrganizationStructure("G", "Engineer"))



root2.PrintTree()

