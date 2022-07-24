import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        f.readline().strip()


    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("")


if __name__ == "__main__":
    main()
