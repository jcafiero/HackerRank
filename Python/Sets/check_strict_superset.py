#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - Check Strict Superset

A = set(input().split())
n = int(input())
for _ in range(n):
    N = set(input().split())
    if (N < A):
        continue
    else:
        print(False)
        break
else:
    print(True)
