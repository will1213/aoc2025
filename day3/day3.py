with open("input.txt", "r") as f:
    lines = f.readlines()

def part1():
    ans = 0
    for line in lines:
        line = line.strip()
        first = max(line[:-1])
        for i in range(len(line)):
            if line[i] == first:
                break
        second = max(line[i+1:])
        ans += int(first+second)
    return ans
    
print(part1())

def helper(num, digit):
    if digit == 0:
        return max(num)
    myMax = max(num[:-digit])
    for i in range(len(num)):
        if num[i] == myMax:
            break
    myMax += helper(num[i+1:], digit-1)
    return myMax

def part2():
    ans = 0
    for line in lines:
        line = line.strip()
        ans += int(helper(line, 11))
    return ans

print(part2())