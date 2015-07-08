#!/usr/bin/env python3
from Bio import SeqIO
import sys


def find_longest_substr(string_list):
    substr = ""
    if len(string_list) > 1 and len(string_list[0]) > 0:
        for i in range(len(string_list[0])):
            for j in range(len(string_list[0])-i+1):
                if j > len(substr) and all(string_list[0][i:i+j] in x for x in string_list):
                    substr = string_list[0][i:i+j]
    return substr


def find_motif(filename):
    seq_list = map(lambda x: x.seq, SeqIO.parse(filename, "fasta"))
    return find_longest_substr(list(seq_list))


if __name__ == "__main__":
    print(find_motif(sys.argv[1]))
