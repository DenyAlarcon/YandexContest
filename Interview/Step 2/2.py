# Дана последовательность неповторяющихся возрастающих целых чисел, нужно вернуть отрезки, содержащие возрастающие на единицу последовательности.

# [-2, -1, 1, 5] -> [-2, -1], [1], [5]
# [1, 2, 3, 4] -> [1, 2, 3, 4]
# [1, 3, 5, 7] -> [1], [3], [5], [7]
# [1, 2, 3, 7] -> [1, 3], [7]

def get_slices(numbers):
    results = []
    first_num = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1] + 1:
            if first_num == numbers[i - 1]:
                results.append([first_num])
            else:
                results.append([first_num, numbers[i - 1]])
            first_num = numbers[i]
    if first_num == numbers[-1]:
        results.append([first_num])
    else:
        results.append([first_num, numbers[-1]])
    return results


def main():
    test_cases = [
        [-2, -1, 1, 5],
        [1, 2, 3, 4],
        [1, 3, 5, 7],
        [1, 2, 3, 7]
    ]

    for test_case in test_cases:
        print("{} ---> {}".format(test_case, get_slices(test_case)))


if __name__ == "__main__":
    main()
