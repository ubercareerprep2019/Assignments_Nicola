#Graphs - Ex1

class GraphNode:
    def __init__(self, data):
        self.data = data

class GraphWithAdjacencyList:
    def __init__(self):
        self.adjNodes = {}
        self.Nodes = {}

    def addNode(self, key):
        graphKey = GraphNode(key)
        self.Nodes[key] = graphKey
        self.adjNodes[graphKey] = []

    def removeNode(self, key):
        if key in self.Nodes:
            graphKey = self.Nodes[key]
            self.Nodes.pop(key)
            self.adjNodes.pop(graphKey)

    def addEdge(self, node1, node2):
        if node1 in self.Nodes and node2 in self.Nodes:
            graphNode1 = self.Nodes[node1]
            graphNode2 = self.Nodes[node2]

            self.adjNodes[graphNode1].append(graphNode2)
            self.adjNodes[graphNode2].append(graphNode1)

    def removeEdge(self, node1, node2):
        if node1 in self.Nodes and node2 in self.Nodes:
            graphNode1 = self.Nodes[node1]
            graphNode2 = self.Nodes[node2]

            self.adjNodes[graphNode1].remove(graphNode2)
            self.adjNodes[graphNode2].remove(graphNode1)


    def getAdjNodes(self, key):
        graphKey = self.Nodes[key]
        return self.adjNodes[graphKey]
    
    
    #Graphs - Ex2

    def DFS(self, key):
        if key not in self.Nodes:
            self.dfsOutput.append(key)
            for x in self.Nodes[key]:
                GraphWithAdjacencyList.DFS(x)
        return self.dfsOutput

    #Graphs - Ex3
    
    
    def BFS(self, key):
        queue = [key]
        self.bfsOutput = [key]
        while queue:
            node = queue.pop(0)
            self.bfsOutput.append(node)

            for n in self.adjNodes[node]:
                if n not in self.bfsOutput:
                    queue.append(n)
                    self.bfsOutput.append(n)
        return self.bfsOutput





