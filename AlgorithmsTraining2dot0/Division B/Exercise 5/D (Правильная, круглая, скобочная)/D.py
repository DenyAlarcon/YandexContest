import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f:
        parentheses = f.readline().strip()

    balance = 0
    result = "YES"
    for parenthesis in parentheses:
        if parenthesis == "(":
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            break
    
    if balance != 0:
        result = "NO"

    with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
