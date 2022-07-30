import sys

test_number = 4


def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        A, K, B, M, X = map(int, f.readline().strip().split())

    left = 1
    right = min((X * K) // A + 1, (X * M) // B + 1)
    while left < right:
        days = (left + right) // 2
        A_work_days = days - days // K
        B_work_days = days - days // M
        trees = A * A_work_days + B * B_work_days
        if trees < X:
            left = days + 1
        else:
            right = days
    
    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(str(left))


if __name__ == "__main__":
    main()
