import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        word = f.readline().strip()

    word_len = len(word)
    remainder = word_len % 2
    word_mid_pos = word_len // 2
    count_different_letters = 0

    for i in range(word_mid_pos):
        if word[word_mid_pos - i - 1] != word[word_mid_pos + i + remainder]:
            count_different_letters += 1


    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(str(count_different_letters))

if __name__ == "__main__":
    main()
