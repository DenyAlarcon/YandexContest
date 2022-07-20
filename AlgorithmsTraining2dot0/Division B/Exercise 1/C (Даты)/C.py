def main():
    with open("C (Даты)/input2.txt") as f:
        x, y, z = map(int, f.readline().strip().split())

    result = 1
    if x < 13 and y < 13 and x != y:
        result = 0


    with open("C (Даты)/output2.txt", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
