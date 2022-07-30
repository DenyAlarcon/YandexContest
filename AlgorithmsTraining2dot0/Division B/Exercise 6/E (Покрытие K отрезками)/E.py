import sys

test_number = 2


def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        _, k = map(int, f.readline().strip().split())
        numbers = list(map(int, f.readline().strip().split()))
    
    numbers.sort()

    left = 0
    right = (numbers[-1] - numbers[0]) // k + 1
    while left < right:
        l = (right + left) // 2
        k_current = 0
        right_bound = numbers[0] - 1
        for number in numbers:
            if number > right_bound:
                k_current += 1
                right_bound = number + l
        if k_current > k:
            left = l + 1
        else:
            right = l
    
    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(str(left))


if __name__ == "__main__":
    main()
