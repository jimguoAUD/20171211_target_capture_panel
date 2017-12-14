
from sys import argv
import numpy as np
import re

fasta_file = argv[1]
seq=""
with open (fasta_file, "r") as f:
    f.readline()
    for line in f:
        seq += line.strip()
#print (seq)
homo_ls = []
mer_100 = [100*"A", 100*"C", 100*"G", 100*"T"]
homo_mer_count, A_dic,C_dic,G_dic,T_dic = ({} for i in range (5))

for mer in mer_100:
    if re.search(mer.upper(), seq.upper()):
        print ("Target sequence contain more than 100 %s, need to increase the length of starting homopolymer." %mer[0])
        exit()
    #print (mer)
for n in range (2,101):
    homo_ls.append(n*"A")
    homo_ls.append(n*"C")
    homo_ls.append(n*"G")
    homo_ls.append(n*"T")
for homo_mer in sorted (homo_ls, reverse = True):
    # print (homo_mer)
    if re.search (homo_mer.upper(),seq.upper()):
        # print("match found!")
        #print(homo_mer.upper())
        matches = re.finditer(homo_mer.upper(),seq.upper())
        homo_mer_count[homo_mer.upper()] = 0
        for match in matches:
            new_seq = seq[:match.start()]+len(match.group(0))*"N"+seq[match.end():]
            seq = new_seq
            #print (seq)
            homo_mer_count[homo_mer.upper()] +=1
        
for key, value in homo_mer_count.items():
    print (key, value)
    if re.search("A", key):
        A_dic[len(key)]=np.log10(value)
    elif re.search("C", key):
        C_dic[len(key)]=np.log10(value)
    elif re.search("G", key):
        G_dic[len(key)]=np.log10(value)
    elif re.search("T", key):
        T_dic[len(key)]=np.log10(value)

import numpy as np
import matplotlib.pyplot as plt

width = 1
f=plt.figure()
#f.set_xticks(list(A_dic.keys()))
plt.bar(list(A_dic.keys()), A_dic.values(), color='r')
plt.title("Distribubtion of A homopolymers in the sequence")
plt.ylabel("log10(Occurence)")
plt.xlabel("length of A homopolyer")
#plt.show()
f.savefig("Distribubtion of A homopolymers.pdf")


f=plt.figure()
# ax.set_xticks(list(C_dic.keys()))
plt.bar(list(C_dic.keys()), C_dic.values(), color='g')
plt.title("Distribubtion of C homopolymers in the sequence")
plt.ylabel("log10(Occurence)")
plt.xlabel("length of C homopolyer")
#plt.show()
plt.savefig("Distribubtion of C homopolymers.pdf")


f=plt.figure()
#ax.set_xticks(list(G_dic.keys()))
plt.bar(list(G_dic.keys()), G_dic.values(), color='b')
plt.title("Distribubtion of G homopolymers in the sequence")
plt.ylabel("log10(Occurence)")
plt.xlabel("length of G homopolyer")
#plt.show()
plt.savefig("Distribubtion of G homopolymers.pdf")


f=plt.figure()
#ax.set_xticks(list(T_dic.keys()))
plt.bar(list(T_dic.keys()), T_dic.values(), color='y')
plt.title("Distribubtion of T homopolymers in the sequence")
plt.ylabel("log10(Occurence)")
plt.xlabel("length of T homopolyer")
#plt.show()
plt.savefig("Distribubtion of T homopolymers.pdf")

    