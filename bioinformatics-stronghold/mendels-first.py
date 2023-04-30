# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals
# are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual
# possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two
# organisms can mate.
k = 25
m = 21
n = 15
p = k + m + n #total population p
combos = 0
for i in range (1,(p)):
    combos = combos + i # determines possible unique matings within the population
    # (sum of 1 thru n-1 where n = population)
print(combos)
outcomes = 4 * combos #(4 outcomes per punnett square)
kx_pairs = 0
c = 1
for i in range (0,k):
    kx_pairs = kx_pairs + (p - c)
    c = c + 1
#computes number of unique pairings where at least one parent is homozygous dominant (k)
mm_pairs = 0
d = 1
for j in range (0,m):
    mm_pairs = (m - d) + mm_pairs
    d = d + 1

nn_pairs = 0
e = 1
for l in range (0,n):
    nn_pairs = (n - e) + nn_pairs
    e = e + 1
mn_pairs = combos - (nn_pairs + mm_pairs + kx_pairs)
print(kx_pairs)
print(mm_pairs)
print(mn_pairs)
pD = ((kx_pairs * 4) + (3 * mm_pairs) + (2 * mn_pairs)) / outcomes
print(pD)