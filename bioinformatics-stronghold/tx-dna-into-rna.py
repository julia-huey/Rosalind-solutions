# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t
f = open("rosalind_rna.txt", "r")
DNA_seq = f.read()
print(DNA_seq)
RNA_seq = DNA_seq.replace("T", "U")
print(RNA_seq)
# below code returns the RNA complement
# f = open("filename.txt", "r")
# DNA_seq = f.read()
# print(DNA_seq)
# print(len(DNA_seq))
# DNA_list = list(DNA_seq)
# for x in range(0, len(DNA_seq)):
#     if DNA_list[x] == "A":
#         DNA_list[x] = "T"
#     else:
#         if DNA_list[x] == "C":
#             DNA_list[x] = "G"
#         else:
#             if DNA_list[x] == "G":
#                 DNA_list[x] = "C"
#             else: DNA_list[x] ="U"
#     x = x + 1
# DNA_str = "".join(DNA_list)
# print(DNA_str)