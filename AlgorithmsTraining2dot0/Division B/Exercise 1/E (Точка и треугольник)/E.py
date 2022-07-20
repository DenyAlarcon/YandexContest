def main():
    with open("E (Точка и треугольник)/input4.txt") as f:
        d = int(f.readline().strip())
        x, y = map(int, f.readline().strip().split())

    result = 0
    if x + y > d or x < 0 or y < 0:
        distance_to_a = (x ** 2 + y ** 2) ** (1/2)
        distance_to_b = (abs(x ** 2 - d ** 2) + y ** 2) ** (1/2)
        distance_to_c = (x ** 2 + abs(y ** 2 - d ** 2)) ** (1/2)
        if distance_to_a <= distance_to_b and distance_to_a <= distance_to_c:
            result = 1
        elif distance_to_b < distance_to_a and distance_to_b <= distance_to_c:
            result = 2
        elif distance_to_c < distance_to_a and distance_to_c < distance_to_b:
            result = 3


    with open("E (Точка и треугольник)/output4.txt", "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    main()
