def main():
    with open("E/input2.txt") as f:
        first_str = f.readline().strip()
        second_str = f.readline().strip()

    letters_dict = {}
    result = 1

    for letter in first_str:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

    for letter in second_str:
        if letter in letters_dict:
            if letters_dict[letter] == 0:
                result = 0
                break
            letters_dict[letter] -= 1
        else:
            result = 0
            break

    if result == 1 and sum(letters_dict.values()) != 0:
        result = 0

    with open("E/output2.txt", "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    main()
