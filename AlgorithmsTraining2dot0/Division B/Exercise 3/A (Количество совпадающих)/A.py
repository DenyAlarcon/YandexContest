import sys

test_number = 3

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        numbers1 = set(map(int, f.readline().strip().split()))
        numbers2 = set(map(int, f.readline().strip().split()))
            

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(str(len(numbers1.intersection(numbers2))))


if __name__ == "__main__":
    main()
