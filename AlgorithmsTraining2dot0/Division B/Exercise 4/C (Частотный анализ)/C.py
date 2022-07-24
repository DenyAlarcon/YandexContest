import sys

test_number = 3

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        lines = f.readlines()

    words_counts = {}
    for line in lines:
        words = line.strip().split()
        for word in words:
            if word not in words_counts:
                words_counts[word] = 0
            words_counts[word] += 1

    words_count_list = []
    for word, count in words_counts.items():
        words_count_list.append((count, word))
    words_count_list.sort(key=lambda x: (-x[0], x[1]))

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("\n".join(word for (_, word) in words_count_list))

if __name__ == "__main__":
    main()
