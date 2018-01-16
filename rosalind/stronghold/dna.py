#!/usr/bin/env python3

s = "TCGTGCAGTGCACATTCGATTCTGGTGCCGCTGACCAACCAATGGGAGCGTTCCATGTATAATGGAAAGTGACGTACTTATGTCCAGCCCAGTCGCCGACGTCGATACCATGCTATTTGGTGTATAGCGACAGCCTGTGATTGAGATGGCAATTGTAAGTCCTAAGTCACAGGGCACAGAGTAAACGGCAAGCAAAGCGTGCCAGGACCGTACGTGCTGAATTTATTTCATCATTAAGTTAATATCATAGTGCAGTTCCTGAATTTTCGTTTACAGGTGGACGCCTTAGGCATCCGGGGCAGAGGGAAGGTCTCTATCCACCTTTAGCACCGTTCTTCGACAGACGACATTAGCTGTCGTTCTTACGTTTGGAGTTGAAGTACTGAAGTGGAGGATTCCACACATACAAGTTTGCCCACCAATCAGAAAGTCATAGTCGCGCGGTCACAGTACCTTGGAGACATCGCGGCATTTTCGCAGCCTTGGGGCTCTTCATGTCACGTGTGCAAGCTGCCCCATATCTCGGGGGGGGTCGCTCCGTTATGCTCACTTAGAAGGCAAAAATTGGATCTCTGGTGCGAACGGGTCAAGGACCCAGACTAAACATGACTAACACCTGTGGCCGGATCATACGTAAAAGGGAGAAGCTCCTCGTCCAGCATGCGATGGTAGCCCGACGCTGGCCCACATGGAATGGAATACCAGCCTTATCCTTGTGAGAGGAAGCGCACGAGCTCAGACGAGCCCCTGCTAAACGGTTTCGGCTCTAGTTTTCACATCTCGTTAAAGAATGCCAAAACAGTTTTAACAAGGAGTGGGCGCGGGCCCTCCTATATGGGATAGATAACATAGCTTGCCGCCCGCCACACCCCAGACTGCCACCTGCGGCACGGGAACCTTTACCTCAGTACGTACAACCTGGACTGTTCTTTCCTTGATGGAGGCACTGGGGTTCGCGGAGCCTAGGAATTCGT"

def count_atcg(s):
    count_result = {
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0
    }

    for c in s:
        count_result[c] += 1

    return count_result


if __name__ == "__main__":
    res = count_atcg(s)
    print(str(res["A"]) + " " +
          str(res["C"]) + " " +
          str(res["G"]) + " " +
          str(res["T"]) + " ")
