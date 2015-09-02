#!/usr/bin/env python3
import sys


def n_in_m(n, m):
    assert n <= m

    count_m = 1
    count_n = 1
    lst = range(0, n)
    for i in lst:
        count_m *= m
        count_n *= n
        m -= 1
        n -= 1
    return int(count_m / count_n)


def n_rate(k, n):
    total = 2 ** k
    total_rate = 0

    for i in range(n, total+1):
        total_rate += 0.25 ** i * 0.75 ** (total - i) * n_in_m(i, total)

    return total_rate


if __name__ == "__main__":
    k, n = int(sys.argv[1]), int(sys.argv[2])
    print(n_rate(k, n))
