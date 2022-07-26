import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        n, q = map(int, f.readline().strip().split())
        numbers = list(map(int, f.readline().strip().split()))
        numbers_sums = [0] * (n + 1)
        for i in range(n):
            numbers_sums[i + 1] += numbers[i] + numbers_sums[i]

        answers = [0] * q  
        for i in range(q):
            left_idx, right_idx = map(int, f.readline().strip().split())
            answers[i] = numbers_sums[right_idx] - numbers_sums[left_idx - 1]


    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("\n".join(map(str, answers)))


if __name__ == "__main__":
    main()
