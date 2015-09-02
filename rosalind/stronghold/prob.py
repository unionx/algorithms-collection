#!/usr/bin/env python3

import math

dna_string = "TTCCGGGTGCTCCTTGACCTCCCCGGCGCCGCTTGAACTGTATTTTGCGTCACGCTATGAACTCTTGCGGTGAAAGCAGGTGACGAACGCGGATCTCGC"

gc_contents_string = "0.079 0.128 0.159 0.226 0.256 0.308 0.393 0.412 0.495 0.549 0.552 0.627 0.651 0.726 0.789 0.821 0.863 0.927"
gc_content_list = [float(x) for x in gc_contents_string.split(" ")]

result_list = []

for gc_content in gc_content_list:
    gc_rate = gc_content
    at_rate = 1 - gc_content

    total_rate = 1
    for c in dna_string:
        if c in ["A", "T"]:
            total_rate *= at_rate * 0.5
        else:
            total_rate *= gc_rate * 0.5

    result_list.append(math.log(total_rate, 10))

result_list = [str(round(x, 3)) for x in result_list]
print(" ".join(result_list))
