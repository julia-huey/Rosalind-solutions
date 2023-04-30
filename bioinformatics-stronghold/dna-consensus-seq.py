# # finding most likely common ancestor
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#
# Return: A consensus string and profile matrix for the collection. (If several possible consensus
# strings exist, then you may return any one of them.)
f = open("rosalind_cons (1).txt","r")
lines = f.readlines() # stores each line of file as item in list 'lines'
line2 = lines[1] # stores second line of file as line2
d = 0
for i in range(0,len(lines)):
    string = lines[i]
    seq = ""
    if string[0] == ">":
        d = d + 1
    else:
        d = d
# returns variable 'd' equal to the number of unique strings in txt document
string_list = []
for i in range (1,len(lines)):
    string2 = lines[i]
    string3 = string2[0:(len(string2)-2)]
    if string2[0] == ">":
        string_list.append(seq)
        seq = ""
    else:
        seq = seq + string3
print(string_list)
n = len(seq)
print(n)
As = "A:"
Cs = "C:"
Gs = "G:"
Ts = "T:"
listA = []
listC = []
listG = []
listT = []
for i in range (0,n):
    A = 0
    C = 0
    G = 0
    T = 0
    for j in range(0, len(string_list)):  # for each line in the source file 'f'
        line_j = string_list[j]
        if line_j[i] == "A":
            A = A + 1
        else:
            if line_j[i] == "C":
                C = C + 1
            else:
                if line_j[i] == "G":
                    G = G + 1
                else:
                    T = T + 1
    As = As + " " + str(A)
    Cs = Cs + " " + str(C)
    Gs = Gs + " " + str(G)
    Ts = Ts + " " + str(T)
    listA.append(A)
    listC.append(C)
    listG.append(G)
    listT.append(T)
consensus = ""
for i in range (0,n):
    curr_base = []
    curr_base.append(listA[i])
    curr_base.append(listC[i])
    curr_base.append(listG[i])
    curr_base.append(listT[i])
    max_base = max(curr_base)
    if max_base == listA[i]:
        consensus = consensus + "A"
    else:
        if max_base == listC[i]:
            consensus = consensus + "C"
        else:
            if max_base == listG[i]:
                consensus = consensus + "G"
            else:
                consensus = consensus + "T"
print(consensus)
print(As)
print(Cs)
print(Gs)
print(Ts)