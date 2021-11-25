#solution of https://open.kattis.com/problems/transportationplanning
import fileinput

#class def
class Edge:
    def __init__(self, end, travelCost):
        self.end = end
        self.travelCost = travelCost

class Node:
    def __init__(self, value, x, y):
        self.edges = []
        self.value = value
        self.x = x
        self.y = y
    def addEdge(self, end, travelCost):
        self.edges.append(Edge(end, travelCost))
    def popEdge(self):
        self.edges.pop(len(self.edges)-1)

#global varibles
inf = 10000000
nodes = []
queue = []
dist = []

#helper methods
def getDist(u, v):
    global nodes
    return ((nodes[u].x - nodes[v].x)**2 + (nodes[u].y - nodes[v].y)**2)**(1/2)

def connect(u, v):
    global nodes
    dist = getDist(u, v)
    nodes[u].addEdge(v, dist)
    nodes[v].addEdge(u, dist)
def disconnect(u, v):
    nodes[u].popEdge()
    nodes[v].popEdge()

def resetDist():
    global dist
    dist = []

    for i in range(n):
        dist.append([])
        for j in range(n):
            if(i == j):
                dist[i].append(0)
            else:
                dist[i].append(inf)

def WFS(queue, start):
    global nodes
    while(len(queue)> 0):
        node = queue.pop(0)
        for e in nodes[node].edges:
            #if tense
            if(dist[start][e.end] > dist[start][node] + e.travelCost):
                dist[start][e.end] = dist[start][node] + e.travelCost
                queue.append(e.end)

def distSum():
    global dist
    sum = 0
    for i in range(n):
        for j in range(i+1, n, 1):
            sum += dist[i][j]
    return sum

#read inputs
inputMessage = ""

for line in fileinput.input():
    inputMessage+=line

inputs = inputMessage.split()

n = int(inputs[0])
m = int(inputs[2*n+1])

#contruct graph
for i in range(n):
    nodes.append(Node(inf, int(inputs[2*i + 1]), int(inputs[2*i + 2])))
for i in range(2*n+2, 2*n+2*m+2, 2):
    u = int(inputs[i])
    v = int(inputs[i+1])
    connect(u, v)

#init dist matirx
resetDist()

#compute shortest dist
for i in range(n):
    queue.append(i)
    WFS(queue, i)

#if below max edges, find a new edge has the greatest different add it to the graph
if(m < n * (n - 1) / 2):
    #find a edge to add
    i = -1
    j = -1
    diff = 0
    preSum = distSum()
    for u in range(n):
        for v in range(u+1, n, 1):
            if(dist[u][v]>getDist(u, v)):
                #add the new edge
                connect(u, v)
                #recompute the shortest path
                resetDist()
                for i in range(n):
                    queue.append(i)
                    WFS(queue, i)
                sum = distSum()
                if(preSum - sum > diff):
                    diff = preSum - sum
                    i = u
                    j = v
                disconnect(u, v)
    print(preSum - diff)
else:
    sum = distSum()
    print(sum)