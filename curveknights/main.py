#solution of https://open.kattis.com/problems/curveknights
from collections import defaultdict

#class def
class Edge:
    def __init__(self, end, travelCost):
        self.end = end
        self.travelCost = travelCost

class Node:
    def __init__(self, value):
        self.edges = []
        self.value = value
        self.indegree = 0
    def addEdge(self, end, travelCost):
        self.edges.append(Edge(end, travelCost))
    def addValue(self, value):
        self.value += value

#import file
import fileinput

inputMessage = ""

for line in fileinput.input():
    inputMessage+=line

inputs = inputMessage.split()

amountProducts = int(inputs[0])
amountsRecipes = int(inputs[1])
start = 2
result = []
graph = defaultdict(Node)
for i in range(amountProducts):
    result.append(0)
    graph[i] = Node(int(inputs[start + i]))

start = start + amountProducts
#contruct graph
for i in range(amountsRecipes):
    u = int(inputs[start+3*i+1])
    v = int(inputs[start+3*i])
    travelCost = int(inputs[start+3*i+2])
    graph[u].addEdge(v, travelCost)
    graph[v].indegree += 1

queue = []
for node in graph:
    if(graph[node].indegree == 0):
        queue.append(node)

#topo sort
def topoSort():
    global graph
    global queue
    global result
    if(len(queue) > 0):
        node = queue.pop(0)
        result[node] = graph[node].value
        for edge in graph[node].edges:
            graph[edge.end].value += graph[node].value * edge.travelCost
            graph[edge.end].indegree -= 1
            if(graph[edge.end].indegree == 0):
                queue.append(edge.end)


while(len(queue) > 0):
    topoSort()

for i in range(amountProducts):
    print(result[i], end =" "),



