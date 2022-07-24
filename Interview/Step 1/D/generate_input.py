import random


def main():
    numbers = [random.randrange(0, 2) for _ in range(10**6)]

    with open("D/input7.txt", "w") as f:
        f.write(str(len(numbers)) + "\n")
        f.write("".join(map(str, numbers)))


if __name__ == "__main__":
    main()
