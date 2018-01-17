from Bio.Seq import translate

table_codes = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23]
dna, protein = open('./datasets/rosalind_ptra.txt').read().strip().split('\n')


for i in table_codes:
    trans = translate(dna, table=i, stop_symbol="")
    if protein == str(trans):
        print(i)
        break
