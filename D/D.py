import sys
import timeit


def get_L(S, R, counts):
    median = 0.5
    SR = int(S[R-1])
    for L in range(1, R):
        counts[R-1] = counts[R-2] + (1 if SR == 1 else -1)
        C = counts[R-1] - (0 if L == 1 else counts[L-2])
        if C < 0:
            median = 0
        elif C > 0:
            median = 1
        if SR == median:
            return L
        if abs(C) > R - L:
            break
    return -1


def main():
    input_number = 5
    with open(f"D/input{input_number}.txt") as f:
        N = int(f.readline())
        S = f.readline()

    counts = [-1 if int(S[0]) == 0 else 1] + [None] * (N - 1)

    with open(f"D/output{input_number}.txt", "w") as f:
        f.write("-1 ")
        for R in range(2, N + 1):
            f.write("{} ".format(get_L(S, R, counts)))

    # print("-1 ", end='')
    # for R in range(2, N + 1):
    #     print("{} ".format(get_L(S, R, counts)), end='')


if __name__ == "__main__":
    elapsed_time = timeit.timeit(stmt="main()", globals=globals(), number=1)
    print("Execution time: {:.3f} seconds".format(elapsed_time))
