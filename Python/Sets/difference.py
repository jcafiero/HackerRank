#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - Set .difference() Operation

n = int(input())
s1 = set(list(map(int, input().split())))
b = int(input())
s2 = set(list(map(int, input().split())))

s1_dif_s2 = s1.difference(s2)

print(len(s1_dif_s2))
