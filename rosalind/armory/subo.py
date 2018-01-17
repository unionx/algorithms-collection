import distance
from Bio import SeqIO

with open("./datasets/rosalind_subo.txt") as f:
    s1, s2 = [fasta.seq for fasta in SeqIO.parse(f, "fasta")]

# pick the 100% and shortest(>32bp)
ss = "TGCGCCTGGAATGCATTAGGACCCTTGCAGTG"


def find_ss(s):
    count = 0
    len_ss = len(ss)
    for i in range(len(s)-len_ss):
        if distance.hamming(s[i:i+len_ss], ss) <= 3:
            count += 1
    print(count)


find_ss(s1)
find_ss(s2)
