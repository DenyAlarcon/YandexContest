import sys


def get_char(W_old, W_new):
    number = (W_old ^ W_new).bit_length() - 1
    if number == 26:
        return ' '
    return chr(number + 97)


def main():
    W = 0
    message = ""
    numbers_length = int(sys.stdin.readline())
    numbers = [0] + list(map(int, sys.stdin.readline().split()))

    for i in range(numbers_length):
        message += get_char(numbers[i], numbers[i+1])

    print(message)


if __name__ == "__main__":
    main()
