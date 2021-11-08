#solution for https://open.kattis.com/problems/gold
import fileinput
import sys
sys.setrecursionlimit(1500)
inputMessage = ""

for line in fileinput.input():
    inputMessage+=line

inputs = inputMessage.split()

#import values
col = int(inputs[0])
row = int(inputs[1])
startID = 2
playerPos = 0
gameMap = []
visited = []
result = 0
for i in range(row):
    for j in inputs[i+startID]:
        gameMap.append(j)
        visited.append(False)

for i in range(col*row):
    if(gameMap[i] == "P"):
        playerPos = i
        break

def findGold(position):
    #mark and check this position
    visited[position] = True
    if(gameMap[position] == "G"):
        global result
        result += 1
    elif(gameMap[position] == "#"):
        return

    right = position + 1
    left = position -1
    up = position - col
    down = position + col
    directions = [right, left, up, down]
    #return if the position is dangerous to move forward
    for direction in directions:
        if(direction>=0 and direction<len(gameMap)):
            if(gameMap[direction] == "T"):
                return
    #visit direction if it can and has not be visited
    for direction in directions:
        if(direction>=0 and direction<len(gameMap)):
            if(not visited[direction]):
                findGold(direction)

findGold(playerPos)

print(result)

