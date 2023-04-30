f = open("rosalind_subs.txt","r")
s = f.readline()
t = f.readline()
print(s)
print(t)
output = ""
print(len(s))
print(len(t))
print(t[0:10])
for i in range(0,len(s)):
    if t[0:len(t)] == s[i:len(t)+i]:
        output = output + str(i+1) + " "
    else:
        output = output
print(output)
