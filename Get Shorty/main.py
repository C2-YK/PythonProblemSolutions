#import file
import fileinput
import sys
sys.setrecursionlimit(15000)

#class def
class Edge:
    def __init__(self, end, travelCost):
        self.end = end
        self.travelCost = travelCost

class Node:
    def __init__(self, value):
        self.edges = []
        self.value = value
    def addEdge(self, end, travelCost):
        self.edges.append(Edge(end, travelCost))

inf = 0 #in this question, we want to find closest to 1 traveling cost, in other word, 0 is defined as inf

inputMessage = ""

for line in fileinput.input():
    inputMessage+=line

inputs = inputMessage.split()

n = int(inputs[0])
m = int(inputs[1])
start = 2
startupSize = 1
nodes = []

for i in range(n):
    nodes.append(Node(inf))

for i in range(start, 3*m + start, 3):
    nodes[int(inputs[i])].addEdge(int(inputs[i+1]), float(inputs[i+2]))
    nodes[int(inputs[i+1])].addEdge(int(inputs[i]), float(inputs[i+2]))

def WFS(queue):
    global nodes
    while(len(queue)> 0):
        node = queue.pop(0)
        for e in nodes[node].edges:
            if(nodes[e.end].value < nodes[node].value * e.travelCost):
                nodes[e.end].value = nodes[node].value * e.travelCost
                queue.append(e.end)

queue = [0]
nodes[0].value = 1

WFS(queue)
print(nodes[n-1].value)