def double_degree_array():
    with open("rosalind7") as file:
        n, m = map(int, file.readline().split())
        adj_list = [[] for _ in range(n + 1)] #создаем список с пустыми списками для соседей
        for _ in range(m):
            line = file.readline()
            u, v = map(int, line.split())
            adj_list[u].append(v)
            adj_list[v].append(u)  
    degrees = [] #создаем список степеней вершин
    for i in range(n + 1):
        degrees.append(len(adj_list[i]))

    result = []
    for i in range(1, n + 1):
        neighbor_sum = 0
        for neighbor in adj_list[i]:
            neighbor_sum += degrees[neighbor] 
        result.append(neighbor_sum)

    print(*(result))
double_degree_array()