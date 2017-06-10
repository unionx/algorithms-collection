#!/usr/bin/env python3
import sys
from Bio import SeqIO

def calc_ratio(seq_list):
    seq0 = seq_list[0]
    seq1 = seq_list[1]

    transition_cnt = 0
    transverstion_cnt = 0

    is_transition = lambda x, y: {x, y} in [{'A', 'G'}, {'C', 'T'}]
    is_transversion = lambda x, y: not is_transition(x, y)

    for i, c0 in enumerate(seq0):
        c1 = seq1[i]
        if c0 != c1:
            if is_transition(c0, c1):
                transition_cnt += 1
            if is_transversion(c0, c1):
                transverstion_cnt += 1

    print(transition_cnt)
    print(transverstion_cnt)
    print(transition_cnt/transverstion_cnt)

if __name__ == '__main__':
    seq_list = []
    filename = sys.argv[1]
    for seq_record in SeqIO.parse(filename, 'fasta'):
        seq_list.append(seq_record.seq)

    calc_ratio(seq_list)