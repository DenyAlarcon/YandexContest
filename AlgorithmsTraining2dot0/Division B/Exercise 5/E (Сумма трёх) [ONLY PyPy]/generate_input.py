import random
import sys

test_number = 4

def main():
    MAX_NUMBER = int(10e9)
    MAX_ARR_LEN = 15000
    S = 3 * MAX_ARR_LEN
    with open(f"{sys.path[0]}/threesum{test_number}.in", "w") as f:
        f.write(str(S))
        for _ in range(3):
            n = MAX_ARR_LEN
            # arr = random.sample(range(1, MAX_NUMBER + 1), n)
            arr = list(range(1, MAX_ARR_LEN + 1))
            f.write("\n" + " ".join(map(str, [n] + arr)))


if __name__ == "__main__":
    main()
