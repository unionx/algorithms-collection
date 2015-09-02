#!/usr/bin/env python3
from Bio import SeqIO
import sys

n = 3

def count_overlap(filename):
    for seq_record in SeqIO.parse(filename, "fasta"):
        for seq_record_1 in SeqIO.parse(filename, "fasta"):
            s1 = seq_record.seq
            s2 = seq_record_1.seq
            if s1 != s2 and s1[-3:] == s2[0:3]:
                print(seq_record.id + " " + seq_record_1.id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Wrong argument number.")

    count_overlap(sys.argv[1])
