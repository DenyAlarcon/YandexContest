
def generate_parentheses(results, n, current_state, count_left, count_right):
    if count_left < n:
        generate_parentheses(results, n, current_state + "(", count_left + 1, count_right)
    if count_right < n and count_left > count_right:
        generate_parentheses(results, n, current_state + ")", count_left, count_right + 1)
    if len(current_state) == 2 * n:
        results.append(current_state)

def main():
    with open("D/input1.txt") as f:
        n = int(f.readline().strip())

    results = []
    generate_parentheses(results, n, "", 0, 0)

    with open("D/output1.txt", "w") as f:
        f.write("\n".join(results))


if __name__ == "__main__":
    main()
