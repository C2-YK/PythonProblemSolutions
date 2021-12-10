#import file
import sys
sys.setrecursionlimit(15000)
import fileinput
inputMessage = ""

for line in fileinput.input():
    inputMessage+=line

inputs = inputMessage.split()

n = int(inputs[0])
matrix = []
index = 0
for i in range(0, n*n, n):
    matrix.append([])
    for j in range(1, n+1, 1):
        matrix[index].append(int(inputs[i + j]))
    index+=1

answer = []
memo = {((0,), 0):0} #visited, current : cost
allVertex = set(range(n))

def tsp(visited, curr):
    toVisit = allVertex.difference(set(visited))
    cost = memo[(visited, curr)]
    if(len(toVisit) == 0):
        next = 0
        next_visited = tuple(list(visited) + [next])
        next_cost = cost + matrix[curr][next]
        if(next_visited, next) not in memo:
            memo[(next_visited, next)] = next_cost
        else:
            if next_cost < memo[(next_visited, next)]:
                memo[(next_visited, next)] = next_cost
        return
    for next in toVisit:
        next_visited = tuple(sorted(list(visited) + [next]))
        next_cost = cost + matrix[curr][next]
        if(next_visited, next) not in memo:
            memo[(next_visited, next)] = next_cost
        else:
            if next_cost < memo[(next_visited, next)]:
                memo[(next_visited, next)] = next_cost
        tsp(next_visited, next)


visited = (0,)
tsp(visited, 0)
circlePath = tuple(list(i for i in range(n)) + [0])
print(memo[circlePath, 0])