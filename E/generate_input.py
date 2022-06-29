import random


def main():
    numbers_len = 10**5
    with open("E/input5.txt", "w") as f:
        f.write(str(numbers_len) + "\n")
        for _ in range(numbers_len):
            xl = random.randint(-10**9, 10**9 - 1)
            xr = random.randint(xl + 1, 10**9)
            yl = random.randint(-10**9, 10**9 - 1)
            yr = random.randint(yl + 1, 10**9)
            f.write("{} {} {} {}\n".format(xl, yl, xr, yr))


if __name__ == "__main__":
    main()
