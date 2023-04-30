# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the
# symbols 'A', 'C', 'G', and 'T' occur in s.
f = open('rosalind_dna.txt','r')
DNA_string = f.read()
print(DNA_string)
noA = DNA_string.replace("A","")
noC = DNA_string.replace("C","")
noAG = noA.replace("G","")
noCG = noC.replace("G","")
noAC = noA.replace("C","")
T = noAG.replace("C","")
A = noCG.replace("T","")
C = noAG.replace("T","")
G = noAC.replace("T","")
print("A " + str(len(A)-1)) # you have to include the -1 because python starts count at 0!!
print("C " + str(len(C)-1))
print("G " + str(len(G)-1))
print("T " + str(len(T)-1))

