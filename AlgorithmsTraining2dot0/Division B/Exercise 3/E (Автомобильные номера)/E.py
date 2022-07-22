import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        M = int(f.readline().strip())
        witnesses = [set() for _ in range(M)]
        for i in range(M):
            witnesses[i].update(list(f.readline().strip()))
            
        N = int(f.readline().strip())
        numbers = [""] * N
        for i in range(N):
            numbers[i] = f.readline().strip()
        
        max_idxs = []
        max_count_matches = 0
        for i in range(N):
            count_matches = 0
            for j in range(M):
                if witnesses[j].issubset(set(numbers[i])):
                    count_matches += 1
            if count_matches > max_count_matches:
                max_idxs = [i]
                max_count_matches = count_matches
            elif count_matches == max_count_matches:
                max_idxs.append(i)

        results = [""] * len(max_idxs)
        for i in range(len(max_idxs)):
            results[i] = numbers[max_idxs[i]]


    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("\n".join(results))


if __name__ == "__main__":
    main()
