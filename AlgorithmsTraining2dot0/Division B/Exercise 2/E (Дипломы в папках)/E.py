from itertools import count
import sys

test_number = 2

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        N = int(f.readline().strip())
        folders_counts = list(map(int, f.readline().strip().split()))

    count_seconds = 0
    max_folder_count = 0

    for folder_count in folders_counts:
        if folder_count > max_folder_count:
            max_folder_count = folder_count
        count_seconds += folder_count

    count_seconds -= max_folder_count

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(str(count_seconds))


if __name__ == "__main__":
    main()
