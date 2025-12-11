with open("input.txt", "r") as f:
    lines = f.readlines()

ranges = lines[0].split(",")

def invalid(start, end):
    ans = 0
    for i in range(start, end+1):
        num = str(i)
        l = len(num)
        half = l // 2
        if l % 2 == 0:
            if num[:half] == num[-half:]:
                ans += i
    return ans

def part1():
    ans = 0
    for range in ranges:
        first, second = range.split("-")
        ans += invalid(int(first), int(second))
    return ans

print(part1())


def invalid2(num):
    l = len(num)
    pattern = num[0]
    times = 1
    i = 1
    isPattern = False
    while i < l:
        isPattern = True
        for j in range(len(pattern)):
            if i >= l:
                isPattern  = False
                break
            if num[i] != pattern[j]:
                pattern = pattern * times
                if j != 0:
                    pattern += pattern[0]
                    i -= j
                else:
                    pattern += num[i]
                times = 1
                isPattern  = False
                break
            i += 1
        if isPattern:
            times += 1
        else:
            i += 1
    if times > 1:
        return isPattern
    return False


def part2():
    ans = 0
    for r in ranges:
        first, second = r.split("-")
        for i in range(int(first), int(second)+1):
            if invalid2(str(i)):
                ans += i
    return ans
print(part2())
