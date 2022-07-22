import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        numbers = list(map(int, f.readline().strip().split()))

    numbers_len = len(numbers)
    results = [""] * numbers_len
    numbers_set = set()

    for i in range(numbers_len):
        if numbers[i] in numbers_set:
            results[i] = "YES"
        else:
            results[i] = "NO"
            numbers_set.add(numbers[i])
            

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("\n".join(results))


if __name__ == "__main__":
    main()
