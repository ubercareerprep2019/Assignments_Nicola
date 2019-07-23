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

class Employee:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.directReports = []

    def __str__(self):
        string = "Name: " + self.name + ", Title: " + self.title
        return string


class OrganizationStructure:
    def __init__(self, name, title):
        self.ceo = Employee(name, title)
        self.employees = self.ceo.directReports

    def PrintByLevel(self):
        queue = []
        queue.append(self.ceo)
        while len(queue) > 0:
            print(queue[0])
            boss = queue.pop(0)
            if boss.directReports is not None:
                queue.append(boss.directReports)

    # Trees - Ex3
    def printNumLevels(self, leaf):
        if leaf is None:
            return 0
        maxdepth = 0
        for  i in leaf.directReports:
            if maxdepth < i.printNumLevels:
                maxdepth = i.printNumLevels
        return maxdepth



company = OrganizationStructure("A", "CEO")
cfo = Employee("B", "CFO")
cto = Employee("C", "CTO")
managerD = Employee("D", "Manager")
managerE = Employee("E", "Manager")
engineerF = Employee("F", "Engineer")
engineerG = Employee("G", "Engineer")
engineerH = Employee("H", "Engineer")
director = Employee("I", "Director")
salesRep = Employee("J", "Sales Representative")
salesIntern = Employee("K", "Sales Intern")

company.ceo.directReports = [cfo, cto]
cto.directReports = [managerD, managerE]
managerD.directReports = [engineerF, engineerG, engineerH]
cfo.directReports = [director]
director.directReports = [salesRep]
salesRep.directReports = [salesIntern]

company.PrintByLevel()


