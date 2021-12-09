#import file
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

def tsp(u, visited, cost, count):
    if(count == n):
            global answer
            answer.append(matrix[u][0]+cost)
            return
    for i in range(len(visited)):
        if(not visited[i]):
            visited[i] = True
            tsp(i, visited, cost+matrix[u][i], count+1)
            visited[i] = False

visited = [False for i in range(n)]     
tsp(0, visited, 0, 1)
print(min(answer))
