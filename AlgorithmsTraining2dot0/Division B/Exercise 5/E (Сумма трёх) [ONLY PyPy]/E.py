import sys
import time

test_number = 4

def main():
    with open(f"{sys.path[0]}/threesum{test_number}.in") as f:
        S = int(f.readline().strip())
        line = list(map(int, f.readline().strip().split()))
        nA, A = line[0], line[1:]
        line = list(map(int, f.readline().strip().split()))
        nB, B = line[0], line[1:]
        line = list(map(int, f.readline().strip().split()))
        nC, C = line[0], line[1:]

    dict_C = {}
    for k in range(nC):
        if S - C[k] >= 2 and C[k] not in dict_C:
            dict_C[C[k]] = k

    result = "-1"
    for i in range(nA):
        if result != "-1":
            break
        for j in range(nB):
            value_C = S - A[i] - B[j]
            if value_C > 0 and value_C in dict_C:
                result = " ".join(map(str, (i, j, dict_C[value_C])))
                break

    with open(f"{sys.path[0]}/threesum{test_number}.out", "w") as f:
        f.write(result)


if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print("Elapsed time is:", t2 - t1, "seconds")
