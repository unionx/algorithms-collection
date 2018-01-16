#!/usr/bin/env python3
import sys
from Bio import SeqIO

threshold = int(sys.argv[2])    # 17
count = 0

for record in SeqIO.parse(open(sys.argv[1], "rU"), "fastq"):
    seq = record.letter_annotations["phred_quality"]
    mean_quality = float(sum(seq)) / len(seq)
    if mean_quality < threshold:
        count += 1

print(count)
