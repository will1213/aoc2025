with open("input.txt", "r") as f:
    lines = f.readlines()

def part1():
    pos = 50
    ans = 0
    for line in lines:
        line = line.strip()
        op, num = line[0], int(line[1:])
        if op == "L":
            pos -= num
        else:
            pos += num
        pos %= 100

        if pos == 0:
            ans += 1
    return ans

print(part1())

def part2():
    pos = 50
    ans = 0
    for line in lines:
        line = line.strip()
        op, num = line[0], int(line[1:])
        ans += num // 100
        num %= 100
        if num != 0:
            atZero = pos == 0
            if op == "L":
                pos -= num
            else:
                pos += num
            if pos == 100 or pos == 0:
                ans += 1
            elif not atZero and abs(pos // 100) > 0:
                ans += 1
            pos %= 100
    return ans

print(part2())
