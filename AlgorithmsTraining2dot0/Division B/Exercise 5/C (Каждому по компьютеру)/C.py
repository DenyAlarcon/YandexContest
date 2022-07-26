import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        N, M = map(int, f.readline().strip().split())
        groups = list(map(int, f.readline().strip().split())) # группы
        classrooms = list(map(int, f.readline().strip().split())) # аудитории

    groups_dict = dict(zip(range(1, N + 1), groups))
    groups_dict = dict(sorted(groups_dict.items(), key=lambda item: -item[1]))
    classrooms_dict = dict(zip(range(1, M + 1), classrooms))
    classrooms_dict = dict(sorted(classrooms_dict.items(), key=lambda item: -item[1]))

    result = [0] * (N + 1)
    classrooms_keys = list(classrooms_dict.keys())
    classroom_idx = 0
    for group_idx in groups_dict.keys():
        if groups_dict[group_idx] + 1 <= classrooms_dict[classrooms_keys[classroom_idx]]:
            result[0] += 1
            result[group_idx] = classrooms_keys[classroom_idx]
            classroom_idx += 1

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write("\n".join((str(result[0]), " ".join(map(str, result[1:])))))


if __name__ == "__main__":
    main()
