import random
import sys

test_number = 5

def main():
    MIN_NUMBER = int(-10e9)
    MAX_NUMBER = int(10e9)
    MAX_ARR_LEN = int(10e5)
    MAX_REQUESTS = int(10e5)
    
    with open(f"{sys.path[0]}/input{test_number}.txt", "w") as f:
        f.write(str(MAX_ARR_LEN))
        arr = list(range(1, MAX_ARR_LEN + 1))
        f.write("\n" + " ".join(map(str, arr)))
        f.write("\n" + str(MAX_ARR_LEN))
        for i in range(MAX_REQUESTS):
            request = (-2*MAX_REQUESTS + i, -MAX_REQUESTS + i)
            f.write("\n" + " ".join(map(str, request)))


if __name__ == "__main__":
    main()
