from Bio import SeqIO

reverse_dict = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

def reverse_dna(dna):
    dna = dna[::-1]
    dna_reversed = [ reverse_dict[c] for c in dna ]
    return "".join(dna_reversed)

count = 0

with open("./datasets/rosalind_rvco.txt") as f:
    for fasta in SeqIO.parse(f, "fasta"):
        ss = fasta.seq
        if reverse_dna(ss) == ss:
            count += 1

print(count)
