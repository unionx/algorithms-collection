#!/usr/bin/env python3

s1 = "TCTAGTTTGATCACGCCGAACGTTCCGGGTAATGTTAACTGTCGGCTCATTATATACGGCACTAAGCAAAGGTGTTCATCCCTGATCGGGCCTTGGTGGCACAGGTAGAAATTACGGCCCCTAAGATAGTTACAGCCCCTAAAACAGGACAGCTGAACAGATAAAAAATCACATAAAGGTCTAAATAACTTCTTCTGCCTGAATTGACGCGAGCCCCTGAGCACTTATAATGACCAGTGGTGATGTCCCCCTGGATCGCGTCCCACCAAATCCTCGCCACCGAATGCCTTTAGTCCTAAAAGAAGGGAGCCGGTGAAGTGTAGCTACCAAGGGCGTGAACGGCACGCTTAGCGGGTGGTGAGCAGAAATAGCCACCTTCCTCCTGGCTGGTCACGTAGCGGAGTGATGGGCTGCAAGGATGGGCAAGTTCGGGAAACACGAGGCGGCGCACTGAGAGGACTACTGAGCCGGAATGGTGAATCTCGAGCATGAATAGATCTGCGGGACAATATTGGGACTCTGCCCCAGCCTTTGCCGAGCCTGAGACCCTGGATAGTATGGCGAAAGTTTACAGACGCAATCTCCGAGGTCACCGGAGGCAATATAGCTTATGCACGATCTTCTAGAGCCGGGTTTTTGGCACGACTGATGAGTGCGCGTTATATGCTAGCCCTGGAAGATCATCAATTTTAATGATGCGCCAGAGTAGCGCTGCCGGCCTTTGTTATCATTGCGGGTGAAGACTAAGATGATTTCTTTTCCTTTATTACGTTTTAGGTCGCCTCTCAGGTCTCACTCTTCATTATTAGGGTCGCCTTATACTGATCATTAAAACTGGCCCACTACGGCGATATGTCTCATATCATCAGAAACATTACGACAAAACCGAAGTGAAGTGGAGACTGGAAAGGTCTGAGTGGTGTCATGGATGCTACGAGAGCCTTGAGCGAGCTCGAGACGTGGTCCGTTAAGGCAAC"
s2 = "GCTCGTGTTCCCATACCTAATATTACCTCCGTTCTCGCACCTAGGTTCTTAGGATACTTCTCTTATCATACGTCGTCATCCCGGCTCCCGGCTTAGGATCAAAGGGAATATGTAGGGACGTAAGTCAGATTAGAGCCCCTGCAAGACTACAGCAGAGACCATTAAAATCGGGATGTAGGTATATACTATTTTGTGGGCCGCACCTTTCTAACGCCTGTTATTGGTTATTACTATCACTATTGGTGGGCCGCTGGATCAACTCCGCGAACCTCCTGCCCAACGAATCACATCACTGTAAACTGAAGAGGCCGGCGCATGGGTTATTACCAAGAGGTCCCAGTCGGACCAAAGCTGCGGCTGCGCAATATTTTACGACAACCTGCTCGGTGGCCACATTACCCCGCCCTGGAGTTTTGGGGCGCAGCACTGCGAACACCCTCACATGGGGGATTGAAGGGTCCGCGCTACTGGCCCGGGCTATCCCAAGTGGAACTGAGGCTTCCCTACCGTATCTGGAAGCCACCTGGAGCGTAGCCCAGTCCGCGCGTAAGCATAGCAGTGACCCCGTGCTAAGTGGTTAACTTTCACGTAATGATAGGCCTAATTGCGTATGCACGCTCATGTACGGGCATCTTTTACACGTCCCCAGTCCGAGCAATTAATACGCTAGCCGACGAACATTTTTAACGGTCCGAAGAGCCCACTATATATACCGATGACTTGTTGAACATGATGATCGGAGATTAAAACTAATATCGACCTTCTAACAGTTTATACGGCGCCTGATTATCACGACGCTACGTTATGAGGGTCCGCTCAGTGGTACAGGTAAAATTGGCTGCCCATGGCAAGTTATCGTCACTGTTTTGTTACGGGCCCCCAGATCCGAAAGGAGTTGGATACACGCTCGGGCTAACTTTGAACTCAGAGGCATCCACCCCCAGGGGATCGACACATCGATGGTCTGTTCAGACTCC"

def is_not_same(c1, c2):
    if c1 != c2:
        return 1
    else:
        return 0

l = list(map(lambda c1, c2: is_not_same(c1, c2), s1, s2))
print(sum(l))
