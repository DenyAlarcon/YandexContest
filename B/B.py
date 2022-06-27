import sys


def print_field(field):
    for row in field:
        for col in row:
            print(col, end='')
        print()


def get_inverted_field(field, n, m):
    inverted_field = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            inverted_field[i][j] = field[n-i-1][m-j-1]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if inverted_field[i-1][j] == '\\' or inverted_field[i-1][j] == '/':
                inverted_field[i][j] = inverted_field[i-1][j]
                inverted_field[i-1][j] = '.'
    return inverted_field


def main():
    n, m = map(int, sys.stdin.readline().split())
    field = [[0] * m for _ in range(n)]

    for i in range(n):
        field[i] = list(sys.stdin.readline().strip())

    inverted_field = get_inverted_field(field, n, m)
    print_field(inverted_field)


if __name__ == "__main__":
    main()
