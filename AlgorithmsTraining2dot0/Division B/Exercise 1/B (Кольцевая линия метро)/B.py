def main():
    with open("B (Кольцевая линия метро)/input1.txt") as f:
        N, i, j = map(int, f.readline().strip().split())

    result = 0
    abs_diff = abs(i - j)
    if abs_diff >= N / 2:
        result = N - abs_diff - 1
    else:
        result = abs_diff - 1


    with open("B (Кольцевая линия метро)/output1.txt", "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    main()
