import sys

test_number = 3

def main():
    MAX_SEATS = 450
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        lines = f.readlines()
  
    consignments_votes = {}
    for line in lines:
        consigment, vote = line.strip().rsplit(" ", 1)
        consignments_votes[consigment] = int(vote)

    first_electoral_qoutient = sum(consignments_votes.values()) / MAX_SEATS
    sum_seats = 0

    consignments_seats = {}
    consignments_remainders = {}
    for consigment in consignments_votes:
        seats = int(consignments_votes[consigment] // first_electoral_qoutient)
        remainder = consignments_votes[consigment] % first_electoral_qoutient
        consignments_seats[consigment] = seats
        consignments_remainders[consigment] = remainder
        sum_seats += seats

    empty_seats = MAX_SEATS - sum_seats

    if empty_seats:
        for consigment in dict(sorted(consignments_remainders.items(), key=lambda item: -item[1])):
            consignments_seats[consigment] += 1
            empty_seats -= 1
            if not empty_seats:
                break

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("\n".join(" ".join((consigment, str(seats))) for consigment, seats in consignments_seats.items()))


if __name__ == "__main__":
    main()
