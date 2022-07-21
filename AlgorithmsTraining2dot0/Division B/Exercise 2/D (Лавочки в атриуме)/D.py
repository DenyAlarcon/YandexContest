import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        L, K = map(int, f.readline().strip().split())
        legs = list(map(int, f.readline().strip().split()))

    remainder = L % 2
    legs_mid_pos = L // 2
    result_legs = []

    for i in range(K):
        if legs[i] == legs_mid_pos:
            if remainder == 0:
                result_legs.append(legs[i-1])
            result_legs.append(legs[i])
            break
        elif legs[i] > legs_mid_pos:
            result_legs.append(legs[i-1])
            result_legs.append(legs[i])
            break

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(" ".join(str(result_leg) for result_leg in result_legs))


if __name__ == "__main__":
    main()
