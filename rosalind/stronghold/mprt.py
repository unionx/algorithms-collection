#!/usr/bin/env python3
import regex as re
import sys
import urllib.request


def find_N_glycosylation(protein_seq):
    find_results = re.finditer(r"N[^P][ST][^P]", protein_seq, overlapped=True)
    for result in find_results:
        yield str(result.start() + 1)


def read_uniport(protein, from_network=True):
    if from_network:
        url = "http://www.uniprot.org/uniprot/" + protein + ".fasta"
        handle = urllib.request.urlopen(url)
        result = handle.read().decode("UTF8")
    else:
        result = protein

    return "".join(result.split("\n")[1:])


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        protein_names = f.readlines()
        for protein in protein_names:
            protein = protein.rstrip()
            seq = read_uniport(protein, from_network=True)
            result = list(find_N_glycosylation(seq))

            if len(result) != 0:
                print(protein)
                print(" ".join(result))
