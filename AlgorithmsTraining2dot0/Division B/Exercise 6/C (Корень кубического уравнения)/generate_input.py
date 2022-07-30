def cube_root(x):
    if x < 0:
        x = abs(x)
        result = x**(1/3)*(-1)
    else:
        result = x**(1/3)
    return result

def main():
    MIN_NUMBER = -5
    MAX_NUMBER = 5
    for a in range(MIN_NUMBER, MAX_NUMBER + 1):
        for b in range(MIN_NUMBER, MAX_NUMBER + 1):
            for c in range(MIN_NUMBER, MAX_NUMBER + 1):
                for d in range(MIN_NUMBER, MAX_NUMBER + 1):
                    p = -((b ** 2) / (3*(a**2))) + (c/a)
                    q = ((2*(b**3))/(27*(a**3))) - ((b*c)/(3*(a**2))) + (d/a)
                    Q = ((p/3)**3) + ((q/2)**2)
                    if Q > 0:
                        alpha = cube_root(-(q/2) + Q**(1/2))
                        beta = cube_root(-(q/2) - Q**(1/2))
                        y = alpha + beta
                        x = y - (b / (3*a))
                        print(a, b, c, d, "--->", x)


if __name__ == "__main__":
    main()
