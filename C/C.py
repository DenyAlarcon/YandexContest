import sys
import math


def get_prime_numbers():
    prime_numbers = [2]
    for i in range(3, 1000000, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in prime_numbers:
            if j*j - 1 > i:
                prime_numbers.append(i)
                break
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers


def get_max_gcd(A, B):
    max_gcd = math.gcd(A, B)
    for prime_number in get_prime_numbers():
        current_gcd_A = math.gcd(A * prime_number, B)
        current_gcd_B = math.gcd(A, B * prime_number)
        if current_gcd_A > max_gcd:
            max_gcd = current_gcd_A
        if current_gcd_B > max_gcd:
            max_gcd = current_gcd_B
    return max_gcd


def main():
    T = int(sys.stdin.readline())
    tasks = []

    for _ in range(T):
        tasks.append(tuple(map(int, sys.stdin.readline().split())))

    for task in tasks:
        print(get_max_gcd(task[0], task[1]))


if __name__ == "__main__":
    main()
