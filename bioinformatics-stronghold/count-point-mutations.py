# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t). the Hamming distance between s and t, denoted dH(s,t), is the number
# of corresponding symbols that differ in s and t
f = open('rosalind_hamm.txt', "r")
seq1 = f.readline()
seq2 = f.readline()
seq1.strip('\n')
seq2.strip('\n')
# print(seq1)
# print(seq2)
length = len(seq1)
dH = 0
for l in range (0,(length-1)):
    if seq1[l] == seq2[l]:
        dH = dH + 0
    else:
        dH = dH + 1
print(dH)