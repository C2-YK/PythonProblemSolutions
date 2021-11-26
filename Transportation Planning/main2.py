#solution of https://open.kattis.com/problems/transportationplanning
import fileinput

#read inputs
inputMessage = ""

for line in fileinput.input():
    inputMessage+=line

inputs = inputMessage.split()

#class def
class Edge:
    def __init__(self, end, travelCost):
        self.end = end
        self.travelCost = travelCost

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#global varibles
n = int(inputs[0])
m = int(inputs[2*n+1])
inf = 10000
nodes = []
dists = [[inf for x in range(n)] for y in range(n)] 

#helper methods
def getDist(u, v):
    global nodes
    return ((nodes[u].x - nodes[v].x)**2 + (nodes[u].y - nodes[v].y)**2)**(1/2)

def connect(dists, u, v):
    dist = getDist(u, v)
    dists[u][v] = dist
    dists[v][u] = dist
def disconnect(dists, u, v):
    dists[u][v] = inf
    dists[v][u] = inf

def initDists():
    global dists
    dists = []

    for i in range(n):
        dists.append([])
        for j in range(n):
            if(i == j):
                dists[i].append(0)
            else:
                dists[i].append(inf)

    for i in range(2*n+2, 2*n+2*m+2, 2):
        u = int(inputs[i])
        v = int(inputs[i+1])
        connect(dists, u, v)

def floydWarshal(cost):
    for k in range(n):    
        for i in range(n):
            for j in range(n):
                if(cost[i][k]+cost[k][j] < cost[i][j]):
                    cost[i][j] = cost[i][k]+cost[k][j]
        


def getSum(cost):
    sum = 0
    for i in range(n):
        for j in range(i+1, n, 1):
            sum += cost[i][j]
    return sum

#contruct graph
for i in range(n):
    nodes.append(Node(int(inputs[2*i + 1]), int(inputs[2*i + 2])))

initDists()
floydWarshal(dists)

#if below max edges, find a new edge has the greatest different add it to the graph
if(m < n * (n - 1) / 2):
    #find a edge to add
    sum = getSum(dists)
    maxDiff = 0
    for u in range(n):
        for v in range(u+1, n, 1):
            if(dists[u][v]>getDist(u, v)):
                diff = 0
                for i in range(n):
                    for j in range(n):
                        if(dists[i][j] > dists[i][u] + getDist(u, v) + dists[v][j]):
                            diff += dists[i][j] - (dists[i][u] + getDist(u, v) + dists[v][j])
                if(diff > maxDiff):
                    maxDiff = diff
    print(sum - maxDiff)
else:
    print(getSum(dists))