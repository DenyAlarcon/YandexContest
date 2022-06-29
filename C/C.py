import math
import sys
import time
import timeit


def get_prime_numbers(limit=sys.maxsize // 10**12):
    if limit < 2:
        return []

    limit += 1  # Preincrement `limit` so sieve is inclusive, unlike `range`.
    primes = [True]*limit
    for base in range(2, int(limit**0.5 + 1)):
        if primes[base]:
            primes[base*2:limit:base] = [False]*(math.ceil(limit / base) - 2)

    primes[0] = primes[1] = False
    return (num for num, is_prime in enumerate(primes) if is_prime)


def get_max_gcd(A, B, prime_numbers):
    max_gcd = math.gcd(A, B)
    for prime_number in prime_numbers:
        current_gcd_A = math.gcd(A * prime_number, B)
        current_gcd_B = math.gcd(A, B * prime_number)
        if current_gcd_A > max_gcd:
            max_gcd = current_gcd_A
        if current_gcd_B > max_gcd:
            max_gcd = current_gcd_B
    return max_gcd


def main():
    tasks = []
    prime_numbers = get_prime_numbers()

    with open("C/input.txt") as f:
        T = int(f.readline())
        for _ in range(T):
            tasks.append(tuple(map(int, f.readline().split())))

    # with open("C/output.txt", "w") as f:
    #     for task in tasks:
    #         f.write("{0} ".format(get_max_gcd(
    #             task[0], task[1], prime_numbers)))

    for task in tasks:
        print("{0} ".format(get_max_gcd(task[0], task[1], prime_numbers)), end='')


if __name__ == "__main__":
    # start_time = time.time()
    # main()
    # elapsed_time = time.time() - start_time
    # print("Execution time: {:.3f} seconds".format(elapsed_time))

    elapsed_time = timeit.timeit(stmt="main()", globals=globals(), number=1)
    print("Execution time: {:.3f} seconds".format(elapsed_time))
