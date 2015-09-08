#!/usr/bin/env python3
from Bio.Data.CodonTable import standard_rna_table
from functools import reduce
import sys


modulo_base = 1000000


def make_multiple_backward_table():
    forward_table = standard_rna_table.forward_table
    backward_table = {}
    for k, v in forward_table.items():
        if v not in backward_table:
            backward_table[v] = [k]
        else:
            backward_table[v].append(k)

    return backward_table


def calc_modulo_of_two(x, y):
    acc = x * y
    if acc > modulo_base:
        acc = acc % 1


def calc_modulo(protein_seq):
    rna_backward_table = make_multiple_backward_table()
    location_probability = map(
        lambda p: len(rna_backward_table[p]), protein_seq)
    total_module = reduce(
        lambda x, y: (x * y) % modulo_base, location_probability)

    return total_module * 3 % modulo_base


if __name__ == "__main__":
    print(calc_modulo(sys.argv[1]))
