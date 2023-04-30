# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# Rosalind allows  for a default error of 0.001 in all decimal answers unless otherwise stated; please see
# the note on absolute error below.
f = open('rosalind_gc (3).txt','r')
all_lines = f.readlines()
seqs = {}

seq_names = [] # empty list for sequence IDs to go into
for i in range (0,len(all_lines)):
    current = all_lines[i]
    if current.startswith('>'):
        current = all_lines[i]
        seqID = current[1:14]
        seqs[seqID] = ""
        seq_names.append(seqID)
        string = ""
    else:
        current = all_lines[i]
        string = string + current.strip('\n')
        seqs[seqID] = [string.strip('\n')]
# print(seqs)
# print(len(seqs))
# print(seq_names)
GC_info = {}
GC_max = []
for j in range (0,len(seq_names)):
    string_j = str(seqs[seq_names[j]])
    length_j = len(string_j) - 4 # minus 4 to remove the ' and [ ] characters that are in each entry
    x = string_j.count('C') + string_j.count('G')
    percent_GC = x * 100 / length_j
    GC_info[seq_names[j]] = percent_GC
key_list = list(GC_info.keys())
# print(key_list)
val_list = list(GC_info.values())
# print(val_list)
max_GC = max(val_list)
position = val_list.index(max_GC)
print(key_list[position])
print(max_GC)

