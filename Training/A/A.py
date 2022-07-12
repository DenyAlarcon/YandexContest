def main():
    with open("A/input.txt") as f:
        J = f.readline().strip()
        S = f.readline().strip()

    count = 0
    for s in S:
        if s in J:
            count += 1

    with open("A/output.txt", "w") as f:
        f.write(str(count))


if __name__ == "__main__":
    main()
