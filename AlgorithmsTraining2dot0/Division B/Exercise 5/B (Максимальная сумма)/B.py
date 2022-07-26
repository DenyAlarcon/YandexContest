import sys

test_number = 6

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        f.readline()
        numbers = list(map(int, f.readline().strip().split()))

        max_sum = int(-10e9)
        current_sum = 0

        for number in numbers:
            if current_sum + number > 0:
                current_sum += number
                max_sum = max(current_sum, max_sum)
            else:
                current_sum = 0

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(str(max(max_sum, max(numbers))))


if __name__ == "__main__":
    main()
