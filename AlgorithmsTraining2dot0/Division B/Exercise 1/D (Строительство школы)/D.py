def main():
    with open("D (Строительство школы)/input1.txt") as f:
        N = int(f.readline().strip())
        coordinates = list(map(int, f.readline().strip().split()))

    with open("D (Строительство школы)/output1.txt", "w") as f:
        f.write(str(coordinates[len(coordinates) // 2]))


if __name__ == "__main__":
    main()
