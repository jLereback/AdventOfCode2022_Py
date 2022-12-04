def part1(f):
    ans = 0
    for lines in f:
        a, b = lines.split(",")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        a1, a2, b1, b2 = [int(i) for i in [a1, a2, b1, b2]]
        if a1 >= b1 and a2 <= b2 or a1 <= b1 and a2 >= b2:
            ans += 1
    return ans


def part2(f):
    ans = 0
    for lines in f:
        a, b = lines.split(",")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        a1, a2, b1, b2 = [int(i) for i in [a1, a2, b1, b2]]
        if a1 <= b2 <= a2 or b1 <= a2 <= b2:
            ans += 1
    return ans
