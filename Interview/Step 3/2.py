# Дана последовательность целых чисел, нужно вернуть отрезок суммы X, если такой имеется.

# [-1, 2, 0, 5]: X=1 -> (-1, 2), X=3 -> -1.

def get_range_sum_X(numbers, X):
    dict_sums = {}
    current_sum = 0
    for i in range(len(numbers)):
        if numbers[i] + current_sum == X:
            return (0, i) if 0 != i else i
        current_sum += numbers[i]
        dict_sums[current_sum] = i
        if current_sum - X in dict_sums:
            return (dict_sums[current_sum - X] + 1, i) if dict_sums[current_sum - X] + 1 != i else i
    return -1


def main():
    test_cases = [
        ([-1, 2, 0, 5], -1),
        ([-1, 2, 0, 5], 1),
        ([-1, 2, 0, 5], 2),
        ([-1, 2, 0, 5], 3),
        ([-1, 2, 0, 5], 4),
        ([-1, 2, 0, 5], 5),
        ([-1, 2, 0, 5], 6),
    ]

    for test_case in test_cases:
        print("{} X ={:>2} ---> {}".format(test_case[0], test_case[1], get_range_sum_X(test_case[0], test_case[1])))


if __name__ == "__main__":
    main()
