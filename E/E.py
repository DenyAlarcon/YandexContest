import sys
import timeit


def intersects(first_rect, second_rect):
    return not (
        first_rect[2] <= second_rect[0] or
        first_rect[0] >= second_rect[2] or
        first_rect[3] <= second_rect[1] or
        first_rect[1] >= second_rect[3]
    )


def main():
    input_number = 1
    with open(f"E/input{input_number}.txt") as f:
        n = int(f.readline())
    
    counts = [0] * n
    rects = []

    for _ in range(n):
        rects.append(tuple(map(int, sys.stdin.readline().split())))

    for i in range(n):
        for j in range(i + 1, n):
            if i != j and intersects(rects[i], rects[j]):
                counts[i] += 1
                counts[j] += 1

    with open(f"D/output{input_number}.txt", "w") as f:
        f.write(' '.join(map(str, counts)))


if __name__ == "__main__":
    elapsed_time = timeit.timeit(stmt='main()', globals=globals(), number=1)
    print("Execution time: {:.3f} seconds".format(elapsed_time))
