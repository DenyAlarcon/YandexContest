def main():
    numbers = []
    with open("B/input.txt") as f:
        n = int(f.readline().strip())
        for _ in range(n):
            numbers.append(int(f.readline().strip()))

    max_length = 0
    current_length = 0
    for number in numbers:
        if number == 1:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    if current_length > max_length:
        max_length = current_length

    with open("B/output.txt", "w") as f:
        f.write(str(max_length))


if __name__ == "__main__":
    main()
