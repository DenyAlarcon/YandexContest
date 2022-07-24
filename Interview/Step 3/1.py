# Нужно в массиве целых чисел вытолкнуть нули вверх, сохранив последовательность (удалить нули из массива). CPU: O(n), Memory O(1).

# [0, 0, 0, 1] -> [1, 0, 0, 0]
# [0, 0, 1, 2] -> [1, 2, 0, 0]
# [0, 1, 0, 2] -> [1, 2, 0, 0]
# [0, 1, 2, 0] -> [1, 2, 0, 0]
# [0, 0, 0, 0] -> [0, 0, 0, 0]
# [1, 0, 0, 0] -> [1, 0, 0, 0]
# [1, 0, 0, 2] -> [1, 2, 0, 0]
# [1, 0, 2, 0] -> [1, 2, 0, 0]

def push_zeros(numbers):
    result_numbers = numbers.copy()
    idx_zero = -1
    for i in range(len(result_numbers)):
        if result_numbers[i] == 0:
            if idx_zero == -1:
                idx_zero = i
        else:
            if i > idx_zero and idx_zero != -1:
                result_numbers[idx_zero], result_numbers[i] = result_numbers[i], result_numbers[idx_zero]
                idx_zero += 1
    return result_numbers


def main():
    test_cases = [
        [0, 0, 0, 1],
        [0, 0, 1, 2],
        [0, 1, 0, 2],
        [0, 1, 2, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 2],
        [1, 0, 2, 0]
    ]

    for test_case in test_cases:
        print(test_case, "->", push_zeros(test_case))


if __name__ == "__main__":
    main()
