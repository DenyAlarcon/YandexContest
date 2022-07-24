import sys

test_number = 3

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        lines = f.readlines()

    votes = {}
    for line in lines:
        surname, num_votes = line.strip().split()
        num_votes = int(num_votes)

        if surname not in votes:
            votes[surname] = 0
        votes[surname] += num_votes
            
    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("\n".join(" ".join(str(x) for x in [surname, num_votes]) for surname, num_votes in sorted(votes.items())))


if __name__ == "__main__":
    main()
