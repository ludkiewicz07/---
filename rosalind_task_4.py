def majority_element(m):
    major = len(m) / 2
    for i in m:
        counter = m.count(i)
        if counter > major:
            return i
    return -1

elements = []

with open("rosalind_4") as file:
    first_line = file.readline().strip()
    k, n = map(int, first_line.split())
    for line in file:
        m = list(map(int, line.split()))
        element = majority_element(m)
        elements.append(element)

print(*elements)

