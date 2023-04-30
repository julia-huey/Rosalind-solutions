# #
# Given: Positive integers n≤40 and k≤5.
#
# Return: The total number of rabbit pairs that will be present after n months, if we begin with
# 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit
# pairs (instead of only 1 pair).

n = 36 # number of months
k = 5 # litter size in rabbit pairs
Fn1 = 1
Fn2 = 0
Fn = 0
for months in range (0,(n-1)):
    Fn = (k * Fn2) + Fn1
    Fn2 = Fn1
    Fn1 = Fn
print(Fn)





