def merge_arrays(array_m, array_n):
    result = []
    i = 0
    j = 0
    while i < len(array_m) and j < len(array_n):
        if array_m[i] <= array_n[j]:
            result.append(array_m[i])
            i += 1
        else:
            result.append(array_n[j])
            j += 1
    while i < len(array_m):
        result.append(array_m[i])
        i += 1
    while j < len(array_n):
        result.append(array_n[j])
        j += 1
    return result
with open("rosalind5") as file:
    n = int, file.readline().strip().split()
    array_n = list(map(int, file.readline().strip().split()))
    m = int, file.readline().strip().split()
    array_m = list(map(int, file.readline().strip().split()))
final_array = merge_arrays(array_m, array_n)
print(*final_array)