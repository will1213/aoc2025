with open("input.txt", "r") as f:
    lines = f.readlines()

myLine = []
for line in lines:
    oneLine = list(line)
    myLine.append(oneLine)
## minus the new line character
x = len(lines[0]) - 1 
y = len(lines)

def checkAround(r, c):
    steps = [[0, 1], [0, -1], [1, 1], [1, 0], [1, -1], [-1, 0], [-1, -1], [-1, 1]]
    count = 0
    for step in steps:
        tempR = r + step[0]
        tempC = c + step[1]
        if  x > tempR >= 0 and x > tempC >= 0:
            if myLine[tempR][tempC] == "@":
                count += 1
                if count > 3:
                    return False
    if count < 4:
        return True
    return False

def part1():
    ans = 0
    for i in range(x):
        for j in range(x):
            if myLine[i][j] == "@":
                if checkAround(i, j):
                    ans +=  1
    return ans

print(part1())

def oneRound():
    toRemove = []
    for i in range(x):
        for j in range(x):
            if myLine[i][j] == "@":
                if checkAround(i, j):
                    toRemove.append([i, j])
    return toRemove

def part2():
    ans = 0
    toRemove = oneRound()
    while toRemove:
        for remove in toRemove:
            i = remove[0]
            j = remove[1]
            myLine[i][j] = "."
            ans += 1
        toRemove = oneRound()
    return ans

print(part2())