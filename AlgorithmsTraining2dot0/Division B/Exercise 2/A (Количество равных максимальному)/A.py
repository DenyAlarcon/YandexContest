import sys

test_number = 2

def main():
    numbers = []
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        for _ in range(10000):
            number = int(f.readline().strip())
            if number == 0:
                break
            numbers.append(number)

    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number

    count_max_numbers = 0
    for number in numbers:
        if number == max_number:
            count_max_numbers += 1

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(str(count_max_numbers))


if __name__ == "__main__":
    main()
