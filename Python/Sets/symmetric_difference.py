#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - Symmetric Difference

def make_set():
    input()
    return set(map(int, input().split(' ')))

m, n = [make_set() for x in range(2)]
{print(x) for x in sorted(m ^ n)}
