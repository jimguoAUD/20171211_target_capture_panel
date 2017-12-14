import re
from sys import argv

fasta_file = argv[1]

def GC_content(seq):
    GC_count = 0
    seq = seq.upper()
    for nt in seq:
        if nt == "G" or nt == "C":
            GC_count+=1
    GC_content = GC_count/len(seq)*100
    return GC_content
        
#main
seq=''
with open (fasta_file, "r") as f:
    f.readline()
    for line in f:
        seq += line.strip()
print (len(seq))
sliding_window = 200
GC_content_across_seq=[]
if len(seq)>=sliding_window:
    for n in range(len(seq)-sliding_window):
        GC_content_across_seq.append(GC_content(seq[n:n+sliding_window]))
else:
    print ("sequence is shorter than 200 bases.")

import numpy as np
import matplotlib.pyplot as plt

width = 1
f=plt.figure(1)
plt.plot(GC_content_across_seq, color='blue')
plt.title("GC_content in the sequence")
plt.ylabel("%GC")
plt.xlabel("Position on the sequence")
f.savefig("GC_content in the sequence.pdf")
