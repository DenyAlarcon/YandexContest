def bfs(graph, start, end):
    path_length = 0
    visited = [start]
    queue = [start]
    
    while queue:
        s = queue.pop(0)
        path_length += 1
        
        for neighbor in graph[s]:
            if neighbor == end:
                return path_length
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return -1

def main():
    cities_coords = []
    with open("G/input3.txt") as f:
        n = int(f.readline().strip())
        for _ in range(n):
            cities_coords.append(tuple(map(int, f.readline().split())))
        k = int(f.readline().strip())
        path = tuple(map(int, f.readline().split()))

    graph = dict.fromkeys(range(1, n + 1), [])

    for i in range(n):
        for j in range(i + 1, n):
            if abs(cities_coords[i][0] - cities_coords[j][0]) + abs(cities_coords[i][1] - cities_coords[j][1]) <= k:
                graph[i + 1] = graph[i + 1] + [j + 1]
                graph[j + 1] = graph[j + 1] + [i + 1]
    

    with open("G/output3.txt", "w") as f:
        f.write(str(bfs(graph, path[0], path[1])))
            

if __name__ == "__main__":
    main()
