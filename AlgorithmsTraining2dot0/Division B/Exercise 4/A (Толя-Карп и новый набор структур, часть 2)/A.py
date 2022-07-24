import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        colors_values = {}
        n = int(f.readline().strip())
        for _ in range(n):
            a, d = map(int, f.readline().strip().split())
            if not a in colors_values:
                colors_values[a] = 0
            colors_values[a] += d
    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("\n".join(" ".join(str(x) for x in [color, value]) for color, value in sorted(colors_values.items())))


if __name__ == "__main__":
    main()
