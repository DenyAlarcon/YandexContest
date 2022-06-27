import sys


def get_median(S):
    C0 = S.count('0')
    C1 = S.count('1')
    if C0 > C1:
        return 0
    elif C1 > C0:
        return 1
    return 0.5


def get_L(S, R):
    SR = int(S[R-1])
    for L in range(0, R):
        if L < R - 1 and SR == get_median(S[L:R]):
            return L + 1
    return -1


def main():
    N = int(sys.stdin.readline())
    S = sys.stdin.readline()

    L = [-1]

    for R in range(2, N + 1):
        L.append(get_L(S, R))

    print(' '.join(map(str, L)))


if __name__ == "__main__":
    main()
