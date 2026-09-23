def hamming_distance(s1, s2):
    counter = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            counter += 1
    return counter

with open("rosalind_2", 'r') as file:
    s1 = file.readline().strip()
    s2 = file.readline().strip()

string = hamming_distance(s1, s2)
print(string)
