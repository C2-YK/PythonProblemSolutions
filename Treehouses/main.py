#import file
import fileinput
import sys
sys.setrecursionlimit(15000)
inputMessage = ""

for line in fileinput.input():
    inputMessage+=line

inputs = inputMessage.split()

n = int(inputs[0])
e = int(inputs[1])
p = int(inputs[2])
start = 3
result = 0

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.comp = 0
        self.vs = []
        self.mark = False

class Edge:
    def __init__(self, weight, u, v):
        self.u = u
        self.v = v
        self.weight = weight
        self.connected = False


def getDist(u, v):
    return ((u.x - v.x)**2 + (u.y - v.y)**2)**(1/2)

nodes = [] #nodes[ID]
edges = []

for i in range(n + 1):
    nodes.append(None)

for i in range(n):
    nodes[i+1] = Node(float(inputs[start+2*i]), float(inputs[start+2*i+1]))

start += 2*n

for i in range(p):
    nodes[int(inputs[start + 2*i])].vs.append(int(inputs[start + 2*i + 1]))
    nodes[int(inputs[start + 2*i + 1])].vs.append(int(inputs[start + 2*i]))

for i in range(e, 1, -1):
    nodes[1].vs.append(i)
    nodes[i].vs.append(1)
for u in range(1, n+1, 1):
    for v in range(u+1, n+1, 1):
        weight = getDist(nodes[u], nodes[v])
        edges.append(Edge(weight, u, v))
def WFS(Comp, queue):
    if(queue):
        global nodes
        target = queue[0]
        queue.pop(0)
        nodes[target].mark = True
        nodes[target].comp = Comp
        for v in nodes[target].vs:
            if not nodes[v].mark:
                queue.append(v)
        WFS(Comp, queue)

def assignComp():
    global nodes
    Comp = 0
    for i in range(1, n+1, 1):
        nodes[i].mark = False
    for i in range(1, n + 1, 1):
        if(not nodes[i].mark):
            Comp+=1
            queue = [i]
            WFS(Comp, queue)
    return Comp

def connect(edgeID):
    global nodes
    global edges
    if not edges[edgeID].connected:
        edges[edgeID].connected = True
        nodes[edges[edgeID].u].vs.append(edges[edgeID].v)
        nodes[edges[edgeID].v].vs.append(edges[edgeID].u)
        global result
        result += edges[edgeID].weight

def addAllSafeEdges(comp):
    global edges
    global nodes
    safe = []
    for i in range(comp+1):
        safe.append(None)
    for i in range(len(edges)):
        if nodes[edges[i].u].comp != nodes[edges[i].v].comp:
            if safe[nodes[edges[i].u].comp] == None or edges[i].weight < edges[safe[nodes[edges[i].u].comp]].weight:
                safe[nodes[edges[i].u].comp] = i
            if safe[nodes[edges[i].v].comp] == None or edges[i].weight < edges[safe[nodes[edges[i].v].comp]].weight:
                safe[nodes[edges[i].v].comp] = i
    for i in range(1, comp+1, 1):
        connect(safe[i])

        

Comp = assignComp()
while(Comp > 1):
    addAllSafeEdges(Comp)
    Comp = assignComp()

print(result)

