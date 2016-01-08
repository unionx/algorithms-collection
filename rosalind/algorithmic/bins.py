#!/usr/bin/env python3
import sys
import bisect

def read_data():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines = f.readlines()
        sorted_list = list(map(lambda x: int(x), lines[2].rstrip().split(" ")))
        random_list = list(map(lambda x: int(x), lines[3].rstrip().split(" ")))

    return sorted_list, random_list

def seach():
    sorted_list, random_list = read_data()
    result_list = []
    max_len = len(sorted_list)

    for x in random_list:
        index = bisect.bisect(sorted_list, x)
        if sorted_list[index-1] != x:
            index = -1
        result_list.append(index)

    print(' '.join(str(x) for x in result_list))

seach()
