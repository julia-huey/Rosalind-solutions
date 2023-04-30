# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#
# Return: The protein string encoded by s.
mRNA = "AUGAACCUUUCAAACAACACUUUAUUAAAACAUACUGCUAUUGCGGUUACCUGGUCGCCGAAGGGCUGCGGUCUGCAGUUACACCCGAACCUACCUAAAGUCUUCUUUCUAGUUACCGCUACGCUGUCGAAGGUGUUUACACCAGGUGCCGCGAGCGUGCUUCCUAGGAGGCAUCGCUAUCAUCGACAUCUCCGGGCGGCGUGGGUCCGAAUCUCAACAUGUGACACUCCUAGCACGCCCUUCCCUUCUCUCCCCGCCUUAUUCCGCGUUCUGGCACACACAUACGGCGUGGUAUCGACGGAGACCGGACACACGGUCAACCUCAAGUCGCCAGUUAGAAUCGCUCGCUACAACAUUUCCGGGGAAUACCUGGCAUUAUCGUCAGUACCAGAUAAGAUUAACCGAAUCGACAUGUAUUCACAGGUCCCCCCUAGUACCACUGGACUCCAAUGGAUCGAAUUCGAGAAAUCAUACUGUUCGGUGAGAGCUGCGGCAGGUCCGGCCAUAGGUGCACAGCCGCUUACUGUGGGUCGGCUACGAACUGUAAGUCGCACCCAUCAACGAUCGCUUGAGCCAGGUCUUGGCAUUGAGAGUUUUGCCAGAGCCUGGGCGGUGGCAAAAUUGGUCACACCUUGCACGAGAUUUGCUGUAGCCCAAAGUCCCCAGGUUUCAUCAGAUGAACGACAAUCCCUUCCAGGCUUUCCCGGCCAAGUACGAAUCUUUUGCUCUAUAAGUCACGCCAAUCUUGACCCAUGCUCCGACGGUAAGGAUGGGGUACGCCCCGGAGUUCCCAAGCGGUACCGGCCACUCUUACGAGUGCCUCCCUCAGAGGAUGCGUCCAGAGACCCAACGCACAGACUAGCUCAUUUCUGCGUGCGGAACUAUAAGGUACAACUUAGCUUAUCGGGUCUCGUAGAAAUAUGGUUAUGCACGAGCGGGCCGAGCUUCCCAUUUAGCCCAUAUCUUCUCUUUAUCCCUUGCGGCAGACAAUGGAAUGGUACAUUCAUCCGACUCACCAAUCUAAAUAACUCAACACGGGCCAUGUUCUUCCCCGUAGAAUUAAAAUCGUUGGUAACAGCCCGUCCCAGUAAAGAGCCUAAGUUGCGGGAUAGCACUCGUCGACGGCAUGAGAUUAUUGAAAAGAUCGAUAUAAGGGAGAAAUGCAAGAGCCGCCAGAGUCAUCGUCUUCGUGCGAUUUGCCGUACUAGGGUUUCACGGCUAAAUCUUUUCCAAUCGAUUUUUUCCUAUGGAUGUUUAGACAUGUCGUACAGAGUAAAUAUACUCGUAAUAUCAGUAUGCGCUGCCCUACUCUGGUUGCCGACUGCGUCCCACUUUUAUGAAGGAGCCCUCCCUUGUUCAACUGCGGGGCUGGCCCAUCUGCGGAAAAUGACCAAUAUAUUUCAUAGUCUCAAAAAAAAGUCGGUUUGUUGUGAACAUAGCAAGGUAGAUUUCCUUAACGGGCGGUGCAUCGCAUUAGCCGCGCUGGAAAAGCGGCUACAGACGUGCGCUGCUAUCCUGGGGAACACGCAGCAACCUAAUGAACUAUCGACUGCUAGCACACGUUCUAGGAGAAGGCUAACCCCUGUACUCCCACUUGCACGUACCAGUCAAUUGGUGUAUAGACAGGUUCAAAAGGAGGAUCCAAUAGUCGGUUGCUUAACGCGCUGCUACGGAACGCGAUUCCAGCUCCAAUCCUCUACAUGGAAGGUGGGGUCGCACCUCGCGAAUUUCCAGUUUACAUUGGACUUCGAGAGUCAGCUAGGCGCCAGCAUGAAACGCAUGGGCUCUGUGCGUUACGUCGGCUUGCACUGGGAGGGCGGGCUUGGACUUUUCUCCUUAAAGCGUGUUUCUAUACAAGGAGACCGCACUAAUACGCGGUCUAAGCGCCCAUAUGAUACUGGGAAGGUAAGUACGCACAAGGUGCUACUCAUCCCCGAACCCGUACGGGUCCAUCUCGUAAUCAUCGCGUCCGAUCGUAGGAGUAUGUCGAAAAUGUUUCCACCCCAGCAGGUCCUCGAUAGAGUCCUUCUUCAAAAUAUGUAUAUUUGGCCAGCUAGGACCAGGGACCUGUCUCGACGGAUGCCAACCCCAUACAUCUCAUCUGGCACUGCGCCUGGGGGCCAACUGGUGAAAGAAGUCUGUAUGCCUAAGUUCACCCGCUCAUGGUACUUGGGAGCGGGACUGGCUGCGAAUAGAAGUCAGCCAACUUUGCGCCACACUGUGGUUAAUCGUCCCACCGACUCGCCCACGUUGGUUGCUCUUAGUUGUAGUCGUCGUUUGCAACGCCUAUGCAUUGGGAGUAUCAGGCACCAAUGCAGGGUGUACUACUCCCAUAUGCCCGUGAACUACUCAUGCACGUGUCCCGAUGUUCCGGACUUGCCAAGACGUCGAAGCAACAAGUCCUCCUCACAUAGGACAUGUCUCAGAGGGACAUUAAUAAAACCUAGCUCUGGCCAAAGAAACCAGUCAUGCAGCACCCACGUGUUCAUCCAUACUGACGGGCAUUUAUGCUUUAUGUUCUCAGGGUGCAGCAGGAGCGCCUUUGGCACGGGACGGGCCCCACAGAACCCGGACCCCGCGUCACGCUUCAUAAAAAUGCCUGUAUGUUGCAAAAUGUACCACAAAGACCUCGCCGCACGGAGCCGACGAUUAACGUCUAAAUUGUGUAGUUUCCAGCGUCUCAGAUUCUCGUACCUAGGUGCAACCACUAUGCUUGCAACUCAGCGUAUCGACUCUGUUAGCGAUAGCCACCUGCCAGGUGAUGGAUCCGACCGUACUUACUGUCGUCAUUGGAACAUAGCAUGUAACACCCUACACAGAGUCCACUUGACUUUUACCACCACGCUCAUAUCGCCGUUGAAACUCGCUUUGUACAAUGUGUUUGGGAUAAGAGUUCUUACGCAACUUCGCGUUAGCGCUGGUAAUGGAGAGAAAGACGGUCUUCAACUCUCGGAUCACUUAAUAAUUUUCGAUAGAUCUACAUUAAGCGAUUUGGAUAGUAGAGCUCAGAAAACCCUUCAUCACGGUUAUGAUCCCAGGACUUACGAGGGUGCCAUGGUGACGCCGGACCCACCAUCGCCAUGCCAUAUGGGCGUCCGAACUCACCGGUCCGGAAAGACGAUUCUGCACUUGUGCAGAGUAGGUUACAGUCAGGCCUAUGCCGCGAUUCGCUUGAUAAGAAGUGAGAAGUUUACACGGGGAAGCCUGGACCGUGGAGCAUUUGUGCUCUGCCUACAGUUCGGUCACCUCAAUUCCGCGAUUGCACUCGUAGGUACCGAACUCCCGAGGCCGGGUAGAUUCGGUCAACCAGGAGCCGUUACUUUUUACAUUAAAGCUAGCGUGCGCUUGUUGCCUCGAACGCAGGGCGAGGCUCAUUUAAUAUUACUCGGGACGCAAAACCCGCGCUCGUACCGCUUCCGAGCACCUGGCCAAGAUCUUGACAUUUGUGUCAAUCAAUGCAUCCUGCUGUAUACGUACACGAAAUCACGGCUUGUGUAUCGACCGCAUAUGACUACCACGUUGCAUUCCUUCAUGCGAAACCAUAAUCUCCUGAACUGUCAAAUUUCUCCUAAAUUGGGCACGAGGCUCUCGCCUUGGAACAGGAAACUCAGAUAUCCAUGCAGGUCGCGGGAGGUAAGCGUUCGAGCCUGCUCUAGCAUGAGGAACAUAUCCGGAGUUGUGCUUCGAGGAUGGUACCUUCCCCUACACCCAGAGCGUCAGCCCUUGCAUACGGGCAAUCUCCAUGAUAACUGGAACUCUGGACGGGAAGGUGAGUUGAAUUGUGCAAAUACGUCCAGCGAGAGUGUUCGACCUGGAUUAGAUCAUUCCACGAUUAUCAAUAAGUUGCUAACAACUUCCAUAAACUUACGACUUCGGCCAACCUCCAAAAAGCGCAAACGUGUUUGUCCUUUCUCGAUGGCCCAGCAUUGCUCCUGCUGUGGGUACCACAUACUGCGCGCACUUGCGUAUGGUGUCAGAGAUUAUGAGAAAUUACCUUAUAAACGAUUCACUACCAUUCAGCGGGGUUAUCGACACGCGCUGUUCUAUCGUUGGCUACCCCAAGUUUACGAGUGGAAGAAGCCCCAUCAGACACGUGACUACGCACACACCACGAGUAGUCGCUUUACCGAAGACGACAAACAGUCUCUUGUGCCGGUUCCACUGAUCUUCUUGGGUCCAGAUUCAACACGGUCCCUAUCCCUGCCCCCAAUUAUUACGAAGGAACUUAUGUGUCCCUACGUGCGAAGUAGUAGAGCGGUGUCCCCUUGUUGCUAUAGGGACCAUCUUCGACUGACCCUUUUAAGAGGUUGCCAUGCAAACAUGCCAAAUCCUAGCGUGAGUUCAACCUCGCGCGACACGAACCGCACAUAUGAUACGUGUCUCGCCCCCUGCGAGACGCGGCGAUGCCGGUCAUCUAUUAGAUACUGCGGCACUGCGACUUGGAUUCGCGGAGAAGAGCAAACCCGUCGAUCGGGGACUUCUCGUCCUGCGCGCUGGAUUGUCCCAGGACCCCCAGAAUUCAGCAGUACCUUUCGGUUCCGAGAGGCGCACGAUCUCCGCAUAAGUCAGGACAUGCUUCCGUUCGUCAGGGAGAACAGAGCCACGUCGAGUUGUUUCGUAAAUACAUCCUGGAACGAACAGAUCCUUCCUGCGUUCCGUGAUCGCGUGCGGGACGUAGAGCCGUGUCAAAUGAACCUUAGGAGACUAGCAGUUCGACGCGGCAACCCAUCGUGGAGACUUAAGCUGGGGUACGCGUUAGCACUGACUUCGACACCUUGUCGACGGGAAAUGCGAUCCACGUCGUAUCCAGUCAAGAAGUCCUGCGUGGUUGUGAACACCCGCAGUCUCAUUGCGUCACCAGUAAGUUUUUUGAGGCACGACAUAAUAUUCAAAACAAAUGUCGGGCAAGCGGGAGCAGAUGCCGGACAGAGGGCUUUAAAAGUCGGUGUGUUGCCGAUAAUAUAUUGCCUCUGCCCCUCCUCUUCUAGGUGCUUUAACCAAGUUUUGAUCGGUAGGGGAGGAAAGUUCAUCGGACCGAGUAGUACUGAUCGAUUAGAUGACGCUGUCGAUUCGAGCAAAUUACCAACUGUCCGGGCUCCGAGGCUCAGUGCAGUGACAAGACUACGAUCACUCUCAAUUACUCUCCAGACUUUCGGCAGUUUCGAAUAUCCUAGAAAUCGAUGGACUGAUAGUGUCACGUCCAAAUGUUUUGCUCACACGCGAACACCAUCCCUCGAGUUUAACGGUUAUGUCGCUGUAACUUGUAGGGAAAGAGGUCGGUCAUCAAAUGCCAACCGUCGGGGGAUGUCGUUUUGCGACAAUGCAUCGGAAUGUGCUCCCGUGAGUGAGACUAGUAUGUACGAUAUUAAUCUCAGGUGGCUACCGAGUCUCCACCAUAAACAUGCCUUGACGAGGGGUACGAUACAUAUUUUCUCCUCAUGCAAUCGAUUGAUUAACCCUUACAUUCCUAAACAGAUCACUAUGAUAAUAACCUUCCGCGGCUUUCUGGGUAAUCGCACGUGUCAGUACCGGGGUUACGUCACCGUCUCGGUGUUGCAUAUUUGCCGCAUUGCCUUUUGGUCCACCUCUGCCCUAGGUGUGGUCUCCGUUGUGGUCCCCAUUAUCAGUUGUUCGACGGCGCUGCCAAUUAACCGCCCGGGCUGCUGUGAACCUUACAAGAGCCAUAUCUCCGAAUGCAGUGCACCCAGGAUGAAACCGGGCUCCCCCCUUGCGCACCUACGCUUACGACCCUUGUUCUCGGUUCGCUUGGGACUGUCCUUAUUAGAUGACGGGAACGCGCUCCGGGCUUCGAGAAACUUGAUACUCCCCUGGCCUGUCGCGUGCGUUUUUCCAGUACAACAAUCGCGUUGUCACCUCAGAGGUAGGCUCGUACCAUGGAGAUUUUUUCGCGUCCGGGUUGAACAAGAGGGUCGGCCGGAUAAGUCCCAAUGGCCGCGCGAUGUGGCCGAUCGGUUCCAAAAGCCGUUGUUGCGAGGCGCAUUAGAUAGUCCAGCCGCCGGUUACACUCUGUGGAUCACGUCAGUGGCCUGGCGGCCGCCGCGCAUAUGGCUGAAAUUUCUCUACAGUACGGUCGUUGACGGACAGCCAGGCAUAAUUACACGUACCGAGCCUAGGAAUACAGUAAGGAGAGAAAGAGUAAUGAAGCGAGGUCUACGACUCUUGGAGGACCGAGCGAGUUUGAACACAGCAAAAGUAUGCACGCAAGUGUGUGCAGGCUGUUUGCUUGCUGCGAAGGGGAUCAGAGACCUAGAAGCUGGCCAUCCCUCACCCUUGGAAAAAUUACGUGCGGGUGUUAGACAGGUAAAAUGGCAGUGGACGGGACAUCAAAUACCCGCGCGCCCGGGCCAUGGUCGCAUGCCACCUAUGUUUUUUGUUAUUCUCGUAGGGAGACUUACAAUUGGACGGUUUGCACAAAGUAGUGUGGAAUACUGUCUUUUUUUACAGCGUCCUUCAGGUAGACCCGGCCUCGCAAAGCUCGCCGUCCCGGGAUGGGCCUUAUUGUGGCCUUAUCGACAAGCUUGUUUCAGGUUUAAGCGUUGUAUGGUUCAACAUCUUCGUGUAUGCACGGGCACACCUACGGAAGGUGAGGAACCGGUACGGCCCUGCUAUGGCACGCUCGGGAAUAGAGGUGACGUUAAAUUACUUUCGCAAUUCUCUCGCGCCGGACAGCCUCCUUCAGUUGCUGCUCAUGUGUUGUACGUCAAGGAACCGUCAAACGGUUGGCCACAAUGCGGUCAUCUUAACUCAAUCAGCCUCAAAGGAAGGUCCGGGCAAAUGCUCGUAAUAUUGGAUAUCCCGUUGGGAGCGGCGAGGCGCACUCUCCAGAGUAUCGCAGCGCUGCGCCUGGCACUCCGGUUGAACUCCGCAGUCUCAAUAUCAGCCUUAGUAUUAGUCUCGCAAAAGCUGCAUUGUCAGCCGCGGUAUCAAAUCACAGGCGUCGCCAAAAUUCGUGAAUCAGCCCUGUUUAAGUUCCGUCGGGAUAGUCGCGGUGGCCCUUGUUUGAUCACCCAGGCGUACACUGCGCGGCCCGUUAGUCUACCUAACCCGACCUCAGCUUCAUGUGGUGAUGGGGGUAUUCCAGAUACUAUUACCAACAAGUGUGAUUACACGCGUCGCUGCCCAGAGUCGGUCCGCCUCGCAGAACACAUCGAUCGAUUAGUAGGUACUAAAGGGGGGCGGGUAUUGACAAGCCGUAUGCACGAUUACUUUUUGACAGGCCCAAUGCUAUACAGUCUCACGAUCCUUGAGAUUUAUACUUAUUCGGAGUUUAUCUCGUCUCCGAUUACGAAUGACUCGACCGUCGAGUCCGCAAUAUACCAAUCAGCUCGAAAACUUGCUAGGGACCGAGGGGUCGGAACCACACGCCAUAAAUGGAACGUACUCUUGCCGUUACUGUUUUUACAACCGUGUACUUCCCCUCGGCAGGAAUCGCCCACACCACAGGGGCGAGCCUUUUUCUUUCUGAAGUCUAUCUGGCACGAGACCAUUCGGGAACGGGAAAGUGUGGAUGAGUGUCUUAGCGUCCUCCAGGACUUGCAUACAGACCAGAUCUCAGAUAGUAAGUGUUCCGAGGAGAUUGGCAUAUAUCGAUCCUACAUAUGCCACGGAACGCUAUACUUAGUAAUGAAAAGGGUUCGGCAAGGGUCGCUGCAGCGUUGCACCCUCAUGCAUUCAUCUGCGGUGACUUUAGUCCACCACGCUUGCAAACAAUGGUACGUGAUGUCGGACGUGGCGAUACCUCAGCCGUUGGCCAAUAUCCUGAGCAAAUUCAGGACCACGAUCGGCAAGGUACGAAAGAGUGCUACCAUCCUGAAGCCGGACGGGGGCAAAUCCCAGGGAUGGAACGGGAGCCCGGUUACCAAACUGUACGUUGUGCCGUCGGUCUCGGCAGUAUGGGUGGUAUCGUUCAGUGGACUGUUGUCGACUCACCUCCUGACGUUCUGUGAGGGCCUCGCAGACGCCACGCGGCGAAAAAUGGUAUUCCUGGGGUGGUCGGAUAACCUUUCAAUCAUAGCGCUGACGGACACUUUAUCGGCUAGUUCCCGACAAAACGGUGAGCCGGUGGUACCAUCAGAUCGAAUUGCCCAACCCCAUAAUCAGAAAGGUUCUCUACGGUCGAUCUGCCUGGCGCCAGACAAUUGUAAUUAUCGCGUGUCCUGCGUUAGUCCGACCUUCGCCGGAGAGGCCCACUCAAUAAGGUACUCCCACCGGCCGGCUCCCGAACAGUACCAGUCCAGAAUGAGGCAGUUACCAUCAACUAGUUUAUGUGCUGCCCAUGGUCUAACGUACAGUAUCUUACACCCUUGCCCUUCCAAGAGUAUCCGCGUCCUCGCGAUGAGCGUUUGUAGUACCGCAUCAUACGAGGCUACGUUGUCCGCUUGUGGACUGCUUAAGGGUUUACCAACUGACGAACAACGCUGCAGGCUAAAAGUGAAAGGCAUCUGCCUUGUCCUGUCCCGGCAGAAGACUUUUCAGCUGCAACGAAGCGAACGUCUAGGGGUGUUAGCGAAGUUGCUAAGAGUACGUACGGGAUCCUGGAAUAGGGCGCUACCGGAGACUGUUCGCUAUCGGGACAUGUUUUUCGCGCAACUCCUAGAUAUUUCAAAACCAUGUGAUGGCCCAACUGAUAUUCACGCGCAUUACUCCUUAUGUAGUAAAGGGCCAGCAGAAUCAUUAUCUGGGUCUCAGGAGGCACAUGGUCGGCCAGCCUGCCAUCCCCUUAACGGUCUCCUAUCCAGAGAACCUGCCUAUGUAUAUUCCGACGAGGGUACAAGUCAGGGUUCCACGAAGGGGGUAGACUACCCCAUUCGUAAGGGCAACGGCCAGACAGAGUUACGCAGCAAAACAGGAGCGGUCUGCAAAAUAAAGUCGAGCUGUGUGCCUGAUCCCGAACAAGCAUUAACGAUCUGGACACUGGCGUUCUUUCCUAGGACUCGCUCGGGGACGUUAAACGCGCCGGGCGGACUUAAGCAGAAUUAUAAACAACCAUUACAUAAAUGGAGCUCUGCAGAAAUUUACGCAAUUAAUGAUGAUAAUCAGCAUAAUACGUGCUCGAUUUUAAACAGCCAUCUUCGUUAA"
aas = int(len(mRNA) / 3)
f = open("codons.txt","r")
codons = f.readlines()
length = len(codons)
codon_dictionary = {}
for i in range(0,length):
    row = codons[i]
    for j in range(0,4):
        codon_dictionary[(row[(0+j*11):(3+j*11)])] = (row[(4+j*11)])
translated_sequence = ""
for x in range (0,aas):
    codon = mRNA[(0+3*x):(3+3*x)]
    if codon == "UAA" or codon == "UAG" or codon == "UGA":
        print(translated_sequence)
    else:
        translated_sequence = translated_sequence + codon_dictionary[codon]
print(translated_sequence)