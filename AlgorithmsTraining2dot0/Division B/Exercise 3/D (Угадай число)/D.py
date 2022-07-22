import sys

test_number = 1

def main():
    with open(f"{sys.path[0]}/input{test_number}.txt") as f_r:
        n = int(f_r.readline().strip())
        results = set(range(1, n + 1))
        
        while True:
            question = f_r.readline().strip()
            if question == "HELP":
                with open(f"{sys.path[0]}/output{test_number}.txt", "w") as f_w:
                    f_w.write(" ".join(str(result) for result in sorted(results)))
                break
            question = set(map(int, question.split()))
            answer = f_r.readline().strip()
            if answer == "NO":
                results.difference_update(question)
            elif answer == "YES":
                results.intersection_update(question)
                    

if __name__ == "__main__":
    main()
