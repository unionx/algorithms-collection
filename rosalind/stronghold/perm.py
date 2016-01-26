#!/usr/bin/env python3
import sys

n = int(sys.argv[1])
number_list = range(1, n+1)


def acc_perm(result_list, x):
    if x == 0:
        return result_list

    new_result_list = []
    for result in result_list:
        for number in number_list:
            if number not in result:
                new_result_list.append(result + [number])

    return acc_perm(new_result_list, x-1)


all_result = acc_perm([[]], n)
print(len(all_result))
for one_result in all_result:
    print(' '.join([str(i) for i in one_result]))
