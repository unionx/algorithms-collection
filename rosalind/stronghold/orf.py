import warnings
from Bio import SeqIO, BiopythonWarning
from Bio.Data import CodonTable

warnings.simplefilter("ignore", BiopythonWarning)
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
stop_codons = standard_table.stop_codons


def chunker(seq, size):
    return [seq[i:i+size] for i in range(0, len(seq), size)]


def trans_orf(record):
    proteins = set()
    for strand in [record, record.reverse_complement()]:
        for start_index in range(len(strand)-2):
            start_codon = str(strand[start_index:start_index+3])
            if start_codon == "ATG":
                frame = strand[start_index:]
                if any(st in chunker(frame[3:], 3) for st in stop_codons):
                    protein = str(strand[start_index:].translate(to_stop=True))
                    proteins.add(protein)
    return proteins


if __name__ == "__main__":
    with open("./datasets/rosalind_orf.txt", "r") as f:
        record = SeqIO.read(f, "fasta").seq

    for protein in trans_orf(record):
        print(protein)
