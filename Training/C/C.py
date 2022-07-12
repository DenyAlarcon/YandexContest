def main():
    old_number = None
    with open("C/input1.txt") as fr, open("C/output1.txt", "w") as fw:
        n = int(fr.readline().strip())
        for _ in range(n):
            number = int(fr.readline().strip())
            if number != old_number:
                if old_number == None:
                    fw.write(str(number))
                else:
                    fw.write("\n" + str(number))
            old_number = number

if __name__ == "__main__":
    main()
