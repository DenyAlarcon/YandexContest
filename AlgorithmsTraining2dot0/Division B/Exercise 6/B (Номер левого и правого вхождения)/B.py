import sys

test_number = 4

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        N = int(f.readline().strip())
        numbers = list(map(int, f.readline().strip().split()))
        M = int(f.readline().strip())
        requests = list(map(int, f.readline().strip().split()))

    requests_sorted = sorted(requests)
    requests_left = {}
    requests_right = {}
    requests_idx = 0
    for i in range(N):
        if requests_idx < M:
            while requests_idx < M - 1 and requests_sorted[requests_idx] < numbers[i]:
                if requests_sorted[requests_idx] not in requests_left:
                    requests_left[requests_sorted[requests_idx]] = 0
                    requests_right[requests_sorted[requests_idx]] = 0
                requests_idx += 1
            if requests_sorted[requests_idx] == numbers[i]:
                if requests_sorted[requests_idx] not in requests_left or requests_left[requests_sorted[requests_idx]] == 0:
                    requests_left[requests_sorted[requests_idx]] = i + 1
                requests_right[requests_sorted[requests_idx]] = i + 1
            elif requests_sorted[requests_idx] > numbers[i]:
                requests_left[requests_sorted[requests_idx]] = 0
                requests_right[requests_sorted[requests_idx]] = 0
        else:
            break

    while requests_idx < M:
        if requests_sorted[requests_idx] not in requests_left:
            requests_left[requests_sorted[requests_idx]] = 0
            requests_right[requests_sorted[requests_idx]] = 0
        requests_idx += 1

    results = [0] * M
    for i in range(M):
        results[i] = requests_left[requests[i]], requests_right[requests[i]]
    
    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("\n".join(" ".join(map(str, result)) for result in results))


if __name__ == "__main__":
    main()
