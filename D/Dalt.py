import sys


def get_median(S, R, L):
    C0 = 0
    C1 = 0

    for i in range(R - L):
        if S & 1 << i == 0:
            C0 += 1
        else:
            C1 += 1

    # print(f"C0 {C0} C1 {C1} ")
    if C0 > C1:
        return 0
    elif C1 > C0:
        return 1
    return 0.5


def get_L(S, R, N):
    SR = 1 if S & 1 << (N - R) != 0 else 0
    for L in range(0, R):
        # print(f"SR: {SR} L: {L} R: {R} S >> L + 1: {bin(S >> (N - R))}")
        if L < R - 1 and SR == get_median(S >> (N - R), R, L):
            return L + 1
    return -1


def main():
    N = int(sys.stdin.readline())
    S = int('1' + sys.stdin.readline(), 2)
    print("-1 ", end='')

    for R in range(2, N + 1):
        print("{} ".format(get_L(S, R, N)), end='')
        # print("\n")


if __name__ == "__main__":
    main()
