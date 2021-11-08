#solution for https://open.kattis.com/problems/narrowartgallery/
import fileinput

inputMessage = ""

for line in fileinput.input():
    inputMessage+=line

inputs = inputMessage.split()

N = int(inputs[0])
k = int(inputs[1])
left = 0
right = 1
inf = 1000000
gallery = [[0 for i in range(2)] for j in range(N)]
intermediates = [[[None for i in range(2)]for j in range(N)]for m in range(k+1)]
result = 0

for i in range(2*N):
    gallery[i//2][i%2] = int(inputs[2+i])
    result += int(inputs[2+i])

def searchMinValueRoomsToClosed(roomToClosed, row, col):
    if roomToClosed == 0:
        return 0
    if row < 0:
        return inf
    if(intermediates[roomToClosed][row][col] != None):
        return intermediates[roomToClosed][row][col]
    intermediates[roomToClosed][row][col] = min(searchMinValueRoomsToClosed(roomToClosed - 1, row-1, col)+gallery[row][col], SearchMinValueRoomsToClosed(roomToClosed, row-1))
    return intermediates[roomToClosed][row][col]
    
def SearchMinValueRoomsToClosed(roomToClosed, row):
    return min(searchMinValueRoomsToClosed(roomToClosed, row, left), searchMinValueRoomsToClosed(roomToClosed, row, right))


result -= SearchMinValueRoomsToClosed(k, N-1)

print(result)