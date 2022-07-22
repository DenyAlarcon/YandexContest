import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        numbers = list(map(int, f.readline().strip().split()))

    numbers_dict = {}
    for i in range(len(numbers)):
        if numbers[i] not in numbers_dict:
            numbers_dict[numbers[i]] = 0
        numbers_dict[numbers[i]] += 1

    results = []
    for key in numbers_dict.keys():
        if numbers_dict[key] == 1:
            results.append(key)
            

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(" ".join(str(result) for result in results))


if __name__ == "__main__":
    main()
