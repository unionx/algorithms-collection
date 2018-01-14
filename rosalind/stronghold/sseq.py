from Bio import SeqIO


def find_spliced_motif(filename):
    dna_list = []
    for seq_record in SeqIO.parse(filename, "fasta"):
        dna_list.append(str(seq_record.seq))

    dna, motif = dna_list
    indices = []
    index = 0
    for char in motif:
        while dna[index] != char:
            index += 1
        index += 1
        indices.append(str(index))

    print(" ".join(indices))


if __name__ == "__main__":
    find_spliced_motif("./datasets/rosalind_sseq.txt")
