import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        buildings = list(map(int, f.readline().strip().split()))

    buildings_len = len(buildings)
    max_distance = 0
    for i in range(buildings_len):
        if buildings[i] == 1:
            min_distance = 10
            current_distance = 1
            for j in range(i-1, -1, -1):
                if buildings[j] == 2:
                    min_distance = current_distance
                    break
                current_distance += 1
            
            current_distance = 1
            for j in range(i+1, buildings_len):
                if buildings[j] == 2 and current_distance < min_distance:
                    min_distance = current_distance
                    break
                current_distance += 1
            if min_distance > max_distance:
                max_distance = min_distance
            

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(str(max_distance))


if __name__ == "__main__":
    main()
