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



