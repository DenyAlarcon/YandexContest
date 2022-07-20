def main():
    with open("A (Interactor)/input6.txt") as f:
        r = int(f.readline().strip()) # код завершения задачи
        i = int(f.readline().strip()) # интерактор
        c = int(f.readline().strip()) # чекер

    result = i

    if i == 0:
        if r != 0:
            result = 3
        else:
            result = c
    elif i == 1:
        result = c
    elif i == 4:
        if r != 0:
            result = 3
        else:
            result = 4
    elif i == 6:
        result = 0
    elif i == 7:
        result = 1

    with open("A (Interactor)/output6.txt", "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    main()
