def check_path(citites_inputs, results, visited, current_city, end, path_length): 
    path_length += 1
    for city_input in citites_inputs[current_city - 1]:
        if city_input == end:
            results.append(path_length)
        elif current_city not in visited:
            visited.append(current_city)
            check_path(citites_inputs, results, visited, city_input, end, path_length)

def main():
    cities_coords = []
    with open("G/input3.txt") as f:
        n = int(f.readline().strip())
        for _ in range(n):
            cities_coords.append(tuple(map(int, f.readline().split())))
        k = int(f.readline().strip())
        path = tuple(map(int, f.readline().split()))

    citites_inputs = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if abs(cities_coords[i][0] - cities_coords[j][0]) + abs(cities_coords[i][1] - cities_coords[j][1]) <= k:
                citites_inputs[i].append(j + 1)
                citites_inputs[j].append(i + 1)

    results = []
    check_path(citites_inputs, results, [], path[0], path[1], 0)
    

    with open("G/output3.txt", "w") as f:
        if len(results) > 0:
            f.write(str(min(results)))
        else:
            f.write(str(-1))

if __name__ == "__main__":
    main()
