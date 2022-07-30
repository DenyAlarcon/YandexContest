import sys

test_number = 3


def cube_root(x):
    if x < 0:
        x = abs(x)
        result = x**(1/3)*(-1)
    else:
        result = x**(1/3)
    return result


def main():
    with open(f"{sys.path[0]}/cubroot{test_number}.in") as f:
        a, b, c, d = map(int, f.readline().strip().split())

    p = -((b ** 2) / (3*(a**2))) + (c/a)
    q = ((2*(b**3))/(27*(a**3))) - ((b*c)/(3*(a**2))) + (d/a)

    Q = ((p/3)**3) + ((q/2)**2)
    alpha = cube_root(-(q/2) + Q**(1/2))
    beta = cube_root(-(q/2) - Q**(1/2))

    y = alpha + beta
    x = y - (b / (3*a))

    with open(f"{sys.path[0]}/cubroot{test_number}.out", "w") as f:
        f.write("{:.5f}".format(x))


if __name__ == "__main__":
    main()
