import sys
import time
import tracemalloc

test_number = 7

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        N = int(f.readline().strip())
        numbers = list(map(int, f.readline().strip().split()))
        K = int(f.readline().strip())
        requests = [None] * K
        for i in range(K):
            requests[i] = tuple(map(int, f.readline().strip().split()))

    numbers.sort()
    request_numbers_left = [request[0] for request in requests]
    request_numbers_right = [request[1] for request in requests]
    request_numbers_left.sort()
    request_numbers_right.sort()
    numbers_counts_left = {}
    request_numbers_left_idx = 0
    for i in range(N):
        if request_numbers_left_idx < len(request_numbers_left):
            while request_numbers_left_idx < len(request_numbers_left) - 1 and request_numbers_left[request_numbers_left_idx] < numbers[i]:
                if request_numbers_left[request_numbers_left_idx] not in numbers_counts_left:
                    numbers_counts_left[request_numbers_left[request_numbers_left_idx]] = i
                request_numbers_left_idx += 1
            if request_numbers_left[request_numbers_left_idx] not in numbers_counts_left:
                numbers_counts_left[request_numbers_left[request_numbers_left_idx]] = i
            if request_numbers_left[request_numbers_left_idx] > numbers[i]:
                numbers_counts_left[request_numbers_left[request_numbers_left_idx]] += 1
        else:
            break
    while request_numbers_left_idx < len(request_numbers_left):
        if request_numbers_left[request_numbers_left_idx] not in numbers_counts_left:
            numbers_counts_left[request_numbers_left[request_numbers_left_idx]] = i + 1
        request_numbers_left_idx += 1

    numbers_counts_right = {}
    request_numbers_right_idx = 0
    for i in range(N):
        if request_numbers_right_idx < len(request_numbers_right):
            while request_numbers_right_idx < len(request_numbers_right) - 1 and request_numbers_right[request_numbers_right_idx] < numbers[i]:
                if request_numbers_right[request_numbers_right_idx] not in numbers_counts_right:
                    numbers_counts_right[request_numbers_right[request_numbers_right_idx]] = i
                request_numbers_right_idx += 1
            if request_numbers_right[request_numbers_right_idx] not in numbers_counts_right:
                numbers_counts_right[request_numbers_right[request_numbers_right_idx]] = i
            if request_numbers_right[request_numbers_right_idx] >= numbers[i]:
                numbers_counts_right[request_numbers_right[request_numbers_right_idx]] += 1
            else:
                request_numbers_right_idx += 1
        else:
            break

    while request_numbers_right_idx < len(request_numbers_right):
        numbers_counts_right[request_numbers_right[request_numbers_right_idx]] = i + 1
        request_numbers_right_idx += 1

    results = [0] * K
    for i in range(K):
        L, R = requests[i]
        results[i] = numbers_counts_right[R] - numbers_counts_left[L]
    
    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(" ".join(map(str, results)))


if __name__ == "__main__":
    tracemalloc.start()
    t1 = time.time()
    main()
    t2 = time.time()
    print("Elapsed time is:", t2 - t1, "seconds")
    print("Memory used is:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MiB")
    tracemalloc.stop()
