#!/usr/bin/env python3

from Bio import SeqIO

def read_fasta_file_wrong():
    with open("./cons-data.fasta", "r") as f:
        lines = f.readlines()
        lines = [l[:-1] for l in lines if not l.startswith(">")]
        lines = [list(l) for l in lines]
        return lines

def read_fasta_file():
    lines = []
    for seq_record in SeqIO.parse("./cons-data.fasta", "fasta"):
        lines.append(str(seq_record.seq))
    return lines

def calc_profile_matrix(dna_matrix):
    profile_matrix = {
        "A": [],
        "C": [],
        "G": [],
        "T": []
    }

    length = len(dna_matrix[0])
    for i in range(0, length):
        column_chars = [c[i] for c in dna_matrix]

        for this_char in ["A", "T", "C", "G"]:
            count_char = len([c for c in column_chars if c == this_char])
            profile_matrix[this_char].append(count_char)

    return profile_matrix

def calc_consensus_string(profile_matrix):
    length = len(profile_matrix["A"])
    consensus_string = ""

    for i in range(0, length):
        this_key = ""
        this_val = 0
        for this_char in ["A", "C", "G", "T"]:
            val = profile_matrix[this_char][i]
            if val > this_val:
                this_key = this_char
                this_val = val
        consensus_string += this_key

    return consensus_string

dna_matrix = read_fasta_file()
profile_matrix = calc_profile_matrix(dna_matrix)
consensus_string = calc_consensus_string(profile_matrix)

print(consensus_string)
for this_char in ["A", "C", "G", "T"]:
    print(this_char + ": " + " ".join([str(c) for c in profile_matrix[this_char]]))
